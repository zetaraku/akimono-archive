# drread aプラグイン 2005/03/30 由來

sub ReadStable
{
$MYST=-1;
$STcount=-1;
undef @ST;
undef %id2st;
open(IN,GetPath($COMMON_DIR,"dra-st")) or return;
my @req=<IN>;
close(IN);
$STcount=$#req;
return if $STcount < 0;
foreach my $cnt(0..$STcount)
	{
	chop $req[$cnt];
	my @buf=split(/,/,$req[$cnt]); my $i=0;
	foreach (@STnamelist) { $ST[$cnt]->{$_}=$buf[$i];$i++;}
	$ST[$cnt]->{win}=$ST[$cnt]->{g1win}+$ST[$cnt]->{g2win}+$ST[$cnt]->{g3win}+$ST[$cnt]->{sdwin};

	my $id=$ST[$cnt]->{no};
	$id2st{$id}=$cnt;

	next if ($MYDIR ne $ST[$cnt]->{town});
	undef $ST[$cnt],next if !defined($id2idx{$ST[$cnt]->{owner}});	# 読み飛ばし。

	if ($ST[$cnt]->{owner}==$DT->{id})
		{
		$MYST=$cnt;
		}
	}
}

sub ReadJock
{
$MYJK=-1;
$JKcount=-1;
undef @JK;
undef %id2jk;
open(IN,GetPath($COMMON_DIR,"dra-jk")) or return;
my @req=<IN>;
close(IN);
$JKcount=$#req;
return if $JKcount < 0;
foreach my $cnt(0..$JKcount)
	{
	chop $req[$cnt];
	my @buf=split(/,/,$req[$cnt]); my $i=0;
	foreach (@JKnamelist) { $JK[$cnt]->{$_}=$buf[$i];$i++;}
	$JK[$cnt]->{win}=$JK[$cnt]->{g1win}+$JK[$cnt]->{g2win}+$JK[$cnt]->{g3win}+$JK[$cnt]->{sdwin};

	my $id=$JK[$cnt]->{no};
	$id2jk{$id}=$cnt;

	next if ($MYDIR ne $JK[$cnt]->{town});
	undef $JK[$cnt],next if !defined($id2idx{$JK[$cnt]->{owner}});	# 読み飛ばし。

	if ($JK[$cnt]->{owner}==$DT->{id})
		{
		$MYJK=$cnt;
		}
	}
}

1;
