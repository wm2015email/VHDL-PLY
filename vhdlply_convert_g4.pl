#!/usr/bin/perl

######################################################
# Attempting to make a VHDL lexer using Python PLY
# GNU License
# William P. Moore
# 8/8/2024
######################################################

use strict;
use warnings;

my $output_file = 'vhdlply_yacc.py';

my $input_file  = 'rules_vhdl.g4';         # modified antlr project vhdl rules
#my $input_file  = 'rules_vhdl2000.lmr';    # vhdl-2000 lmr rules


my $lmr_mode = 0;
if ($input_file =~ /.lmr$/) {
   $lmr_mode = 1;
}

open(my $in,  '<', $input_file) or die "Could not open file '$input_file' $!";
open(my $out, '>', $output_file) or die "Could not open file '$output_file' $!";

print "reading: $input_file\n";
print "reading: $output_file\n";

print $out "#!/usr/bin/python3\n";
print $out "\n";
print $out "# PLY Yacc script generated from vhdl.g4\n";
print $out "import ply.yacc as yacc\n";
print $out "from vhdlply_lexer import tokens\n\n";  # Assuming a separate vhdl_lex.py file for tokens
print $out "\n";
print $out "start =  'design_file'\n";
print $out "\n";
print $out "yacc_debug_file = 'parsedebug.txt'\n";
print $out "\n";
print $out "debug_def  = False\n";
print $out "debug_yacc = True\n";
print $out "\n";

#-----------------------------------------------------
# Load G4 File
#-----------------------------------------------------
my $inum      = 0;
my $indent    = "";
my @rule_list = ();
my $rline     = "";
my $rname     = "";
my $wauto     = 0;
my $state     = 0;

my %not_a_token = (
	"BIT_STRING_LITERAL" => 1
);

