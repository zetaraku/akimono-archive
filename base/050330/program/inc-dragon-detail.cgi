# ドラゴンレース ドラゴン詳細表示 2005/03/30 由來

$disp.="<BIG>●ドラゴンレース：牧場</BIG><br><br>";

ReadDragon();
my $cnt=$id2dra{$Q{dr}};
OutError("bad request") if ($DR[$cnt]->{town} ne $MYDIR || $DR[$cnt]->{owner} != $DT->{id});
my $stname="";
$forment="";

ReadStable();
if (scalar @ST)
	{
	foreach(0..$STcount)
		{
		$stname=$ST[$_]->{name} if ($ST[$_]->{no}==$DR[$cnt]->{stable});
		$forment.="<OPTION VALUE=\"$ST[$_]->{no}\">$ST[$_]->{name}";
		}
	}

$disp.="$TB$TR$TDB名称$TDB年齢$TDB性別$TDB毛色$TDB預託厩舎$TDB脚質$TDB距離適性$TDB総賞金$TDB成績$TDB出走$TRE";
$disp.=$TR;
$disp.=$TD."<b>".GetTagImgDra($DR[$cnt]->{fm},$DR[$cnt]->{color}).$DR[$cnt]->{name}."</b>";
$disp.=$TD.GetTime2found($NOW_TIME-$DR[$cnt]->{birth});
$disp.=$TD.$FM[$DR[$cnt]->{fm}];
$disp.=$TD.$DRCOLOR[$DR[$cnt]->{color}];
$disp.=$TD.$stname;
$disp.=$TD.$STRATE[ GetRaceStrate($DR[$cnt]->{sr},$DR[$cnt]->{ag}) ];
$disp.=$TD.GetRaceApt($DR[$cnt]->{apt},$DR[$cnt]->{fl})."km";
$disp.=$TD.($DR[$cnt]->{prize} + 0)."万";
$disp.=$TD.($DR[$cnt]->{g1win} + 0)." - ".($DR[$cnt]->{g2win} + 0)." - ".($DR[$cnt]->{g3win} + 0)." - ".($DR[$cnt]->{sdwin} + 0);
$disp.=$TD.$ONRACE[$DR[$cnt]->{race}];
$disp.=$TRE;
$disp.=$TBE."<br>";
$disp.="<BIG>●能\力の詳細</BIG><br><br>";
$disp.=$TB;
$disp.=$TR.$TDB."スピード".$TD.GetDragonBar($DR[$cnt]->{sp},$DR[$cnt]->{spp}).$TRE;
$disp.=$TR.$TDB."勝負根性".$TD.GetDragonBar($DR[$cnt]->{sr},$DR[$cnt]->{srp}).$TRE;
$disp.=$TR.$TDB."瞬発力".$TD.GetDragonBar($DR[$cnt]->{ag},$DR[$cnt]->{agp}).$TRE;
$disp.=$TR.$TDB."パワー".$TD.GetDragonBar($DR[$cnt]->{pw},$DR[$cnt]->{pwp}).$TRE;
$disp.=$TR.$TDB."健康".$TD.GetDragonBar($DR[$cnt]->{hl},$DR[$cnt]->{hlp}).$TRE;
$disp.=$TR.$TDB."柔軟性".$TD.GetDragonBar($DR[$cnt]->{fl},$DR[$cnt]->{flp}).$TRE;
$disp.=$TR.$TDB."体調".$TD.GetConBar($DR[$cnt]->{con}).$TRE;
$disp.=$TR.$TDB."体重".$TD.GetWtBar($DR[$cnt]->{wt}).$TRE;
$disp.=$TR.$TDB."成長度".$TD.GetConBar($DR[$cnt]->{gr},1).$TRE;
$disp.=$TBE."<br>";
if ($DR[$cnt]->{race} < 2)
	{
	FormEnt() if (scalar @ST);
	FormToRace();
	FormRetire() if ($NOW_TIME-$DR[$cnt]->{birth} > $DRretire);
	}
1;

sub GetDragonBar
{
	my($point,$up)=@_;
	my $per=$point - $up;
	
	my $bar="";
	$bar ="<nobr>";
	$bar.=qq|<img src="$IMAGE_URL/b.gif" width="|.($per).qq|" height="12">| if $per;
	$bar.=qq|<img src="$IMAGE_URL/r.gif" width="|.($up).qq|" height="12">| if $up;
	$bar.=qq|<img src="$IMAGE_URL/t.gif" width="|.(100-$point).qq|" height="12">| if $point!=100;
	$bar.=" ".($per + 0)." + ".($up + 0);
	$bar.="</nobr>";
	return $bar;
}

