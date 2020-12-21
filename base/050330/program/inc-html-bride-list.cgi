# 住宅操作 2005/01/06 由來

$i=SearchBride($Q{no});
OutError('指定された情報は存在しません') if ($i==-1);
($ida,$idb)=($BRIDE[$i]->{ida},$BRIDE[$i]->{idb});

if (!$BRIDE[$i]->{mode})
{
Agree();
}
elsif ($Q{d})
{
DivCheck();
}
else
{
House();
}
1;

sub Agree
{
if ($idb == $DT->{id}) {
	# プロポーズ承諾
	$disp.=<<STR;
$TB$TR$TD
$image[3]
神父：プロポーズを受けますか？ それなら次の注意をよく聴いてください。<br>
・結婚資金が<b>500万$term[2]</b>かかります。<br>
・事前によく話し合いなさい。その人と助け合っていけるかよく考えなさい。<br>
・プロポーズをした側が夫となり，受けた側が妻になります。
$TRE$TBE
<form action="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="agree">
<INPUT TYPE=HIDDEN NAME=idx VALUE="$BRIDE[$i]->{no}">
<BIG>●プロポーズを受ける</BIG>：私 $DT->{name} ($DT->{shopname})は
$DT[$id2idx{$ida}]->{name} ($DT[$id2idx{$ida}]->{shopname})を夫とし<br>
健やかなる時も病める時もその身を共にする事を
<INPUT TYPE=SUBMIT VALUE='誓います'>
</FORM>
<hr width=500 noshade size=1>
<form action="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="dis">
<INPUT TYPE=HIDDEN NAME=idx VALUE="$BRIDE[$i]->{no}">
<BIG>●プロポーズを断る</BIG>：そんなこと言われても困るので
<INPUT TYPE=SUBMIT VALUE='ごめんなさい'>
</FORM>
STR
}
elsif ($ida == $DT->{id}) {
	# プロポーズ撤回
	$disp.=<<STR;
$TB$TR$TD
$image[3]
神父：プロポーズを取りやめるつもりですか。<br>
少し恥ずかしいかもしれませんが仕方ありませんね。
$TRE$TBE
<form action="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="end">
<INPUT TYPE=HIDDEN NAME=idx VALUE="$BRIDE[$i]->{no}">
<BIG>●プロポーズを取りやめる</BIG>：やはりまだ愛が足らなかったので
<INPUT TYPE=SUBMIT VALUE='取りやめます'>
</FORM>
STR
}
else {
	# 野次馬
	$disp.=<<STR;
$TB$TR$TD
$image[3]
神父：<b>$DT[$id2idx{$ida}]->{name}</b>さんの
<b>$DT[$id2idx{$idb}]->{name}</b>さんへ想いは真剣です。たぶん。<br>
今は二人をあたたかく見守ってあげてください。
$TRE$TBE
STR
}
}

