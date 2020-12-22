# 陳列棚処理 2005/01/06 由來

$NOMENU=1;
$Q{er}=(($Q{bk} eq "sc")?'main':'stock');
OutError('不正な呼び出しです') if $Q{no}eq'';

Lock();
DataRead();
CheckUserPass();

$no=int($Q{no});
$itemno=int($Q{item});
$per=CheckCount($Q{per},0,1,200);
$prc=CheckCount($Q{prc},0,0,$MAX_MONEY);
$price=0;

UseTime($TIME_EDIT_SHOWCASE);

if($no<0 || $no>=$DT->{showcasecount}
|| $itemno<0 || $itemno>$MAX_ITEM
|| ($per<=0 && $prc<=0)
|| $per>200
|| $ITEM[$itemno]->{flag}=~/s/
)
{
	OutError('不正な要求です');
}

$price=0;
if($itemno>0)
{
	OutError('そのアイテムは在庫無しです') if !$DT->{item}[$itemno-1];
	$price=$prc!=0 ? $prc : int($ITEM[$itemno]->{price} / 100 * $per);
}
$price=$MAX_MONEY if $price>$MAX_MONEY;

if($itemno && $price)
{
	$ret="棚".($no+1)."に$ITEM[$itemno]->{name}を".GetMoneyString($price)."で陳列しました。";
	PushLog(0,$DT->{id},$ret);
}
else
{
	$itemno=0;
	$price=0;
	$ret="棚".($no+1)."への陳列をやめました。";
	PushLog(0,$DT->{id},$ret);
}

$DT->{showcase}[$no]=$itemno;
$DT->{price}[$no]=$price;

RenewLog();
DataWrite();
DataCommitOrAbort();
UnLock();

$disp.=$TBT.$TRT.$TD.GetTagImgJob($DT->{job},$DT->{icon});
$disp.=$TD.GetMenuTag('stock',	'[倉庫へ行く]');
$disp.=GetMenuTag('main','[店内に戻る]');
$disp.=$TRE.$TBE;
$disp.="<br>".$ret;

OutSkin();
1;
