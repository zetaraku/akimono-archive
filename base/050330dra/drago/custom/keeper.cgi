# ペット預かり所 2003/12/28 由來

Lock() if ($Q{mode});	# できるだけ早くロック。
DataRead();
CheckUserPass();

my $image=GetTagImgKao("飼育係","keeper",'align="left" ');
my @STOCK;
ReadDTSub($DT,"keeper");
$stock[0]=$DT->{_keeper}->{0};
$stock[1]=$DT->{_keeper}->{1};
$stock[2]=$DT->{_keeper}->{2};
EditKeeper() if ($Q{mode});	# 各種データ処理

$disp.="<BIG>●ペット預かり所</BIG><br><br>";
	$disp.='<TABLE cellpadding="26" width="500"><tr>';
	$disp.=qq|<TD style="background-repeat : repeat-x;background-image : url($IMAGE_URL/keeper.png);" valign="top"><br><br>|;
	$disp.=$image.'<SPAN>飼育係</SPAN>：ここでは，３種類までのペットをお預かりできます。<br>';
	$disp.='ただし，お預かりできるのは，それぞれ１匹ずつだけです。<br>';
	$disp.='お返しする際に，代金を \50,000 いただきます。'.$TRE;
	$disp.=$TBE."<br>";

$disp.=<<STR;
$TB$TR
<TD class=b NOWRAP colspan=3>預かり帳
$TRE$TR
STR

my $formstock;
my $formitem;
foreach (0..2) {
	$disp.=$TD."(".($_ + 1).")";
	$disp.="なし",next if !$stock[$_];
	$disp.=GetTagImgItemType($stock[$_]).$ITEM[$stock[$_]]->{name};
	$formstock.="<OPTION VALUE=\"$_\">$ITEM[$stock[$_]]->{name}";
	}
$disp.=$TRE.$TBE."<hr width=500 noshade size=1>";

	my @sort;
	foreach(1..$MAX_ITEM){$sort[$_]=$ITEM[$_]->{sort}};
	my @itemlist=sort { $sort[$a] <=> $sort[$b] } (1..$MAX_ITEM);
	foreach(@itemlist)
	{
		next if !$DT->{item}[$_-1];
		next if $ITEM[$_]->{type} < 3;
		next if $ITEM[$_]->{type} > 8;
		$formitem.="<OPTION VALUE=\"$_\">$ITEM[$_]->{name}";
	}

$disp.=<<STR;
<form action="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=id VALUE="$DT->{id}">
<INPUT TYPE=HIDDEN NAME=idx VALUE="$BRIDE[$i]->{no}">
<INPUT TYPE=HIDDEN NAME=no VALUE="$BRIDE[$i]->{no}">
<INPUT TYPE=HIDDEN NAME=mode VALUE="plus">
<BIG>●寄託</BIG>：預かり所に <SELECT NAME=it SIZE=1>
$formitem
</SELECT> を
 <INPUT TYPE=SUBMIT VALUE='預ける'>
</FORM>
<hr width=500 noshade size=1>
<form action="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=id VALUE="$DT->{id}">
<INPUT TYPE=HIDDEN NAME=idx VALUE="$BRIDE[$i]->{no}">
<INPUT TYPE=HIDDEN NAME=no VALUE="$BRIDE[$i]->{no}">
<INPUT TYPE=HIDDEN NAME=mode VALUE="minus">
<BIG>●受取</BIG>：預かり所から <SELECT NAME=it SIZE=1>
$formstock
</SELECT> を
 <INPUT TYPE=SUBMIT VALUE='受け取る'>
</FORM>
STR

OutSkin();
1;


sub EditKeeper
{
if ($Q{mode} eq 'plus') {
	$itemno=$Q{it};
	my $n=SearchKstock($Q{it});
	OutError('保管スペースがありません。') if ($n == -1) ;
	OutError('指定されたペットはいません。') if ($DT->{item}[$itemno-1] < 1);
	$DT->{item}[$itemno-1]-=1;
	$DT->{_keeper}->{$n}=$itemno;
	$stock[$n]=$itemno;
}
if ($Q{mode} eq 'minus') {
	my $n=$Q{it};
	my $itemno=$stock[$n];
	OutError('指定されたペットはいません。') if (!$itemno);
	OutError('倉庫が一杯で取り出せません。') if ($ITEM[$itemno]->{limit} <= $DT->{item}[$itemno-1]);
	OutError('返却資金を持っていません。') if ($DT->{money} < 50000);
	$DT->{money}-=50000;
	$DT->{item}[$itemno-1]+=1;
	delete($DT->{_keeper}->{$n});
	$stock[$n]=0;
}
WriteDTSub($DT,"keeper");
DataWrite();
DataCommitOrAbort();
UnLock();
}

sub SearchKstock
{
	my($no)=@_;
	foreach(0..2)
	{
		return -1 if($no == $stock[$_]);	# まずすでに保管されている物と同じか調べる
	}
	foreach(0..2)
	{
		return $_ if !($stock[$_]);	# 次に空きがあるか調べる
	}
	return -1;
}



