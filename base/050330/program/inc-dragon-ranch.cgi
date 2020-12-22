# ドラゴンレース 牧場メニュー表示 2005/03/30 由來

ReadRanch();
$disp.="<BIG>●ドラゴンレース：牧場</BIG><br><br>";

if ($MYRC==-1)
{
$disp.="$TB$TR$TD".GetTagImgKao("ドラゴン老師","slime1").$TD;
$disp.="<SPAN>ドラゴン老師</SPAN>：自分の牧場を持っていないようじゃな。<br>";
$disp.="牧場を持てば，自分のドラゴンを育てることができる。".$TRE.$TBE;
my $estmsg=GetMoneyString($RCest);
$disp.=<<STR;
<br>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="slime-s">
<INPUT TYPE=HIDDEN NAME=bk VALUE="slime">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="rcedit">
<INPUT TYPE=HIDDEN NAME=code VALUE="new">
<BIG>●牧場設立</BIG>： <INPUT TYPE=TEXT NAME=name SIZE=20> と名付けて 
<INPUT TYPE=SUBMIT VALUE='設立'>
</FORM>
<br>
$TB$TR$TD
・牧場を設立するには，資金<b>$estmsg</b>がかかります。<br>
・ドラゴンの育成には別途さらに資金がかかるので，余裕があるか考えてください。<br>
$TBE
STR
}
else
{
$disp.="$TB$TR$TDB名称$TDB創立$TDB平均賞金$TDB総賞金$TDB成績$TRE";
$disp.=$TR;
$disp.=$TD.$RC[$MYRC]->{name};
$disp.=$TD.GetTime2found($NOW_TIME-$RC[$MYRC]->{birth});
$disp.=$TD.($RC[$MYRC]->{aprize} + 0)."万";
$disp.=$TD.($RC[$MYRC]->{prize} + 0)."万";
$disp.=$TD.($RC[$MYRC]->{g1win} + 0)." - ".($RC[$MYRC]->{g2win} + 0)." - ".($RC[$MYRC]->{g3win} + 0)." - ".($RC[$MYRC]->{sdwin} + 0);
$disp.=$TRE.$TBE;
$disp.="<br><BIG>●所有競争竜</BIG><br><br>";
ReadDragon();
if (!scalar @MYDR)
	{
	$disp.="所有の競争竜はありません<br><br>";
	}
	else
	{
$disp.="$TB$TR$TDB名称$TDB年齢$TDB性別$TDBスピ$TDB勝負$TDB瞬発$TDBパワ$TDB体調$TDB体重$TDB距離適性$TDB総賞金$TDB成績$TRE";
	foreach (@MYDR)
		{
$disp.=$TR;
$disp.=$TD."<a href=\"action.cgi?key=slime&mode=detail&dr=$DR[$_]->{no}&$USERPASSURL\">"
	.GetTagImgDra($DR[$_]->{fm},$DR[$_]->{color}).$DR[$_]->{name}."</a>";
$disp.=$TD.GetTime2found($NOW_TIME-$DR[$_]->{birth});
$disp.=$TD.$FM[$DR[$_]->{fm}];
$disp.=$TD.$VALUE[int($DR[$_]->{sp} /100*6)];
$disp.=$TD.$VALUE[int($DR[$_]->{sr} /100*6)];
$disp.=$TD.$VALUE[int($DR[$_]->{ag} /100*6)];
$disp.=$TD.$VALUE[int($DR[$_]->{pw} /100*6)];
$disp.=$TD.$EVALUE[int($DR[$_]->{con} /100*4)];
$disp.=$TD.$DR[$_]->{wt};
$disp.=$TD.GetRaceApt($DR[$_]->{apt},$DR[$_]->{fl});
$disp.=$TD.($DR[$_]->{prize} + 0)."万";
$disp.=$TD.($DR[$_]->{g1win} + 0)." - ".($DR[$_]->{g2win} + 0)." - ".($DR[$_]->{g3win} + 0)." - ".($DR[$_]->{sdwin} + 0);
$disp.=$TRE;
		}
$disp.=$TBE."<br>";
	}

ReadParent();

if (scalar @MYPR)
	{
	$disp.="<BIG>●所有繁殖".$FM[1]."竜</BIG><br><br>";
$disp.="$TB$TR$TDB名称$TDB年齢$TDB遺伝$TDBスピ$TDB勝負$TDB瞬発$TDBパワ$TDB健康$TDB柔軟$TDB距離適性$TDB現役賞金$TDB現役成績$TRE";
	foreach (@MYPR)
		{
$disp.=$TR;
$disp.=$TD."<a href=\"action.cgi?key=slime&mode=pr&dr=$PR[$_]->{no}&$USERPASSURL\">"
	.GetTagImgDra($PR[$_]->{fm},$PR[$_]->{color},1).$PR[$_]->{name}."</a>";
$disp.=$TD.GetTime2found($NOW_TIME-$PR[$_]->{birth});
$disp.=$TD.$VALUE[int($PR[$_]->{hr} /100*6)];
$disp.=$TD.$VALUE[int($PR[$_]->{sp} /100*6)];
$disp.=$TD.$VALUE[int($PR[$_]->{sr} /100*6)];
$disp.=$TD.$VALUE[int($PR[$_]->{ag} /100*6)];
$disp.=$TD.$VALUE[int($PR[$_]->{pw} /100*6)];
$disp.=$TD.$VALUE[int($PR[$_]->{hl} /100*6)];
$disp.=$TD.$VALUE[int($PR[$_]->{fl} /100*6)];
$disp.=$TD.GetRaceApt($PR[$_]->{apt},$PR[$_]->{fl});
$disp.=$TD.($PR[$_]->{prize} + 0)."万";
$disp.=$TD.($PR[$_]->{g1win} + 0)." - ".($PR[$_]->{g2win} + 0)." - ".($PR[$_]->{g3win} + 0)." - ".($PR[$_]->{sdwin} + 0);
$disp.=$TRE;
		}
$disp.=$TBE."<br>";
	}



if (scalar @MYDR < $MYDRmax)
	{
my @dist=('短距離竜','中距離竜','長距離竜');
my $formdist="";
foreach(0..$#dist) {$formdist.=qq|<OPTION VALUE="$_">$dist[$_]|; }
my $buymsg=GetMoneyString($DRbuy);
$disp.=<<STR;
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="slime-s">
<INPUT TYPE=HIDDEN NAME=bk VALUE="slime">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="dredit">
<INPUT TYPE=HIDDEN NAME=code VALUE="new">
<BIG>●ドラゴン購入</BIG>： <SELECT NAME=fm SIZE=1>
<OPTION VALUE="0">$FM[0]<OPTION VALUE="1">$FM[1]
</SELECT> の <SELECT NAME=dist SIZE=1>
$formdist
</SELECT> を 
<INPUT TYPE=TEXT NAME=name SIZE=20> と名付けて 
<INPUT TYPE=SUBMIT VALUE='購入'>
</FORM>
<br>
$TB$TR$TD
・競争竜は，<b>$MYDRmax</b>頭まで持つことができます。<br>
・購入するには，資金<b>$buymsg</b>がかかります。<br>
・名前は，<b>全角カタカナ10文字</b>以内です。
$TBE
STR
	}
}
1;



