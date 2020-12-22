# ドラゴンレース レース表示 2005/03/30 由來

my $rcode=$Q{code};
$rcode||=0;
ReadRace($rcode);
my @MYRACE=@{$RACE[$rcode]};
my @R=@{$MYRACE[$RDS[1]]};
undef @RACE;
undef @MYRACE;	#不必要な配列は解放

$disp.="<BIG>●ドラゴンレース：".$RACETERM[$rcode]."</BIG><br><br>";
$disp.="$TB$TR$TD".GetTagImgKao("レース受付","slime2").$TD;
$disp.="<SPAN>レース受付</SPAN>：";

if ($RDS[0]>1) {
$disp.="ただいまレースが行われています。<br>";
$disp.="次の実況放送は ".GetTime2FormatTime($DRTIME[$rcode + 1])." です。";
	}
elsif ($RDS[0]==1) {
$disp.="出走ドラゴンは以下のとおり決定いたしました。<br>";
$disp.="レース開始時刻は ".GetTime2FormatTime($DRTIME[$rcode + 1])." です。";
	}
else {
$disp.="ただいま出走登録を受付中です。<br>";
$disp.="登録締め切りは ".GetTime2FormatTime($DRTIME[$rcode + 1])." です。";
	}

$disp.=$TRE.$TBE."<br>";
$disp.="<b>".$R[0]."</b> (".$RACERANK[$R[1]].") ".$FIELDTYPE[$R[3]].$R[5]."km";
$disp.='<IMG class="i" SRC="'.$IMAGE_URL.'/dragonw'.($RDS[2] + 1).$IMAGE_EXT.'"> ';
$disp.="定員 ".$R[9]." ハンデ";
$disp.=($R[2] ? "$R[2]万毎" : "なし");
$disp.=qq|<br><IMG class="i" SRC="$IMAGE_URL/guildprize$IMAGE_EXT">|;
$disp.="賞金 ".$R[6]."万 - ".$R[7]."万 - ".$R[8]."万";
$disp.=qq| <input type="button" value="出走竜詳細" onclick="javascript:window.open('action.cgi?key=slime-l&mode=rd&rcode=$rcode','_blank','width=760,height=580,scrollbars')">|;
$disp.="<br><br>$TB$TR$TDB枠番$TDB名前$TDB年齢$TDB性別$TDBハンデ$TDB牧場$TDB厩舎$TDB騎手$TDB総賞金$TDB脚質$TDB人気$TDB通過タイム$TRE";

foreach (0..$#RD)
	{
	next if !$RD[$_]->{name};
	$disp.=$TR;
	$disp.=$TD.$RD[$_]->{no};
	$disp.=$TD.GetTagImgDra($RD[$_]->{fm},$RD[$_]->{color}).$RD[$_]->{name};
	$disp.=$TD.GetTime2found($NOW_TIME-$RD[$_]->{birth});
	$disp.=$TD.$FM[$RD[$_]->{fm}];
	$disp.=$TD.($R[2] ? int($RD[$_]->{prize} / $R[2]) : "0");
	$disp.=$TD.$RD[$_]->{rcname};
	$disp.=$TD.$RD[$_]->{stname};
	$disp.=$TD.$RD[$_]->{jkname};
	$disp.=$TD.($RD[$_]->{prize} + 0)."万";
	$disp.=$TD.$STRATE[ $RD[$_]->{strate} ];
	$disp.=$TD.$RD[$_]->{pop};
	$disp.=$TD.GetRaceTime($RD[$_]->{time});
	$disp.=$TRE;
	}
$disp.=$TBE."<br>";

ReadRaceLog($rcode);
$disp.=$TB.$TR.$TD.GetTagImgKao("レース受付","slime6","align=left ")."<SPAN>実況アナウンサー</SPAN><br>".$RACELOG.$TRE.$TBE if ($RACELOG);
1;

sub ReadRaceLog
{
	my($f)=@_;
	$f||=0;
	my $fn=GetPath($COMMON_DIR,"dra-rlog$f");
	undef $RACELOG;
	open(IN,$fn) or return;
	read(IN,$RACELOG,-s $fn);
	close(IN);
}

