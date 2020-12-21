# フォーム表示 2005/03/30 由來

$disp.=GetMenuTag('dwarf','[宅配便リスト]')
	."<b>[宅配便を出す]</b>";
$disp.=GetMenuTag('dwarf','[貿易品リスト]','&trade=list') if -e "trade.cgi";
$disp.="<hr width=500 noshade size=1>";

my $cnt=$MAX_BOX - scalar(@SENDWF);
if ($cnt > 0)
{
$preerror="";
LFormCheck() if ($Q{form} eq 'check');
NewLform() if ($preerror || $Q{form} eq 'make');
}
else
{
$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>住み込みドワーフ</SPAN>：これ以上の宅配便を出すことはできんぞい。<br>
不必要な宅配便を解除するなりしてくれい。
$TRE$TBE
HTML
}
1;

sub NewLform
{
FormSet();
$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>住み込みドワーフ</SPAN>：あと $cnt包まで宅配便を出せるぞい。<br>
もらう相手にとって失礼にならぬようにな。
$TRE$TBE<br>$preerror
<FORM ACTION="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
$TB
$TR$TDB<b>宛先</b>
HTML

$disp.=$TD."<SELECT NAME=to><OPTION VALUE=\"-1\">－－宛先選択－－";
$disp.="<OPTION VALUE=\"99\">◇他の街へ輸出◇" if -e "trade.cgi";
	foreach (@DT)
	{
		$disp.="<OPTION VALUE=\"$_->{id}\"".($Q{to}==$_->{id} ? ' SELECTED' : '').">$_->{shopname}";
	}
$disp.="</SELECT>\n";
$disp.="<INPUT TYPE=CHECKBOX NAME=notice".(($preerror&&!$Q{notice}) ? '' : ' checked').">";

$disp.=<<"HTML";
郵便で知らせる$TRE
$TR$TDB<b>商品</b>
$TD<SELECT NAME=item SIZE=1>
$formitem
</SELECT> を <INPUT TYPE=TEXT NAME=num SIZE=7 VALUE="$Q{num}"> 個$TRE
$TR$TDB<b>代金</b>
$TD<INPUT TYPE=TEXT NAME=price SIZE=12 VALUE="$Q{price}"> $term[2](
<INPUT TYPE=CHECKBOX NAME=unit>単価指定)
$TR$TD<SPAN>使用法</SPAN>$TD
・商品を相手に送り，その代金をとることができます。<br>
・宅配便を送ったことを自動的に「郵便で知らせる」ことができます。<br>
・手数料として代金の <b>$DTTaxrate%</b>の税金がかかります。
$TBE
<br><INPUT TYPE=HIDDEN NAME=form VALUE="check">
<INPUT TYPE=SUBMIT VALUE="送信確認">
</FORM>
HTML
}

sub LFormCheck
{
my $to=$Q{to};
my $toname;
$preerror="宛先を指定してください。", return if $to==-1;
OutError("自分自身に宅配便を出すことはできません。") if ($to == $DT->{id});
if ($to==99)
	{
	$preerror="貿易がつながっていないので指定できません。", return unless -e "trade.cgi";
	$toname="他の街へ輸出";
	$Q{notice}=0;
	}
	else
	{
	$preerror="存在しない店舗です。", return if !defined($id2idx{$to});
	$toname=$DT[$id2idx{$to}]->{shopname};
	}
$preerror="アイテムの指定が不正です。", return if !$ITEM[$Q{item}]->{name};
$preerror="アイテムの指定が不正です。", return if $ITEM[$Q{item}]->{flag}=~/r/;	# r 依頼不可

$Q{num}||=$DT->{item}[$Q{item}-1];
$Q{num}=CheckCount($Q{num},0,0,$DT->{item}[$Q{item}-1]);
$preerror="アイテムの在庫がありません。", return if !$Q{num};
my $price=CheckCount($Q{price},0,0,$MAX_MONEY);
$price=$price * $Q{num} if $Q{unit};
$preerror="代金を指定してください。", return if !$price;
my $numrate=$ITEM[$Q{item}]->{price} * $Q{num};
$preerror="商品の価値と代金がつりあっていません。", return if ($price > $numrate * 2) || ($numrate > $price * 2);
my $pricestring=GetMoneyString($price);

$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>住み込みドワーフ</SPAN>：この内容で宅配便を出すぞい。<br>
これで問題ないか確認してくれい。
$TRE$TBE<br>
$TB$TR$TD
<SPAN>宛先</SPAN>：$toname<br>
<SPAN>商品</SPAN>：$ITEM[$Q{item}]->{name} × $Q{num} $ITEM[$Q{item}]->{scale}<br>
<SPAN>代金</SPAN>：$pricestring
$TRE$TBE
<FORM ACTION="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=to VALUE="$to">
<INPUT TYPE=HIDDEN NAME=notice VALUE="$Q{notice}">
<INPUT TYPE=HIDDEN NAME=item VALUE="$Q{item}">
<INPUT TYPE=HIDDEN NAME=num VALUE="$Q{num}">
<INPUT TYPE=HIDDEN NAME=price VALUE="$Q{price}">
<INPUT TYPE=HIDDEN NAME=unit VALUE="$Q{unit}">
<INPUT TYPE=HIDDEN NAME=form VALUE="make">
<INPUT TYPE=SUBMIT NAME=ok VALUE="送信">
<INPUT TYPE=SUBMIT NAME=ng VALUE="再編集">
</FORM>
HTML
}

sub FormSet
{
	my @sort;
	foreach(1..$MAX_ITEM){$sort[$_]=$ITEM[$_]->{sort}};
	my @itemlist=sort { $sort[$a] <=> $sort[$b] } (1..$MAX_ITEM);
	$formitem="";
	foreach my $idx (@itemlist)
	{
		next if !$ITEM[$idx]->{name};
		next if $ITEM[$idx]->{flag}=~/r/;	# r 依頼不可
		my $cnt=$DT->{item}[$idx-1];
		my $scale=$ITEM[$idx]->{scale};
		my $price=$ITEM[$idx]->{price};
		$formitem.="<OPTION VALUE=\"$idx\"".($Q{item}==$idx ? ' SELECTED' : '').">$ITEM[$idx]->{name}($cnt$scale@".GetMoneyString($price).")" if $cnt;
	}
}


