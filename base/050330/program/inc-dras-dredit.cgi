# ドラゴンレース ドラゴンメンテ 2005/03/30 由來

ReadDragon();
$disp.="<BIG>●ドラゴンレース：牧場</BIG><br><br>";

my $functionname=$Q{code};
OutError("bad request") if !defined(&$functionname);
&$functionname;

WriteDragon();
CoDataCA();
1;

sub new
{
	#牧場チェック
	ReadRanch();
	OutError("bad request") if ($MYRC==-1);

	OutError('資金の余裕がありません。') if ($DT->{money} < $DRbuy);
	OutError('これ以上ドラゴンを所有できません。') if (scalar @MYDR >= $MYDRmax);

	# 名前の正当性をチェック
	require $JCODE_FILE;
	if(!$Q{name})
	{
		OutError('名前を入力してください。');
	}
	$Q{name}=jcode::sjis($Q{name},$CHAR_SHIFT_JIS&&'sjis');
	if($Q{name} =~ /([,:;\t\r\n<>&])/ || CheckNGName($Q{name}) )
	{
		OutError('名前に使用できない文字が含まれています。');
	}

	#一度EUCに変換
	&jcode::convert(\$Q{name}, "euc", "sjis");
	$ZkatakanaExt = '(?:\xA5[\xA1-\xF6]|\xA1[\xA6\xBC\xB3\xB4])';
	OutError('名前は全角カタカナで指定してください。') if ($Q{name} !~ /^($ZkatakanaExt)*$/);
	&jcode::convert(\$Q{name}, "sjis", "euc");

	OutError('名前が長すぎます。') if length($Q{name})>20;
	OutError('名前が短すぎます。') if length($Q{name})<6;

	@DR=reverse(@DR);
	$DRcount++;
	my $i=$DRcount;
	$DR[$i]->{no}=($i > 0) ? ($DR[$i-1]->{no} + 1) : 1 ;
	$DR[$i]->{birth}=$NOW_TIME - 5 * 86400;
	$DR[$i]->{fm}=$Q{fm};
	$DR[$i]->{color}=int(rand(scalar @DRCOLOR));
	$DR[$i]->{name}=$Q{name};
	$DR[$i]->{town}=$MYDIR;
	$DR[$i]->{owner}=$DT->{id};
	$DR[$i]->{apt}=1400 + ($Q{dist} * 600) + int(rand(3))*100;
	$DR[$i]->{sp}=10 + int(rand(20));
	$DR[$i]->{sr}=5 + int(rand(20));
	$DR[$i]->{ag}=5 + int(rand(20));
	$DR[$i]->{pw}=10 + int(rand(20));
	$DR[$i]->{hl}=10 + int(rand(40));
	$DR[$i]->{fl}=10 + int(rand(20));
	$DR[$i]->{con}=70 + int(rand(20));
	$DR[$i]->{wt}=49 + int(rand(3));

	# 特徴がないとかわいそうなので特徴付与
	if ($DR[$i]->{sr} > $DR[$i]->{ag})
		{
		$DR[$i]->{sr}+=15;
		}
		else
		{
		$DR[$i]->{ag}+=15;
		}
	@DR=reverse(@DR);

WritePayLog($MYDIR,$DT->{id},-$DRbuy);
$disp.="新しいドラゴン「<b>".$Q{name}."</b>」を購入しました。";
}

sub ent
{
my $cnt=$id2dra{$Q{dr}};
OutError("bad request") if ($DR[$cnt]->{town} ne $MYDIR || $DR[$cnt]->{owner} != $DT->{id});

ReadStable();
OutError("bad request") if (!scalar @ST);
OutError("bad request") if (!defined $id2st{$Q{ent}});
$DR[$cnt]->{stable}=$Q{ent};
my $i=$id2st{$Q{ent}};
$disp.="ドラゴンを厩舎「".$ST[$i]->{name}."」に預託しました。";
}