while (my $line = <$in>) {
    chomp $line;
		
	$line =~ s/^\s*//;
	$line =~ s/\s*$//;

    if ($lmr_mode) {
		$line =~ s/^\s*#.*$//;

        $line =~ s/\b(\w+)__(\w+)\b/$2/g;
		
		# zero or one 
		$line =~ s/\[/(/g;
		$line =~ s/\]/)?/g;

        # zero or more
		$line =~ s/\{/(/g;
		$line =~ s/\}/)*/g;
		
	}
	
	# g4 mode
	else {
        $line =~ s/^\/\/.*$//;
		
        # REMOVE EOF TOKEN
        $line =~ s/\s*\bEOF\b\s*//g;

        # hacky fix
        $line =~ s/\(: identifier\)\s*$/ identifier /g;	
	
	    # Remove non-capture groups?!??  (: ... ) =>  ( )
	    $line =~ s/\(\:/(/g;
	}
		
	next if ($line =~ /^$/);
		
	if ($state eq 0) {
	    if ($line =~ /^(\w+)$/) {
	         #print "!1 $1\n";
		     $rname  = $1;
		     $rline = "$1";
			 $state = 1;
	    }
	}
	elsif ($state eq 1) {
	    if ($line =~ /^:\s+(.*)$/) {
			$state = 1;
	        #print "!2 $1 <=> $2\n";
		    $rline = "${rline} ${line}";
	    }
	    elsif ($line =~ /^\|\s+(.*)$/) {
			$state = 1;
	        #print "!2 $1 <=> $2\n";
		    $rline = "${rline}\n${line}";
	    }
	    elsif ($line eq ";") {
			$state = 0;
		    # skip token rules
		    #if ($rname =~ /^[A-Z0-9_]+$/) {
			#	if (!defined($not_a_token{$rname})) {
			#        #print "SKIP TOKEN RULE: $rule\n";
			#        next;
		    #	}
		    #}
		    $rline = "${rline}\n";			
			push(@rule_list, $rline);
		}
		else {
		    $rline = "${rline} ${line}";
		}
		
    }
}

#-----------------------------------------------------
# Convert G4 to PLY Yacc
#-----------------------------------------------------
my $new_rule    = "";
my %warpdone    = ();
my $junker      = "";
my $bx          = "";
my @branch      = ();
my $b0          = "";
my $b1          = "";
my $warp        = "";
my $wname       = "";
my $wexpr       = "";
my $wtype       = "";
my $rule_curr   = "";
my @new_rules   = ();

#Foreach rule in G4 File
for my $rule_curr (@rule_list) {
	my @rcurr   = split(/\n/, $rule_curr);
	my @rpart   = split(/\s*:\s*/, $rcurr[0]);
	$rname      = $rpart[0];	
	$wname      = "";

	#-------------------------------------
	# Transform1
	#-------------------------------------
	while (1) {

		#regex: '(' anything until matching ')' <'?'|'+'|'*'>
        my @result = get_altr_group($rule_curr);
		last if (@result == 0);
	
   	    $junker = $result[0];
	    $wexpr  = $result[1];
	    $wtype  = $result[2];
		$warp   = $result[1];
		$wname  = "";
		
		if ($warp =~ /\s+/) {
		    $warp = "warp${wauto}";
			$wauto++;
		}
		
		$junker  = quotemeta($junker);
	    		
		if ($wtype eq '*') {
		    $wname          = "${warp}_a1star";
			
		    $rule_curr      =~ s/$junker/$wname/; 
		
			$wexpr = "($wexpr)" if ($wexpr =~ /\|/);
			
			if (!defined($warpdone{$wname})) {
			    $warpdone{$wname} = 1;
		        $new_rule  = "$wname : $wexpr $wname\n";
		        $new_rule .= "| empty\n";	
                push(@rule_list, $new_rule);
                #print "newrule: $new_rule\n";
		    }				
		}
		elsif ($wtype eq '+') {
		    $wname          = "${warp}_a1plus";

		    $rule_curr      =~ s/$junker/$wname/; 
			
			$wexpr = "($wexpr)" if ($wexpr =~ /\|/);
		    
			if (!defined($warpdone{$wname})) {
			    $warpdone{$wname} = 1;
			    $new_rule  = "$wname : $wexpr $wname\n";
		        $new_rule .= "| $wexpr\n";
                push(@rule_list, $new_rule);	
                #print "newrule: $new_rule\n";				
			}
		}		
		elsif ($wtype eq '?') {
		    $wname          = "${warp}_a1mark";
			
		    $rule_curr      =~ s/$junker/$wname/; 
			
			$wexpr = "($wexpr)" if ($wexpr =~ /\|/);
		    
			if (!defined($warpdone{$wname})) {				
			    $warpdone{$wname} = 1;
			    $new_rule  = "$wname : $wexpr\n";
		        $new_rule .= "| empty\n";	
                push(@rule_list, $new_rule);	
                #print "newrule: $new_rule\n";
			}					
	    }

	} # End Tranform1


	#-------------------------------------
	# Transform2
	#-------------------------------------
	while(1) {
		# regex: '(' <anything that's not ')'> | <anything that's not ')'> ')'
		if ($rule_curr =~ /(\(([^)]*\|[^)]*)\))/) {
			$junker      = $1;
			$bx          = $junker; $bx =~ s/^\(//; $bx =~ s/\)$//;
			@branch      = split(/\|/, $bx);
			$b0          = $branch[0];
			$b1          = $branch[1];
		    $warp        = "warp${wauto}"; $wauto++;
		    $wname       = "${warp}_a1branch";

		    $junker         = quotemeta($junker);
		    $rule_curr      =~ s/$junker/$wname/;
			
		    if (!defined($warpdone{$wname})) {				
			    $warpdone{$wname} = 1;
		        $new_rule = "$wname : $b0\n";
		        $new_rule .= "| $b1\n";
                push(@rule_list, $new_rule);	
			}
		}
		last;
	} # End Tranform2
	
	#-------------------------------------
	# Write PLY Rule
	#-------------------------------------		
	$inum   = 4*0; $indent = " " x $inum;		
	print $out "${indent}def p_${rname}(p):\n";
		
	$inum   = 4*1; $indent = " " x $inum;		
    print $out "${indent}'''\n";
	my @rule_curr = split(/\n/, $rule_curr);
	for my $x (@rule_curr) {
        print $out "${indent}$x\n";
		$inum   = 4*2; $indent = " " x $inum;
	} 
	$inum   = 4*1; $indent = " " x $inum;
	print $out "${indent}'''\n";
	print $out "${indent}if debug_def: print(\"\\n=> $rname\", p[1:])\n";
	print $out "${indent}p[0] = p[1:]\n";
	print $out "\n";
	
	if (${rname} eq "architecture_body") {
        print $out "${indent}type   = \"arch\"\n";
        print $out "${indent}name   = p[2][0]\n";
        print $out "${indent}entity = p[4][0]\n";
        print $out "${indent}loc  = f\"{p.lexer.file}:{p.lineno(1)}:\"\n";
        print $out "${indent}print(f\"===> {loc:<20} {type:<10} {entity:<10} of:{name:<10} \")\n";
	    print $out "\n";
	}
	
	if (${rname} eq "entity_declaration") {
        print $out "${indent}type   = \"entity\"\n";
        print $out "${indent}name   = p[2][0]\n";
        print $out "${indent}loc  = f\"{p.lexer.file}:{p.lineno(1)}:\"\n";
        print $out "${indent}print(f\"===> {loc:<20} {type:<10} {name:<10} \")\n";
	    print $out "\n";
	}

}


my @out = (
  "# Define the empty rule to handle the zero occurrences case",
  "def p_empty(p):",
  "    '''",
  "    empty : ",
  "    '''",
  "    pass",
  "",
  "# Error rule for syntax errors",
  "def p_error(p):",
  "    print(f\"PARSE ERROR: value:{p.value} lineno:{p.lineno} pos:{p.lexpos} type:{p.type}\\n\")",
  "    exit(-1);",
  "",
  "import logging",
  "log = logging.getLogger('ply')",
  "logging.basicConfig(",
  "    level = logging.DEBUG,",
  "    filename = yacc_debug_file,",
  "    filemode = \"w\",",
  "    format = \"%(filename)10s:%(lineno)4d:%(message)s\"",
  ")",
  "",
  "parser = None",
  "",
  "def new_parser(start):",
  "    global parser",
  "",
  "    if debug_yacc:",
  "        print(f\"creating yacc debug file: {yacc_debug_file}\")",
  "        parser = yacc.yacc(debug=True, errorlog=log, start=start)",
  "    else:",
  "        parser = yacc.yacc()",
  "",
  "new_parser(\"design_file\")",
 );



for my $line (@out) {
	print $out "$line\n"; 	
}
print $out "\n";

print "finished: $output_file\n";
close($out);
close($in);

exit 1;

#####################################################################33

sub get_altr_group {
    my $str = shift;
    my $len = length($str);
    my $found = 0;
    my $result = '';
	my $end1   = undef;
    my $end2   = undef;
	
    # Traverse the string to find ')x' attributes
    for (my $i = 0; $i < $len - 1; $i++) {
	    $end1 = substr($str, $i,   1); #) 
	    $end2 = substr($str, $i+1, 1); #x
		next if !(($end2 eq '*') || ($end2 eq '+') || ($end2 eq '?'));
		#print ">> $end1 $end2\n";
		
        # Find the matching opening bracket
        my $count = 0;
        for (my $j = $i - 1; $j >= 0; $j--) {
            if (substr($str, $j, 1) eq ')') {
                $count++;
            } elsif (substr($str, $j, 1) eq '(') {
                $count--;
            }

            if ($count == -1) {
                # Extract the substring from the matching '(' to ')x'
                $result = substr($str, $j, $i - $j + 2);
                $found = 1;
                last;
            }
        }
        last if $found;
        
    }

    if (!$found) {
		return ();
    }

    my $expr = $result;
    $expr =~ s/^\(\s*//;
    $expr =~ s/\s*\).$//;
	
	return ($result, $expr, $end2);
}

