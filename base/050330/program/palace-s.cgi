# 宮殿達成処理 2004/01/20 由來

Lock();
RequireFile("inc-palace.cgi");
$image[0]=GetTagImgKao("王様","king",'align="left" ');
$image[1]=GetTagImgKao("大臣","minister",'align="left" ');

DataRead();
CheckUserPass();

$evt=GetTownData('evt');
$evt=0 if (!$evt);
$level=DignityDefine($DT->{dignity});

$disp.="<BIG>●宮殿</BIG><br><br>";

$shopname=$DT->{shopname};
$name=$DT->{name};
$need=$itemno[$evt];

if ( $DT->{item}[$need-1] < $count[$evt] )
	{
	$disp.='<TABLE cellpadding="26" width="570"><tr>';
	$disp.=qq|<TD style="background-repeat : repeat-x;background-image : url($IMAGE_URL/palace.png);" valign="top"><br><br>|;
	$disp.=$image[0].'おぉ何ということだ<b>'.$shopname.'</b>の<b>'.$name.$level.'</b>よ。<br>';
	$disp.='<b>'.GetTagImgItemType($need).$ITEM[$need]->{name}.$count[$evt].$ITEM[$need]->{scale}.'</b>は，いまだ揃っていないではないか！<br>';
	$disp.='それとも'.$name.'は余をからかっているのではあるまいな？';
	$disp.='<br>はやく使命を達成するのじゃ。ゆめゆめ忘れるでないぞ。'.$TRE;
	$disp.=$TBE."<br>王様はぷりぷり怒り出してしまいました。";
	}
	else
	{
	$disp.='<TABLE cellpadding="26" width="570"><tr>';
	$disp.=qq|<TD style="background-repeat : repeat-x;background-image : url($IMAGE_URL/palace.png);" valign="top"><br><br>|;
	$disp.=$image[0].'あっぱれじゃ<b>'.$shopname.'</b>の<b>'.$name.$level.'</b>よ。<br>';
	$disp.='<b>'.GetTagImgItemType($need).$ITEM[$need]->{name}.$count[$evt].$ITEM[$need]->{scale}.'</b>は確かに受け取ったぞ。<br>';
	$disp.='よってそなたに褒美として'.DignityDefine(1,1).'<b>爵位経験値</b>を与えよう。'.$TRE;
	$disp.=$TBE."<br>";

	$DT->{item}[$need-1] -= $count[$evt];
	$DT->{dignity}++;
	$evt=int(rand(scalar(@itemno)));
	SetTownData('evt',$evt);

	PushLog(0,0,$DT->{shopname}.'が王様の使命を達成しました。');
	RenewLog();
	DataWrite();
	DataCommitOrAbort();
	}
UnLock();
OutSkin();
1;