sub torace
{
	#ドラゴンチェック
	my $cnt=$id2dra{$Q{dr}};
	OutError("bad request") if ($DR[$cnt]->{town} ne $MYDIR || $DR[$cnt]->{owner} != $DT->{id});
	OutError("bad request") if ($DR[$cnt]->{race} > 1);

	#牧場チェック
	ReadRanch();
	OutError("bad request") if ($MYRC==-1);

	#レースチェック
	my $rcode=$Q{rcode};
	ReadRace($rcode);
	OutError("現在".$RACETERM[$rcode]."は出走登録を受け付けていません") if ($RDS[0]);

	my @MYRACE=@{$RACE[$rcode]};
	my @R=@{$MYRACE[$RDS[1]]};
	undef @RACE;
	undef @MYRACE;	#不必要な配列は解放

	OutError("次回の".$R[0]."は賞金未獲得のドラゴンのみ出走できます") if ($R[1]==5 && $DR[$cnt]->{prize} > 0);

	#所属厩舎を調べる
	ReadStable();
	my $stname="";
	if (scalar @ST)
	{
	foreach(0..$STcount)
		{
		$stname=$ST[$_]->{name},last if ($ST[$_]->{no}==$DR[$cnt]->{stable});
		}
	}

	my $lose="実力不足";
	my ($sp,$sr,$ag,$pw)=($DR[$cnt]->{sp},$DR[$cnt]->{sr},$DR[$cnt]->{ag},$DR[$cnt]->{pw});

	# パワー配分
	my $pwp=$R[3] * 4 + $RDS[2] * 3 + 1;
	$lose="パワー不足" if ($pwp > 1 && $sp < $pw);
	$sp=int(($sp * (10 - $pwp) + $pw * $pwp) / 10);

	# 体調による影響 最大でスピード5割
	$sp-=int($sp*(100 - $DR[$cnt]->{con})/200);
	$lose="体調不調" if ($DR[$cnt]->{con} < 60);

	# 体重とハンデによる影響 10トンでスピード5割
	my $wt=$DR[$cnt]->{wt} - 50;
	$wt=-$wt if ($wt < 0);
	$wt+=int($DR[$cnt]->{prize} / $R[2]) if $R[2];
	$sp-=int($sp*$wt/20);
	$lose="重量調整失敗" if ($wt > 2);

	my $sp1=$sp2=$sp3=$sp4=$sp * 6 + 1000;		#基準速度 1000 - 1600

	# 終盤に坂がある場合
	$sp4=$sp * 4 + $pw * 2 + 950 if $R[4];

	if (!$Q{str})
		{
		#逃げの場合
		$sp1+=$sr * 6 - $ag * 4 + 40;
		$sp2+=$sr * 2 + 50;
		$sp1=$sp2 if ($sp1 < $sp2);
		}
	elsif ($Q{str}==1)
		{
		#先行の場合
		$sp1+=$sr * 2 + 50;
		$sp2+=$sr * 4 + 100;
		}
	elsif ($Q{str}==2)
		{
		#差しの場合
		$sp3+=$ag * 4 + 100;
		$sp4+=$ag * 2 + 50;
		}
	else
		{
		#追込の場合
		$sp3+=$ag * 2 + 50;
		$sp4+=$ag * 6 - $sr * 4 + 40;
		$sp4=$sp3 if ($sp4 < $sp3);
		} 

	# 距離適性による影響
	my $m=GetRaceApt($DR[$cnt]->{apt},$DR[$cnt]->{fl},$R[5]);
	if ($m > 0)
		{
		$lose="距離短すぎ";
		$m=300 if $m > 300;
		$sp1-=$m * 2;
		$sp2-=$m;
		}
	elsif ($m < 0)
		{
		$lose="距離長すぎ";
		$m=-300 if $m < -300;
		$sp1+=$m * 2;
		$sp2+=$m;
		}

	#騎手を調べる
	my $jkname="";
	if ($Q{jock})
	{
	ReadJock();
	if (scalar @JK)
		{
		foreach(0..$JKcount)
			{
			next if ($JK[$_]->{no}!=$Q{jock});
			OutError("その騎手はすでに他の竜に騎乗しています") if ($JK[$_]->{race} > 1);
			$jkname=$JK[$_]->{name};
			$JK[$_]->{race}=2;

			#騎手による補正
			$sp1+=int($sp1 * $JK[$_]->{ahead} / 20 / 100);
			$sp2+=int($sp2 * $JK[$_]->{ahead} / 20 / 100);
			$sp3+=int($sp3 * $JK[$_]->{back} / 20 / 100);
			$sp4+=int($sp4 * $JK[$_]->{back} / 20 / 100);

			WriteJock();
			last;
			}
		}
	}

	my $i=$RDcount;
	$RDcount++;
	$RD[$i]->{no}=($i > 0) ? ($RD[$i-1]->{no} + 1) : 1 ;
	$RD[$i]->{dr}=$Q{dr};

	$RD[$i]->{birth}=$DR[$cnt]->{birth};
	$RD[$i]->{fm}=$DR[$cnt]->{fm};
	$RD[$i]->{color}=$DR[$cnt]->{color};
	$RD[$i]->{name}=$DR[$cnt]->{name};
	$RD[$i]->{ranch}=$RC[$MYRC]->{no};
	$RD[$i]->{rcname}=$RC[$MYRC]->{name};
	$RD[$i]->{stable}=$DR[$cnt]->{stable};
	$RD[$i]->{stname}=$stname;
	$RD[$i]->{jock}=$Q{jock};
	$RD[$i]->{jkname}=$jkname;
	$RD[$i]->{prize}=$DR[$cnt]->{prize};
	$RD[$i]->{strate}=GetRaceStrate($DR[$cnt]->{sr},$DR[$cnt]->{ag});
	$RD[$i]->{sp1}=$sp1;
	$RD[$i]->{sp2}=$sp2;
	$RD[$i]->{sp3}=$sp3;
	$RD[$i]->{sp4}=$sp4;
	$RD[$i]->{str}=$Q{str};
	$lose="作戦ミス" if ($Q{str} != $RD[$i]->{strate});
	$RD[$i]->{lose}=$lose;

	WriteRace($rcode);

	$DR[$cnt]->{race}=2;
$disp.="ドラゴン「".$DR[$cnt]->{name}."」を".$R[0]."に出走登録しました。";
}

