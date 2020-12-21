# 荘園種購入 2005/03/30 由來

$NOITEM=1;
$NOMENU=1;
DataRead();
CheckUserPass();
OutError("領主がいないので荘園制度が機能していません") if !defined($id2idx{$STATE->{leader}});
RequireFile('inc-manor.cgi');

	# 荘園設定を取得
	my $i=$id2idx{$STATE->{leader}};
	ReadDTSub($DT[$i],"lord");
	$MANORLORD=$DT[$i]->{_lord};

	ReadDTSub($DT,"seed");

my $usetime=10*60;
$i=int($Q{buy});

my @MYMANOR=@{$MANOR[$i]};
$price=$MANORLORD->{"price$i"};
OutError("bad request") if !$price;

$stock=$MANORLORD->{"count$i"};
OutError("販売在庫が尽きています") if !$stock;

RequireFile('inc-html-ownerinfo.cgi');

$disp.="<BIG>●購入</BIG><br><br>";

$disp.=$TB.$TR.$TDB."商品".$TD;
$disp.=GetTagImgManor($MYMANOR[1]).$MYMANOR[0].$TRE;
$disp.=$TR.$TDB."価格".$TD.'@'.GetMoneyString($price).$TRE;
$disp.=$TR.$TDB."販売在庫数".$TD.$stock." 個".$TRE;
$disp.=$TR.$TDB.'自店保有数'.$TD.($DT->{_seed}->{"base$i"} + 0)." 個".$TRE;
$disp.=$TBE;
$disp.="<hr width=500 noshade size=1>";

if($DT->{_seed}->{"base$i"}>=$tlimit)
	{$disp.='<BR>これ以上購入できません<BR>';}
elsif($DT->{money}<$price)
	{$disp.='<BR>資金が足りません<BR>';}
elsif(GetStockTime($DT->{time})<$usetime)
	{$disp.='<BR>時間が足りません<BR>';}
else
{
	$disp.="<FORM ACTION=\"action.cgi\" $METHOD>";
	$disp.="<INPUT TYPE=HIDDEN NAME=key VALUE=\"manor-s\">";
	$disp.="$USERPASSFORM";
	$disp.="<INPUT TYPE=HIDDEN NAME=bk VALUE=\"manor\">";
	$disp.="<INPUT TYPE=HIDDEN NAME=it VALUE=\"$i\">";
	$disp.="上記を ";
	$limit=$tlimit - $DT->{_seed}->{"base$i"};
	$money=$MAX_MONEY;
	$money=int($DT->{money}/$price) if $price;
	$msg{1}=1;
	$msg{10}=10;
	$msg{100}=100;
	$msg{1000}=1000;
	$msg{10000}=10000;
	$msg{$stock}="$stock(在庫最大)";
	$msg{$limit}="$limit(保有最大)";
	$msg{$money}="$money(資金最大)";
	$disp.="<SELECT NAME=num1 SIZE=1>";
	my $oldcnt=0;
	foreach my $cnt (sort { $a <=> $b } (1,10,50,$stock,$limit,$money))
	{
		last if $stock<$cnt || $DT->{money}<$cnt*$price || $cnt>$limit || $cnt==$oldcnt;
	
		$disp.="<OPTION VALUE=\"$cnt\">$msg{$cnt}";
		$oldcnt=$cnt;
	}
	$disp.="</SELECT> 個、もしくは ";
	$disp.="<INPUT TYPE=TEXT NAME=num2 SIZE=5> 個 ";

	$disp.="<INPUT TYPE=SUBMIT VALUE='買う'>";

	$disp.="<br>(消費時間:".GetTime2HMS($usetime).")";
	$disp.="</FORM>";
}

OutSkin();
1;
