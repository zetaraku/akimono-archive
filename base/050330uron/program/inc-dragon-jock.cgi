# ドラゴンレース 騎手メニュー表示 2005/03/30 由來

ReadJock();
$disp.="<BIG>●ドラゴンレース：騎手</BIG><br><br>";

if ($MYJK==-1)
{
$disp.="$TB$TR$TD".GetTagImgKao("騎手仲間","slime5").$TD;
$disp.="<SPAN>騎手仲間</SPAN>：騎手を雇っていないんだな。<br>";
$disp.="騎手を雇えば，自分や他人のドラゴンの力をレースで引き出せる。".$TRE.$TBE."<br>";
if (scalar @JK < $JKmax)
	{
	FormJock();
	}
	else
	{
	$disp.="<BIG>●騎手雇用</BIG>： 定員に達しているため，これ以上雇用できません。";
	}
}
else
{
$disp.="$TB$TR$TDB名前$TDB勤続$TDB逃先$TDB差追$TDB成績$TDB特殊能\力$TDB出走$TRE";
$disp.=$TR;
$disp.=$TD.$JK[$MYJK]->{name};
$disp.=$TD.GetTime2found($NOW_TIME-$JK[$MYJK]->{birth});
$disp.=$TD.$VALUE[int($JK[$MYJK]->{ahead} /100*6)];
$disp.=$TD.$VALUE[int($JK[$MYJK]->{back} /100*6)];
$disp.=$TD.($JK[$MYJK]->{g1win} + 0)." - ".($JK[$MYJK]->{g2win} + 0)." - ".($JK[$MYJK]->{g3win} + 0)." - ".($JK[$MYJK]->{sdwin} + 0);
$disp.=$TD."<small>".$JKSP[($JK[$MYJK]->{sp} + 0)]."</small>";
$disp.=$TD.$ONRACE[$JK[$MYJK]->{race}];
$disp.=$TRE.$TBE;
}
1;

sub FormJock
{
my $estmsg=GetMoneyString($JKest);
$disp.=<<STR;
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="slime-s">
<INPUT TYPE=HIDDEN NAME=bk VALUE="slime">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="jkedit">
<INPUT TYPE=HIDDEN NAME=code VALUE="new">
<BIG>●騎手雇用</BIG>： <INPUT TYPE=TEXT NAME=name SIZE=20> と名付けて 
<INPUT TYPE=SUBMIT VALUE='雇用'>
</FORM>
<br>
$TB$TR$TD
・騎手を雇用するには，資金<b>$estmsg</b>がかかります。<br>
・騎手は全体で <b>$JKmax</b>人の定員があり，満員になると雇用できません。
$TBE
STR
}

