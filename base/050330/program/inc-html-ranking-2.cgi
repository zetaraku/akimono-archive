# 爵位リスト下請け 2003/07/19 由來

$disp.="<BIG>●新聞：爵位リスト</BIG><br><br>";

my @itemlist=();
my %msg;
my $bar;

foreach my $DT (@DT)
{
	my $shopname=$DT->{shopname};
	my $name=$DT->{name};
	my $count=$DT->{dignity};
	next if !$count;
	my $num=0;
	foreach(1..$#DIG_POINT)
	{
		last if $count<$DIG_POINT[$_];
		$num++;
	}
	$msg{$num}.=$shopname."， ";
}

my $ret;
foreach (1..$#DIG_POINT) {
	$msg{$_} = substr($msg{$_},0,(length($msg{$_})-3)) if ($msg{$_});
	$ret=$TR.$TDB.DignityDefine($DIG_POINT[$_],2).$TD.$msg{$_}.$TRE.$ret;
}
$disp.="$TB$TR<td width=50>爵位<td class=b width=570>店名$TRE";
$disp.=$ret.$TBE;
1;