sub GetConBar
{
	my($per,$mode)=@_;
	
	$per=100 if $per > 100;
	my $bar="";
	$bar ="<nobr>";
	$bar.=qq|<img src="$IMAGE_URL/r.gif" width="|.($per).qq|" height="12">| if $per;
	$bar.=qq|<img src="$IMAGE_URL/t.gif" width="|.(100-$per).qq|" height="12">| if $per!=100;
	$bar.=" ".$EVALUE[int($per/100*4)] if !$mode;
	$bar.=" ".($per + 0)."%";
	$bar.="</nobr>";
	return $bar;
}

sub GetWtBar
{
	my($point)=@_;
	my $per=($point - 40) * 5;
	my $rank=int(($point - 50) / 2);
	$rank=-$rank if ($rank < 0);
	$rank=3 - $rank;
	$rank=0 if $rank < 0;
	
	my $bar="";
	$bar ="<nobr>";
	$bar.=qq|<img src="$IMAGE_URL/r.gif" width="|.($per).qq|" height="12">| if $per;
	$bar.=qq|<img src="$IMAGE_URL/t.gif" width="|.(100-$per).qq|" height="12">| if $per!=100;
	$bar.=" ".$EVALUE[int($rank)]." ".$point."トン";
	$bar.="</nobr>";
	return $bar;
}

sub FormEnt
{
my $costmsg=GetMoneyString($STcost);
$disp.=<<STR;
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="slime-s">
<INPUT TYPE=HIDDEN NAME=bk VALUE="slime">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="dredit">
<INPUT TYPE=HIDDEN NAME=code VALUE="ent">
<INPUT TYPE=HIDDEN NAME=dr VALUE="$Q{dr}">
<BIG>●厩舎預託</BIG>： <SELECT NAME=ent SIZE=1>
$forment
</SELECT> にドラゴンを
<INPUT TYPE=SUBMIT VALUE='預託'>
</FORM>
<br>
$TB$TR$TD
・厩舎にドラゴンを預託すると，調教による成長が見込めます。<br>
・預託料が毎日<b>$costmsg</b>かかります。
$TBE<br>
STR
}

sub FormToRace
{
my $formrace="";
my $formjock="<OPTION VALUE=\"0\">－－騎手なし－－";
my $formstrate="";
foreach (0..$#RACETERM)
	{
	$formrace.="<OPTION VALUE=\"$_\">$RACETERM[$_]";
	}
foreach (0..3)
	{
	$formstrate.="<OPTION VALUE=\"$_\">$STRATE[$_]";
	}
ReadJock();
if (scalar @JK)
	{
	foreach(0..$JKcount)
		{
		next if $JK[$_]->{race} > 1;
		$formjock.="<OPTION VALUE=\"$JK[$_]->{no}\">$JK[$_]->{name}";
		}
	}


$disp.=<<STR;
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="slime-s">
<INPUT TYPE=HIDDEN NAME=bk VALUE="slime">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="dredit">
<INPUT TYPE=HIDDEN NAME=code VALUE="torace">
<INPUT TYPE=HIDDEN NAME=dr VALUE="$Q{dr}">
<BIG>●レース出走登録</BIG>： ドラゴンを <SELECT NAME=rcode SIZE=1>
$formrace
</SELECT> に，鞍上 <SELECT NAME=jock SIZE=1>
$formjock
</SELECT> 作戦 <SELECT NAME=str SIZE=1>
$formstrate
</SELECT> で 
<INPUT TYPE=SUBMIT VALUE='出走'>
</FORM>
<br>
$TB$TR$TD
・定員を超えていると，抽選によって出走できない場合があります。<br>
・出走すると，その間の調教が行われないうえ，体調・体重が減少します。<br>
・レースの距離やハンデ，他の出場竜などを見て，不利にならないか確認しましょう。
$TBE<br>
STR
}

sub FormRetire
{
my $remsg=GetTime2found($DRretire);
$disp.=<<STR;
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="slime-s">
<INPUT TYPE=HIDDEN NAME=bk VALUE="slime">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="predit">
<INPUT TYPE=HIDDEN NAME=code VALUE="retire">
<INPUT TYPE=HIDDEN NAME=dr VALUE="$Q{dr}">
<BIG>●引退</BIG>： ドラゴンを
<INPUT TYPE=SUBMIT VALUE='引退させる'>
<INPUT TYPE=TEXT NAME=check SIZE=10 VALUE="">
(retireと入力) 
</FORM>
<br>
$TB$TR$TD
・年齢 <b>$remsg</b>以上のドラゴンは，引退させることができます。<br>
・総賞金が <b>$PRentry万</b>以上のドラゴンは，種・繁殖入りします。
$TBE
STR
}

