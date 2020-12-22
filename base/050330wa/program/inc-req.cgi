# 依頼下請け関数 2003/09/25 由來

$MENUSAY=GetMenuTag('stock',	'[倉庫を確認する]')
	.GetMenuTag('req','[依頼一覧に戻る]')
	.GetMenuTag('town',	'[依頼所を出る]');
$AucImg=GetTagImgKao("受付","req");

@REQnamelist=qw(
		no tm id itemno num prn pr mode
		);
ReadReq();
1;

sub ReadReq
{
$REQNONE=1;
undef @REQ;
open(IN,GetPath("request")) or return;
my @req=<IN>;
close(IN);
$Scount=$#req;
return if $Scount < 0;
foreach my $cnt(0..$Scount)
	{
	chop $req[$cnt];
	my @buf=split(/,/,$req[$cnt]); my $i=0;
	foreach (@REQnamelist) { $REQ[$cnt]->{$_}=$buf[$i];$i++;}
	undef $REQ[$cnt],next if ($REQ[$cnt]->{tm} < $NOW_TIME);	# 期限切れを削除。
	$REQNONE=0;
	}
}

sub SearchReqIndex
{
	my($no)=@_;
	foreach(0..$Scount)
		{
		return $_ if ($no==$REQ[$_]->{no});
		}
	return -1;
}