sub House
{
$disp.=($BRIDE[$i]->{mode}==1)?$image[0]:$image[1];
$btitle=($BRIDE[$i]->{mode}==1)?"教会 > 共用倉庫":"住宅";
	# 無関係な人
	if ($DT->{id} != $ida && $DT->{id} != $idb) {
	$disp.=<<STR;
：<BIG>$DT[$id2idx{$ida}]->{shopname} ＆ $DT[$id2idx{$idb}]->{shopname}</BIG><br><br>
$TB$TR$TD
結婚すると，マイホームとして二人の共用倉庫がもらえます。<br>
資金や商品を置くことができ，維持費もかかりません。
$TRE$TBE
STR
	return;
	}
	my $moneymes=GetMoneyString($BRIDE[$i]->{money});
	my $moneymax=GetMoneyString($BRIDE[$i]->{mode}*20000000);
	$disp.=<<STR;
：<BIG>$DT[$id2idx{$ida}]->{shopname} ＆ $DT[$id2idx{$idb}]->{shopname}</BIG><br><br>
$TB$TR
$TDB備品
$TDB数量<small>/最大</small>
$TRE
$TR$TD資金
$TD$moneymes<small>/$moneymax</small>
$TRE
STR

$formstock="<OPTION VALUE=\"-1\">資金(".GetMoneyString($BRIDE[$i]->{money}).")";
foreach (0..$BRIDE[$i]->{mode}-1) {
	my $stock=$BRIDE[$i]->{stock}[$_];
	my $cnt=$BRIDE[$i]->{cnt}[$_];
	$disp.='<tr><td>';
	$disp.=GetTagImgItemType($stock).$ITEM[$stock]->{name}.'<td>';
	$disp.=($cnt) ? ($cnt.'<small>/'.($ITEM[$stock]->{limit}*$HouseMax).$ITEM[$stock]->{scale}) : ' ';
	$formstock.="<OPTION VALUE=\"$_\">$ITEM[$stock]->{name}($cnt$ITEM[$stock]->{scale})" if ($cnt);
	}
$disp.=$TRE.$TBE."<hr width=500 noshade size=1>";

	my @sort;
	foreach(1..$MAX_ITEM){$sort[$_]=$ITEM[$_]->{sort}};
	my @itemlist=sort { $sort[$a] <=> $sort[$b] } (1..$MAX_ITEM);
	$formitem="<OPTION VALUE=\"-1\">資金(".GetMoneyString($DT->{money}).")";
	foreach(@itemlist)
	{
		my $cnt=$DT->{item}[$_-1];
		$cnt=0 if ($ITEM[$_]->{flag}=~/r/);	# 依頼できないアイテムは置けない。
		my $scale=$ITEM[$_]->{scale};
		$formitem.="<OPTION VALUE=\"$_\">$ITEM[$_]->{name}($cnt$scale)" if $cnt;
	}

$disp.=<<STR;
<form action="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=id VALUE="$DT->{id}">
<INPUT TYPE=HIDDEN NAME=idx VALUE="$BRIDE[$i]->{no}">
<INPUT TYPE=HIDDEN NAME=no VALUE="$BRIDE[$i]->{no}">
<INPUT TYPE=HIDDEN NAME=mode VALUE="plus">
<BIG>●保管</BIG>：住宅に <SELECT NAME=it SIZE=1>
$formitem
</SELECT> を数量 <INPUT TYPE=TEXT NAME=num SIZE=5> (無記入で最大)
 <INPUT TYPE=SUBMIT VALUE='保管する'>
</FORM>
<hr width=500 noshade size=1>
<form action="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=id VALUE="$DT->{id}">
<INPUT TYPE=HIDDEN NAME=idx VALUE="$BRIDE[$i]->{no}">
<INPUT TYPE=HIDDEN NAME=no VALUE="$BRIDE[$i]->{no}">
<INPUT TYPE=HIDDEN NAME=mode VALUE="minus">
<BIG>●取出</BIG>：住宅から <SELECT NAME=it SIZE=1>
$formstock
</SELECT> を数量 <INPUT TYPE=TEXT NAME=num SIZE=5> (無記入で最大)
 <INPUT TYPE=SUBMIT VALUE='取り出す'>
</FORM>
STR

Reform() if ($BRIDE[$i]->{mode} > 2 && $BRIDE[$i]->{mode} < 7);

$disp.=<<STR;
<hr width=500 noshade size=1>
<form action="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=id VALUE="$DT->{id}">
<INPUT TYPE=HIDDEN NAME=no VALUE="$BRIDE[$i]->{no}">
<INPUT TYPE=HIDDEN NAME=d VALUE="1">
<SPAN>離婚</SPAN>：
<INPUT TYPE=SUBMIT VALUE='離婚する'>
(備品は全て破棄)
</FORM>
STR
}

sub Reform
{
if ($BRIDE[$i]->{money} > $BRIDE[$i]->{mode} * 10000000)
	{
$disp.=<<STR;
<hr width=500 noshade size=1>
<form action="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=id VALUE="$DT->{id}">
<INPUT TYPE=HIDDEN NAME=idx VALUE="$BRIDE[$i]->{no}">
<INPUT TYPE=HIDDEN NAME=no VALUE="$BRIDE[$i]->{no}">
<INPUT TYPE=HIDDEN NAME=mode VALUE="more">
<BIG>●増築</BIG>：
<INPUT TYPE=SUBMIT VALUE='増築する'>
STR
$disp.="(費用".GetMoneyString($BRIDE[$i]->{mode} * 10000000).")</form>";
	}
	else
	{
$disp.=<<STR;
<hr width=500 noshade size=1>
<BIG>●増築</BIG>：資金が足りません
STR
	}
}

sub DivCheck
{
	# 離婚確認
	$disp.=<<STR;
$TB$TR$TD
$image[3]
神父：本当に離婚するのですね？
$TRE$TBE
<form action="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=id VALUE="$DT->{id}">
<INPUT TYPE=HIDDEN NAME=idx VALUE="$BRIDE[$i]->{no}">
<INPUT TYPE=HIDDEN NAME=mode VALUE="divorce">
<SPAN>●離婚</SPAN>：
<INPUT TYPE=SUBMIT VALUE='離婚する'>
(備品は全て破棄)
</FORM>
STR
}
