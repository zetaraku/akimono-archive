# 兵士駐屯所 2005/01/06 由來

$image[0]=GetTagImgKao("案内人","army");
DataRead();
CheckUserPass();
ReadArmy();
RequireFile('inc-html-ownerinfo.cgi');

my $price=($DTevent{rebel}) ? 1500 : 1000;
my $level=DignityDefine($DT->{dignity},2);
$level=$DIGNITY[0] if !$level;

$disp.="<BIG>●傭兵所</BIG><br><br>";
$disp.=$TB.$TR.$TD.$image[0].$TD."<SPAN>案内人</SPAN>：ここにはドワーフ兵たちが雇い手を求めて集まっています。<br>";
$disp.="彼らを集めて反乱を起こすも，逆に領主を守るも，雇い主次第です。".$TRE.$TBE;

$disp.="<hr width=500 noshade size=1><BIG>●$DT->{shopname}の雇用状況</BIG><br><br>";
$disp.="$TB$TR$TDB爵位$TD$level <small>(経験値 ".($DT->{dignity}+0)."pt)$TRE";
$disp.="$TR$TDB雇用最大数$TD".(($DT->{dignity}+0)*1000)."人$TRE";
$disp.="$TR$TDB雇用費用$TD@".GetMoneyString($price)."$TRE";
$disp.="$TR$TDB雇用数$TD".($ARMY{$DT->{id}}+0)."人$TRE";
$disp.="$TR$TDB状態$TD".($RIOT{$DT->{id}} ? "<SPAN>反乱</SPAN>" : "待機").$TRE;
$disp.=$TBE;

ArmyBuy();
if ($ARMY{$DT->{id}})
	{
	ArmyFire();
	ArmyRebel() if !$DTevent{rebel};
	ArmyAction() if $DTevent{rebel} && !$RIOT{$DT->{id}};
	}
OutSkin();
1;


sub ArmyBuy
{
my $usetime=60*40;
my $limit= ($DT->{dignity}+0)*1000 - $ARMY{$DT->{id}};
$disp.="<hr width=500 noshade size=1>";
$disp.='<BIG>●兵士雇用</BIG>：兵士を雇うには爵位を上げる必要があります<BR>',return if $limit <= 0;
$disp.='<BIG>●兵士雇用</BIG>：資金が足りません<BR>',return if $DT->{money}<$price;
$disp.='<BIG>●兵士雇用</BIG>：時間が足りません<BR>',return if GetStockTime($DT->{time})<$usetime;

	$disp.=<<STR;
	<FORM ACTION="action.cgi" $METHOD>
	<INPUT TYPE=hidden NAME=key VALUE="army-s">
	$USERPASSFORM
	<INPUT TYPE=HIDDEN NAME=bk VALUE="army">
	<INPUT TYPE=hidden NAME=mode VALUE="plus">
	<BIG>●兵士雇用</BIG>： 兵士を 
	<SELECT NAME=cnt1>
	<OPTION VALUE="0" SELECTED>
STR
	$money=int($DT->{money}/$price);
	$msg{1000}=1000;
	$msg{5000}=5000;
	$msg{10000}=10000;
	$msg{20000}=20000;
	$msg{$limit}="$limit(雇用最大)";
	$msg{$money}="$money(資金最大)";
	my $oldcnt=0;
	foreach my $cnt (sort { $a <=> $b } (1000,5000,10000,20000,$limit,$money))
	{
		last if $cnt>$money || $cnt>$limit || $cnt==$oldcnt;
		$disp.="<OPTION VALUE=\"$cnt\">$msg{$cnt}";
		$oldcnt=$cnt;
	}
	$disp.=<<STR;
	</SELECT>
	 人、もしくは 
	<INPUT TYPE=TEXT SIZE=7 NAME=cnt2> 人
	<INPUT TYPE=SUBMIT VALUE="雇用する">
STR
	$disp.="(消費時間:".GetTime2HMS($usetime).")</FORM>";
}


