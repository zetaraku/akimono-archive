# 宮殿 2004/01/20 由來

RequireFile("inc-palace.cgi");	#設定ファイル読み込み

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

if ($DT->{point} <  $deny_point )
	{
	$disp.='<TABLE cellpadding="26" width="570"><tr>';
	$disp.=qq|<TD style="background-repeat : repeat-x;background-image : url($IMAGE_URL/palace.png);" valign="top"><br><br>|;
	$disp.=$image[1].'おや宮殿に御用ですか？<b>'.$shopname.'</b>の<b>'.$name.'</b>さん。<br>';
	$disp.='しかし国王陛下は'.$name.'さんとは面会できないとの仰せでございます。';
	$disp.='<br>もう少し経営の手腕を高めてから来てみてはどうでしょう。'.$TRE;
	$disp.=$TBE."<br>";
	}
	else
	{
	KingMain();
	}

OutSkin();
1;


sub KingMain
{
$disp.='<TABLE cellpadding="26" width="570"><tr>';
$disp.=qq|<TD style="background-repeat : repeat-x;background-image : url($IMAGE_URL/palace.png);" valign="top"><br><br>|;
$disp.=$image[0].'よくぞ参った<b>'.$shopname.'</b>の<b>'.$name.$level.'</b>よ。<br>';
$disp.='活躍はかねがね聞き及んでおるぞ。そこでじゃ，そなたを見込んで使命を与える。<br><br>';
$disp.=$msg[$evt].'<br>されば<b>'.GetTagImgItemType($need).$ITEM[$need]->{name}.'を'.$count[$evt].$ITEM[$need]->{scale}.'</b>求めて参れ。';
$disp.='<br>この使命を見事果たせたならばそなたに'.DignityDefine(1,1).'<b>爵位経験値</b>を与える。やってくれるな？'.$TRE;
$disp.=$TBE;

$disp.=<<"HTML";
<br><FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="palace-s">
$USERPASSFORM
<BIG>●使命達成</BIG>： 王様が依頼する商品を
<INPUT TYPE=SUBMIT VALUE="渡す"></FORM>
HTML
}