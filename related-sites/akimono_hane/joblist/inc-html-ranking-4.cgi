# 職業一覧 2005/01/07 BASARA
# 改変 seraphy

$disp.="<BIG>●新聞：職業一覧</BIG><br><br>";
my %msg;
my $bar;
foreach my $DT (@DT){
	my $shopname=$DT->{shopname};
	my $job=$DT->{job};
	foreach("",(keys %JOBTYPE)){
		if ($job eq $_){$msg{$_}.=$shopname."， ";}
	}
}
my $ret;
foreach ("",(keys %JOBTYPE)){
	$jobname="すっぴん";
	$jobname=$JOBTYPE{$_} if ($JOBTYPE{$_});
	$msg{$_} = substr($msg{$_},0,(length($msg{$_})-3)) if ($msg{$_});
	$ret=$ret.$TR.$TDB.GetTagImgJob($_).$jobname."<td width=570>".$msg{$_}.$TRE;
}
$disp.="$TB$TR<td width=50>ジョブ名<td class=b width=570>店名$TRE";
$disp.=$ret.$TBE;
1;