sub ArmyFire
{
my $usetime=60*10;
my $stock=($ARMY{$DT->{id}}+0);
$disp.="<hr width=500 noshade size=1>";
$disp.='<BIG>●兵士解雇</BIG>：時間が足りません<BR>',return if GetStockTime($DT->{time})<$usetime;

	$disp.=<<STR;
	<FORM ACTION="action.cgi" $METHOD>
	<INPUT TYPE=hidden NAME=key VALUE="army-s">
	$USERPASSFORM
	<INPUT TYPE=HIDDEN NAME=bk VALUE="army">
	<INPUT TYPE=hidden NAME=mode VALUE="fire">
	<BIG>●兵士解雇</BIG>： 兵士を 
	<SELECT NAME=cnt1>
	<OPTION VALUE="0" SELECTED>
STR
	$msg{1000}=1000;
	$msg{5000}=5000;
	$msg{10000}=10000;
	$msg{20000}=20000;
	$msg{$stock}="$stock(兵士最大)";
	my $oldcnt=0;
	foreach my $cnt (sort { $a <=> $b } (1000,5000,10000,20000,$stock))
	{
		last if $stock<$cnt || $cnt==$oldcnt;
		$disp.="<OPTION VALUE=\"$cnt\">$msg{$cnt}";
		$oldcnt=$cnt;
	}
	$disp.=<<STR;
	</SELECT>
	 人、もしくは 
	<INPUT TYPE=TEXT SIZE=7 NAME=cnt2> 人
	<INPUT TYPE=SUBMIT VALUE="解雇する">
STR
	$disp.="(消費時間:".GetTime2HMS($usetime).")</FORM>";
}


sub ArmyRebel
{
return if ($STATE->{leader}==$DT->{id});
my $usetime=60*30;
$disp.="<hr width=500 noshade size=1>";
$disp.='<BIG>●武装蜂起</BIG>：反乱に必要な兵士数が足りません。<BR>',return if ($ARMY{$DT->{id}} < 2500);
$disp.='<BIG>●武装蜂起</BIG>：時間が足りません<BR>',return if GetStockTime($DT->{time})<$usetime;

	$disp.=<<STR;
	<FORM ACTION="action.cgi" $METHOD>
	<INPUT TYPE=hidden NAME=key VALUE="army-s">
	$USERPASSFORM
	<INPUT TYPE=HIDDEN NAME=bk VALUE="army">
	<INPUT TYPE=hidden NAME=mode VALUE="rebelon">
	<BIG>●武装蜂起</BIG>： 
	<INPUT TYPE=TEXT NAME=cmd SIZE=10 VALUE="">
	(rebel と入力)
	反乱を <INPUT TYPE=SUBMIT VALUE="開始する">
STR
	$disp.="(消費時間:".GetTime2HMS($usetime).")</FORM>";
}


sub ArmyAction
{
my $usetime=60*20;
$disp.="<hr width=500 noshade size=1>";
$disp.='<BIG>●反乱加勢</BIG>：時間が足りません<BR>',return if GetStockTime($DT->{time})<$usetime;

	$disp.=<<STR;
	<FORM ACTION="action.cgi" $METHOD>
	<INPUT TYPE=hidden NAME=key VALUE="army-s">
	$USERPASSFORM
	<INPUT TYPE=HIDDEN NAME=bk VALUE="army">
	<INPUT TYPE=hidden NAME=mode VALUE="rside">
	<BIG>●反乱加勢</BIG>： 
	<INPUT TYPE=TEXT NAME=cmd SIZE=10 VALUE="">
	(rebel と入力)
	反乱に <INPUT TYPE=SUBMIT VALUE="呼応する">
STR
	$disp.="(消費時間:".GetTime2HMS($usetime).")</FORM>";

$usetime=60*20;
$disp.="<hr width=500 noshade size=1>";
$disp.='<BIG>●護衛協力</BIG>：時間が足りません<BR>',return if GetStockTime($DT->{time})<$usetime;

	$disp.=<<STR;
	<FORM ACTION="action.cgi" $METHOD>
	<INPUT TYPE=hidden NAME=key VALUE="army-s">
	$USERPASSFORM
	<INPUT TYPE=HIDDEN NAME=bk VALUE="army">
	<INPUT TYPE=hidden NAME=mode VALUE="lside">
	<BIG>●護衛協力</BIG>： 
	兵士を領主の護衛軍に <INPUT TYPE=SUBMIT VALUE="派遣する">
STR
	$disp.="(消費時間:".GetTime2HMS($usetime).")</FORM>";
}
