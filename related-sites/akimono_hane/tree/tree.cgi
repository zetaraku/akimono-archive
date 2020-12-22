# 不思議な木 2005/09/28 seraphy
# 2008/10/26 改良

# 1人1回水を与えることができ、$TREE_WATER_CNT回水が与えられると成長モードに突入します。
# 成長モードに突入してから$TREE_GROW_TIME経過すると花が咲き、
# 全員の持ち時間が$TREE_PRESENT_TIME増加します。

# 設定

$TREE_USE_TIME=30*60;	#水を与える時の消費時間
$TREE_WATER_CNT=10;		#水を与える回数
$TREE_GROW_TIME=12*60*60;	#成長にかかる時間
$TREE_PRESENT_TIME=3*60*60;	#花が咲いた時に全員に与えられる時間
$TREE_GET_DT=0;		#花が咲いた時に・・・
				#0・・・アイテムを配布しない
				#1・・・全員にアイテムを配布する
				#2・・・水をあげたプレイヤーのみにアイテムを配布する
$TREE_GET_ITEM=1;		#花が咲いた時に配られるアイテムのナンバー
$TREE_GET_PROB=1000;		#花が咲いた時にアイテムがもらえる確率(プレイヤー毎)

Lock();
DataRead();
CheckUserPass();

$cnt=GetTownData('treecnt');
$tim=GetTownData('treetime');
SetTownData("treecnt",0) unless($cnt);
if($Q{mode} eq "water")
{
	OutError("もう水を与える必要はありません") if($tim);
	OutError("もう水を与えてあります") if($DT->{user}->{tree});
	OutError("時間が足りません") if(GetStockTime($DT->{time})<$TREE_USE_TIME);
	PushLog(0,0,"$DT->{name}が不思議な木に水を与えました");
	$cnt++;
	SetTownData("treecnt",$cnt);
	$DT->{time}+=$TREE_USE_TIME;
	$DT->{user}->{tree}=1;
}
if((!$tim)&&($cnt >= $TREE_WATER_CNT))
{
	PushLog(2,0,"不思議な木が成長を開始しました");
	SetTownData("treetime",$NOW_TIME);
}
if(($tim)&&($tim+$TREE_GROW_TIME <= $NOW_TIME))
{
	PushLog(2,0,"不思議な木が大きな花を咲かせました");
	$gtm=GetTime2HMS($TREE_PRESENT_TIME);
	foreach $DT(@DT)
	{
		PushLog(0,$DT->{id},"持ち時間が$gtm増加しました");
		$DT->{time}-=$TREE_PRESENT_TIME;
		if($TREE_GET_DT && $TREE_GET_ITEM && $TREE_GET_PROB)
		{
			if(($DT->{user}->{tree}) && ($TREE_GET_DT==2) && (rand(1000)<$TREE_GET_PROB))
			{
				$DT->{item}[$TREE_GET_ITEM-1]++;
				if($DT->{item}[$TREE_GET_ITEM-1]>$ITEM[$TREE_GET_ITEM]->{limit})
				{
					$DT->{item}[$TREE_GET_ITEM-1]=$ITEM[$TREE_GET_ITEM]->{limit};
				}
				else
				{
					PushLog(0,$DT->{id},$ITEM[$TREE_GET_ITEM]->{name}."を手に入れました");
				}
			}
			elsif(($TREE_GET_DT==1) && (rand(1000)<$TREE_GET_PROB))
			{
				$DT->{item}[$TREE_GET_ITEM-1]++;
				if($DT->{item}[$TREE_GET_ITEM-1]>$ITEM[$TREE_GET_ITEM]->{limit})
				{
					$DT->{item}[$TREE_GET_ITEM-1]=$ITEM[$TREE_GET_ITEM]->{limit};
				}
				else
				{
					PushLog(0,$DT->{id},$ITEM[$TREE_GET_ITEM]->{name}."を手に入れました");
				}
			}
		}
		$DT->{user}->{tree}="";
	}
	SetTownData("treecnt",0);
	SetTownData("treetime",0);
}

RequireFile('inc-html-ownerinfo.cgi');

$disp.="<BIG>●不思議な木</BIG><br><br>";
$disp.=$TB.$TR.$TD.GetTagImgKao("案内人","guide").$TD;
$disp.='これは街の不思議な木です。<br>';

if(($tim)&&($cnt>=$TREE_WATER_CNT))
{
	$rtm=GetTime2HMS($TREE_GROW_TIME-($NOW_TIME-$tim));
	$disp.="この木は現在成長中です。<br>";
	$disp.="開花まであと$rtmかかります。";
	$img=2;
}
elsif($DT->{user}->{tree})
{
	$disp.="水を与えていただいてありがとうございます。<br>";
	$disp.="きっと良いことが起こると思いますよ。";
}
else
{
	$disp.="水を与えると何か良いことがあるかもしれません。<br>";
	$disp.="あなたも水を与えてみませんか？";
}
$img=1 unless($img);
$disp.=qq|<td><IMG width="48" height="65" BORDER="0" SRC="$IMAGE_URL/tree$img.gif" alt="不思議な木"></td></tr></table><br>|;
$utm=GetTime2HMS($TREE_USE_TIME);
if((!$DT->{user}->{tree})&&($cnt<$TREE_WATER_CNT)&&(GetStockTime($DT->{time})>=$TREE_USE_TIME)&&(!$tim))
{
$disp.=<<"HTML";
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="tree">
<INPUT TYPE=HIDDEN NAME=mode VALUE="water">
$USERPASSFORM
<INPUT TYPE=SUBMIT VALUE="水を与える">（消費時間:$utm）</FORM>
HTML
}

RenewLog();
DataWrite();
DataCommitOrAbort();
UnLock();
OutSkin();
1;