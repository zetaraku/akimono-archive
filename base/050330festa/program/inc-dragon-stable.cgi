# ドラゴンレース 厩舎メニュー表示 2005/03/30 由來

ReadStable();
$disp.="<BIG>●ドラゴンレース：厩舎</BIG><br><br>";

if ($MYST==-1)
{
$disp.="$TB$TR$TD".GetTagImgKao("ドラゴン調教師","slime3").$TD;
$disp.="<SPAN>ドラゴン調教師</SPAN>：自分の厩舎を持っていないようだな。<br>";
$disp.="厩舎を持てば，自分や他人のドラゴンを調教することができる。".$TRE.$TBE."<br>";
if (scalar @ST < $STmax)
	{
	FormStable();
	}
	else
	{
	$disp.="<BIG>●厩舎設立</BIG>： 定数に達しているため，これ以上設立できません。";
	}
}
else
{
	$disp.="$TB$TR$TDB名称$TDB方針$TDB調教$TDB体調$TDB体重$TDBコース$TDB併竜$TDB坂路$TDBダート$TDB温泉$TDB繋養$TDB成績$TDB維持費$TDB老朽化$TRE";
	$disp.=$TR;
	$disp.=$TD.$ST[$MYST]->{name};
	$disp.=$TD.$EMPHA[$ST[$MYST]->{emp}];
	$disp.=$TD.$VALUE[int($ST[$MYST]->{tr} /100*6)];
	$disp.=$TD.$VALUE[int($ST[$MYST]->{con} /100*6)];
	$disp.=$TD.$VALUE[int($ST[$MYST]->{wt} /100*6)];
	$disp.=$TD.$EVALUE[$ST[$MYST]->{sp}];
	$disp.=$TD.$EVALUE[$ST[$MYST]->{sr}];
	$disp.=$TD.$EVALUE[$ST[$MYST]->{ag}];
	$disp.=$TD.$EVALUE[$ST[$MYST]->{pw}];
	$disp.=$TD.$EVALUE[$ST[$MYST]->{hl}];
	$disp.=$TD.$EVALUE[$ST[$MYST]->{fl}];
	$disp.=$TD.($ST[$MYST]->{g1win} + 0)." - ".($ST[$MYST]->{g2win} + 0)." - ".($ST[$MYST]->{g3win} + 0)." - ".($ST[$MYST]->{sdwin} + 0);
	$cost=($ST[$MYST]->{sp} + $ST[$MYST]->{sr} + $ST[$MYST]->{ag} + $ST[$MYST]->{pw} + $ST[$MYST]->{hl} + $ST[$MYST]->{fl});
	$disp.=$TD.GetMoneyString($cost * $STcost);
	my $limit=$ST[$MYST]->{birth} + $STtime - $NOW_TIME;
	$disp.=$TD."あと ".(($limit > 0) ? GetTime2found($limit) : "わずか");
	$disp.=$TRE.$TBE."<br>";
	StableDragon();
	FormLarge();
}
1;

sub FormStable
{
my $estmsg=GetMoneyString($STest);
my $costmsg=GetMoneyString($STcost);
my $formemp;
	foreach (0..$#EMPHA)
	{
	$formemp.="<OPTION VALUE=\"$_\">$EMPHA[$_]";
	}
$disp.=<<STR;
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="slime-s">
<INPUT TYPE=HIDDEN NAME=bk VALUE="slime">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="stedit">
<INPUT TYPE=HIDDEN NAME=code VALUE="new">
<BIG>●厩舎設立</BIG>： <SELECT NAME=emp SIZE=1>
$formemp
</SELECT> を調教方針とする厩舎を <INPUT TYPE=TEXT NAME=name SIZE=20> と名付けて 
<INPUT TYPE=SUBMIT VALUE='設立'>
</FORM>
<br>
$TB$TR$TD
・厩舎を設立するには，資金<b>$estmsg</b>がかかります。<br>
・維持費が最低でも毎日<b>$costmsg</b>かかります。<br>
・調教方針を選べます。後から変更することはできません。<br>
・厩舎は全体で <b>$STmax</b>舎の上限があり，満杯になると設立できません。
$TBE
STR
}

sub StableDragon
{
	$disp.="<BIG>●入厩中の竜</BIG><br><br>";
	ReadDragon();
	$disp.="$TB$TR$TDB名称$TDB年齢$TDB性別$TDB体調$TDB体重$TDB総賞金$TDB成績$TRE";
	foreach(0..$#DR)
	{
	next if ($DR[$_]->{stable} != $ST[$MYST]->{no});
$disp.=$TR;
$disp.=$TD.GetTagImgDra($DR[$_]->{fm},$DR[$_]->{color}).$DR[$_]->{name};
$disp.=$TD.GetTime2found($NOW_TIME-$DR[$_]->{birth});
$disp.=$TD.$FM[$DR[$_]->{fm}];
$disp.=$TD.$EVALUE[int($DR[$_]->{con} /100*4)];
$disp.=$TD.$DR[$_]->{wt};
$disp.=$TD.($DR[$_]->{prize} + 0)."万";
$disp.=$TD.($DR[$_]->{g1win} + 0)." - ".($DR[$_]->{g2win} + 0)." - ".($DR[$_]->{g3win} + 0)." - ".($DR[$_]->{sdwin} + 0);
$disp.=$TRE;
	}
$disp.=$TBE."<br>";
}


sub FormLarge
{
my $n=int(($NOW_TIME - $ST[$MYST]->{birth})/86400/2) + 1;
if ($n < $cost)
	{
	$disp.="<BIG>●厩舎増築</BIG>： まだこれ以上の増築はできません";
	return;
	}
my $estmsg=GetMoneyString($STest);
my @LARGE=(
	'トラックコース (スピード上昇)',
	'併せ竜 (勝負根性上昇)',
	'坂路施設 (瞬発力上昇)',
	'ダートトラック (パワー上昇)',
	'温泉施設 (健康上昇)',
	'繋養施設 (柔軟性上昇)'
);
my $formemp;
	foreach (0..$#LARGE)
	{
	$formemp.="<OPTION VALUE=\"$_\">$LARGE[$_]";
	}
$disp.=<<STR;
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="slime-s">
<INPUT TYPE=HIDDEN NAME=bk VALUE="slime">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="stedit">
<INPUT TYPE=HIDDEN NAME=code VALUE="large">
<BIG>●厩舎増築</BIG>： <SELECT NAME=lar SIZE=1>
$formemp
</SELECT> を <INPUT TYPE=SUBMIT VALUE='増築'>
</FORM>
<br>
$TB$TR$TD
・厩舎を増築するには，資金<b>$estmsg</b>がかかります。<br>
・増築すると維持費が多くかかるようになります。<br>
・預託料の収入より維持費が上回ると，赤字になるのでご注意ください。
$TBE
STR
}

