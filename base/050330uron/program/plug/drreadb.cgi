# drread プラグイン 2005/03/30 由來

sub ReadRanch
{
$MYRC=-1;
$RCcount=-1;
undef @RC;
undef %id2rc;
open(IN,GetPath($COMMON_DIR,"dra-rc")) or return;
my @req=<IN>;
close(IN);
$RCcount=$#req;
return if $RCcount < 0;
foreach my $cnt(0..$RCcount)
	{
	chop $req[$cnt];
	my @buf=split(/,/,$req[$cnt]); my $i=0;
	foreach (@RCnamelist) { $RC[$cnt]->{$_}=$buf[$i];$i++;}
	$RC[$cnt]->{aprize}=int($RC[$cnt]->{prize} / ($NOW_TIME - $RC[$cnt]->{birth} + 1) * 86400 * 2);

	my $id=$RC[$cnt]->{no};
	$id2rc{$id}=$cnt;

	next if ($MYDIR ne $RC[$cnt]->{town});

	undef $RC[$cnt],next if !defined($id2idx{$RC[$cnt]->{owner}});	# 読み飛ばし。
	if ($RC[$cnt]->{owner}==$DT->{id})
		{
		$MYRC=$cnt;
		}
	}
}

sub ReadDragon
{
@MYDR=();
$DRcount=-1;
undef @DR;
undef %id2dra;
open(IN,GetPath($COMMON_DIR,"dra-dr")) or return;
my @req=<IN>;
close(IN);
$DRcount=$#req;
return if $DRcount < 0;
foreach my $cnt(0..$DRcount)
	{
	chop $req[$cnt];
	my @buf=split(/,/,$req[$cnt]); my $i=0;
	foreach (@DRnamelist) { $DR[$cnt]->{$_}=$buf[$i];$i++;}

	my $id=$DR[$cnt]->{no};
	$id2dra{$id}=$cnt;

	if ($MYDIR eq $DR[$cnt]->{town} && $DR[$cnt]->{owner}==$DT->{id})
		{
		push(@MYDR,$cnt);
		}
	}
}

sub ReadParent
{
@MYPR=();
$PRcount=-1;
undef @PR;
undef %id2pr;
open(IN,GetPath($COMMON_DIR,"dra-pr")) or return;
my @req=<IN>;
close(IN);
$PRcount=$#req;
return if $PRcount < 0;
foreach my $cnt(0..$PRcount)
	{
	chop $req[$cnt];
	my @buf=split(/,/,$req[$cnt]); my $i=0;
	foreach (@PRnamelist) { $PR[$cnt]->{$_}=$buf[$i];$i++;}

	my $id=$PR[$cnt]->{no};
	$id2pr{$id}=$cnt;

	next if ($MYDIR ne $PR[$cnt]->{town});

	undef $PR[$cnt],next if !defined($id2idx{$PR[$cnt]->{owner}});	# 読み飛ばし。
	if ($PR[$cnt]->{owner}==$DT->{id} && $PR[$cnt]->{fm})
		{
		push(@MYPR,$cnt);
		}
	}
}

sub GetRaceApt
{
	my($apt,$fl,$mode)=@_;
	my $m1=$apt - ($fl * 8) - 150;
	$m1=int($m1 / 10)*10;
	$m1=1200 if $m1 < 1200;

	my $m2=$apt + ($fl * 8) + 150;
	$m2=int($m2 / 10)*10;
	$m2=3200 if $m2 > 3200;

	if ($mode)
		{
		my $i;
		$i=$m1-$mode, return $i if ($mode < $m1);
		$i=$m2-$mode, return $i if ($mode > $m2);
		return 0;
		}
	return "$m1～$m2";
}

sub GetRaceStrate
{
	my($sr,$ag)=@_;
	return 0 if ($sr > $ag * 3) && ($sr > 80);
	return 1 if ($sr > $ag * 1.2);
	return 3 if ($ag > $sr * 3) && ($ag > 80);
	return 2 if ($ag > $sr * 1.2);
	return 4;
}

1;
