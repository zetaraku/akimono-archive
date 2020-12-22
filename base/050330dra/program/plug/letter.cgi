# letter プラグイン 2003/11/03 由來

sub WriteLetter
{
	my @MESSAGE=();
	my @LETTERnamelist=
		qw(
			no time fromt fromid tot toid title msg mode other
		);
	foreach my $i(0..$Lcount)
		{
		next if $LETTER[$i]->{mode}==2;		#削除する手紙
		$MESSAGE[$i]=join(",",map{$LETTER[$i]->{$_}}@LETTERnamelist)."\n";
		}
	OpenAndCheck(GetPath($COTEMP_DIR,$BOX_FILE));
	print OUT @MESSAGE;
	close(OUT);
}

sub SearchLetterName
{
	my($no,$to)=@_;
	return '(宅配便のお知らせ)' if $no==1;
	foreach(0..$Ncount{$to})
		{
		return $LNAME{$to}[$_] if ($no==$LID{$to}[$_]);
		}
	return "(不明)";
}

sub ReadLetter
{
	my @LETTERnamelist=
		qw(
			no time fromt fromid tot toid title msg mode other
		);
	undef @RECLETTER;
	$NeverR=0;
	undef @SENLETTER;
	$NeverS=0;
	my $datafile=GetPath($COMMON_DIR,$BOX_FILE);
	open(IN,$datafile) or return();
	my @MESSAGE=<IN>;
	close(IN);
	$Lcount=$#MESSAGE;
	return if $Lcount < 0;
	foreach my $cnt(0..$Lcount)
	{
	chop $MESSAGE[$cnt];
	my @buf=split(/,/,$MESSAGE[$cnt]); my $i=0;
	foreach (@LETTERnamelist) { $LETTER[$cnt]->{$_}=$buf[$i];$i++;}
	$LETTER[$cnt]->{mode}=2 , next if ($NOW_TIME - $LETTER[$cnt]->{time}) > $BOX_STOCK_TIME;	#期限切れ

	if ($MYDIR eq $LETTER[$cnt]->{tot} && $LETTER[$cnt]->{toid}==$DT->{id})
		{
		push(@RECLETTER, $cnt);
		$NeverR++ if ($LETTER[$cnt]->{mode}==1);
		}
	if ($MYDIR eq $LETTER[$cnt]->{fromt} && $LETTER[$cnt]->{fromid}==$DT->{id})
		{
		push(@SENLETTER, $cnt);
		$NeverS++ if ($LETTER[$cnt]->{mode}==1);
		}
	}
}

sub ReadLetterName
{
	my $a;
	foreach my $pg(@OtherDir)
	{
	my $datafile='../'.$pg.'/data/user.cgi';
	open(IN,$datafile) or return();
	my @data=<IN>;
	close(IN);
	$Ncount{$pg}=scalar(@data) - 1;
	foreach my $i(0..$Ncount{$pg})
		{
		($a,$LNAME{$pg}[$i],$LID{$pg}[$i])=split(/\t/,$data[$i]);
		}
	}
}
1;
