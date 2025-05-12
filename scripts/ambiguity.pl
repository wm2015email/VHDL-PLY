

$file = "vhdl.lmr";

%save = ();

open(F, $file) || die("cannot open: $file");

while(<F>) {
    $line = $_;
	$line =~ s/#.*$//;
	$line =~ s/^\s+//;
	$line =~ s/\s+$//;
	
	next if ($line =~ /^\s*$/);
	
	@tok = split(/\s+/, $line);
	for $tok (@tok) {
	    if ($tok =~ /__/) {
		    $save{$tok} = 1;
		}
	}
	
}

@list = ();

for $tok (keys %save) {
	@c = split(/__/, $tok);
	$sline = $c[1] . " " . $c[0];
	push(@list, $sline);
}

@slist = sort(@list);

for $tok (@slist) {
	@c = split(/ /, $tok);
	$sline = $c[1] . "__" . $c[0];
    print "$sline\n";
}

