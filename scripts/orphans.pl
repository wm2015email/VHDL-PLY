

$file = "vhdl.lmr";

%save = ();

open(F, $file) || die("cannot open: $file");

while(<F>) {
    $line = $_;
	$line =~ s/^\s*#.*$//;
	$line =~ s/^\s+//;
	$line =~ s/\s+$//;
	
	next if ($line =~ /^\s*$/);
	
	
	@tok = split(/\s+/, $line);
	for $tok (@tok) {
		if ($tok =~ /__(.*)$/) {
			$tok = $1;
		}
		if (!defined($save{$tok})) {
		    $save{$tok} = 1;
		}
		else {
		    $save{$tok} = $save{$tok} + 1; 
		}
	}
	
}

@list = ();

for $tok (keys %save) {
	if ($save{$tok} <= 1) {
		push(@list, $tok);
	}
}

@slist = sort(@list);

for $item (@slist) {
    print "orphan: $item\n";
}

$grepfile = "vhdlply_lexer.py";
open(G, $grepfile) || die("cannot open file: $grepfile\n");
while(<G>) {
	$line = $_;
	push(@glines, $line);
}
close(G);

for $sline (@slist) {
	$found = 0;
	for $gline (@glines) {
		if ($gline =~ /$sline/i) {
			$found = 1;
			last;
		}
	}
	if (!$found) 
	{
		print "missing: $sline\n";
	}
}
