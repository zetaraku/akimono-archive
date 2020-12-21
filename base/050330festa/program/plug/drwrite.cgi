# drwrite プラグイン 2005/03/30 由來

sub WriteRanch
{
	my @MESSAGE=();
	foreach my $i(0..$RCcount)
		{
		next if !$RC[$i]->{name};
		$MESSAGE[$i]=join(",",map{$RC[$i]->{$_}}@RCnamelist)."\n";
		}
	OpenAndCheck(GetPath($COTEMP_DIR,"dra-rc"));
	print OUT @MESSAGE;
	close(OUT);
}

sub WriteStable
{
	my @MESSAGE=();
	foreach my $i(0..$STcount)
		{
		next if !$ST[$i]->{name};
		$MESSAGE[$i]=join(",",map{$ST[$i]->{$_}}@STnamelist)."\n";
		}
	OpenAndCheck(GetPath($COTEMP_DIR,"dra-st"));
	print OUT @MESSAGE;
	close(OUT);
}

sub WriteJock
{
	my @MESSAGE=();
	foreach my $i(0..$JKcount)
		{
		next if !$JK[$i]->{name};
		$MESSAGE[$i]=join(",",map{$JK[$i]->{$_}}@JKnamelist)."\n";
		}
	OpenAndCheck(GetPath($COTEMP_DIR,"dra-jk"));
	print OUT @MESSAGE;
	close(OUT);
}

sub WriteDragon
{
	my @MESSAGE=();
	foreach my $i(0..$DRcount)
		{
		next if !$DR[$i]->{name};
		$MESSAGE[$i]=join(",",map{$DR[$i]->{$_}}@DRnamelist)."\n";
		}
	OpenAndCheck(GetPath($COTEMP_DIR,"dra-dr"));
	print OUT @MESSAGE;
	close(OUT);
}

sub WriteParent
{
	my @MESSAGE=();
	foreach my $i(0..$PRcount)
		{
		next if !$PR[$i]->{name};
		$MESSAGE[$i]=join(",",map{$PR[$i]->{$_}}@PRnamelist)."\n";
		}
	OpenAndCheck(GetPath($COTEMP_DIR,"dra-pr"));
	print OUT @MESSAGE;
	close(OUT);
}

sub WriteRace
{
	my($fn)=@_;
	$fn||=0;
	my @MESSAGE=();
	$MESSAGE[0]=join(",",@RDS)."\n";
	foreach my $i(1..$RDcount)
		{
		next if !$RD[$i-1]->{name};
		$MESSAGE[$i]=join(",",map{$RD[$i-1]->{$_}}@RDnamelist)."\n";
		}
	OpenAndCheck(GetPath($COTEMP_DIR,"dra-rd$fn"));
	print OUT @MESSAGE;
	close(OUT);
}

sub WriteDrLast
{
	my $message='@DRTIME=('.$DRTIME[0].','.$DRTIME[1].','.$DRTIME[2].");\n1;\n";
	OpenAndCheck(GetPath($COTEMP_DIR,"dr-last"));
	print OUT $message;
	close(OUT);
}

1;
