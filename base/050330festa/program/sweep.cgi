# お掃除 2004/01/20 由來

DataRead();
CheckUserPass();
RequireFile('inc-html-ownerinfo.cgi');

$disp.="<BIG>●お掃除</BIG><br><br>";

my $usetime=GetTimeDeal($DT->{trush})-$TIME_SEND_MONEY+3599;	#端数を切り上げ
my $time=int($usetime/3600);
my $stocktime=int(GetStockTime($DT->{time})/3600);

if($DT->{trush} < 10000)
{
	$disp.=$TB.$TR;
	$disp.=$TD.GetTagImgKao("お掃除アドバイザ","sweep").$TD;
	$disp.="お掃除アドバイザ：現在お店に目立ったごみはありません。<br>";
	$disp.="またごみがたまったら，こまめに掃除しましょう。";
	$disp.=$TRE.$TBE;
HTML
}
else
{
	$disp.=$TB.$TR;
	$disp.=$TD.GetTagImgKao("お掃除アドバイザ","sweep").$TD;
	$disp.="お掃除アドバイザ：現在".int($DT->{trush}/10000)."kg相当のごみがありますね。<br>";
	$disp.="これを全部片付けるには".GetTime2found($usetime)."くらいかかりそうです。";
	$disp.=$TRE.$TBE;

	if ($stocktime < 1)
	{
	$disp.=<<"HTML";
	<br><BIG>●時間指定：</BIG>時間が足りません
HTML
	}
	else
	{
	$disp.=<<"HTML";
	<br><FORM ACTION="action.cgi" $METHOD>
	<INPUT TYPE=HIDDEN NAME=key VALUE=sweep-s>
	$USERPASSFORM
	<BIG>●時間指定：</BIG>
	<SELECT NAME=cnt1>
	<OPTION VALUE="0" SELECTED>
HTML
	$msg{1}=1; $msg{2}=2; $msg{3}=3; $msg{5}=5; $msg{10}=10;
	$msg{$stocktime}="$stocktime(時間最大)";
	$msg{$time}="$time(掃除最大)";
	my $oldcnt=0;
	foreach my $cnt (sort { $a <=> $b } (1,2,3,5,10,$time,$stocktime))
	{
		last if $time<$cnt || $stocktime<$cnt || $cnt==$oldcnt;
		$disp.="<OPTION VALUE=\"$cnt\">$msg{$cnt}";
		$oldcnt=$cnt;
	}
	$disp.=<<STR;
	</SELECT>
	時間、もしくは
	<INPUT TYPE=TEXT SIZE=7 NAME=cnt2>時間
	<INPUT TYPE=SUBMIT VALUE="掃除する"></FORM>
STR
	}
}

OutSkin();
1;
