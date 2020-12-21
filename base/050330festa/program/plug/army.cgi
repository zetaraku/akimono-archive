# army プラグイン 2003/07/19 由來

sub ReadArmy
{
	undef %ARMY;
	undef %RIOT;
	open(IN,GetPath("army"));
	my @buf=<IN>;
	close(IN);
	chop $buf[0];
	%ARMY=split(/,/,$buf[0]);
	chop $buf[1];
	foreach(split(/,/,$buf[1])) {
	next if !defined($id2idx{$_});
	$RIOT{$_}=1;
	}
}

sub WriteArmy
{
	OpenAndCheck(GetPath($TEMP_DIR,"army"));
	foreach(keys(%ARMY)) {
	delete $ARMY{$_} if !defined($id2idx{$_});
	delete $ARMY{$_} if !$ARMY{$_};
	}
	print OUT join(",",%ARMY)."\n";
	print OUT join(",",keys(%RIOT))."\n";
	close(OUT);
}
1;
