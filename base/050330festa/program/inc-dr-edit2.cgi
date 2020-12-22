# ドラゴンレース レース展開 2005/03/30 由來

if ($NOW_TIME > $DRTIME[2]) { $rcode=1; } else { $rcode=0; }

ReadRace($rcode);

@MYRACE=@{$RACE[$rcode]};
@R=@{$MYRACE[$RDS[1]]};
undef $RACELOG;
if (!$RDS[0])
	{
	Entry();
	}
	else
	{
	my $functionname="Race".$RDS[0];
	&$functionname;
	}
WriteRaceLog($rcode,$RACELOG) if $RACELOG;
WriteRace($rcode);
WriteDrLast();
RenewDraLog();
CoDataCA();
CoUnLock();
1;


sub WriteRaceLog
{
	my($f,$message)=@_;
	$f||=0;
	my $fn=GetPath($COMMON_DIR,"dra-rlog$f");
	open(OUT,">>$fn") or return;
	print OUT $message;
	close(OUT);
}

sub Entry
{
	# 出走スライム確定処理
	ReadDragon();
	ReadJock();

	if (scalar @RD < 3)
		{
		# 出走数が３つに満たない場合は全部落選しお流れ
		foreach(0..$#RD)
			{
			my $id=$RD[$_]->{dr};
			$DR[$id2dra{$id}]->{race}=1 if (defined $id2dra{$id});

			$id=$RD[$_]->{jock};
			$JK[$id2jk{$id}]->{race}=1 if (defined $id2jk{$id});

			undef $RD[$_];

			}
		PushDraLog($rcode+1,$R[0]."は出走竜不足のため開催が見送られました。");
		$DRTIME[$rcode+1]+=86400*2;
		$RDS[1]++;
		$RDS[1]=0 if ($RDS[1] > $#MYRACE);
		$RDS[2]=int(rand(2));
		}
		else
		{
		PushDraLog($rcode+1,$R[0]."の出走登録が締め切られました。");
		# 出走数が定員を超える場合は抽選
		if (scalar @RD > $R[9])
			{
			foreach(0..$#RD) { $RD[$_]->{rnd}=($RD[$_]->{prize} * 10000) + int(rand(10000));}
			if ($rcode)
				{
				@RD=sort{$b->{rnd}<=>$a->{rnd}}@RD;	#重賞レースは大きい順
				}
				else
				{
				@RD=sort{$a->{rnd}<=>$b->{rnd}}@RD;	#登竜レースは小さい順
				}
			foreach($R[9]..$#RD)
				{
				#落選
				my $id=$RD[$_]->{dr};
				$DR[$id2dra{$id}]->{race}=1 if (defined $id2dra{$id});

				$id=$RD[$_]->{jock};
				$JK[$id2jk{$id}]->{race}=1 if (defined $id2jk{$id});
				undef $RD[$_];
				}
			PushDraLog($rcode+1,"出走竜多数のため，抽選が行われました。");
			}

		#出走処理
		my $num=$R[9] - 1;
		foreach(0..$num)
			{
			next if !$RD[$_]->{name};
			$RD[$_]->{no}=$_ + 1;	#枠番振り直し
			my $id=$RD[$_]->{dr};
			$DR[$id2dra{$id}]->{race}=3 if (defined $id2dra{$id});

			$id=$RD[$_]->{jock};
			$JK[$id2jk{$id}]->{race}=3 if (defined $id2jk{$id});
			}

		$DRTIME[$rcode+1]+=3600*2;
		$RDS[0]++;
		}
	my $fn=GetPath($COMMON_DIR,"dra-rlog$rcode");
	unlink $fn if -e $fn;				#過去の実況ログ消去
	WriteDragon();
	WriteJock();
}

sub Race1
{
	# 人気の決定
	foreach(0..$#RD) { $RD[$_]->{sumsp}=$RD[$_]->{prize}*100 + int(rand(100)); }
	@RD=sort{$b->{sumsp}<=>$a->{sumsp}}@RD;

	foreach(0..$#RD)
		{
		$RD[$_]->{pop}=$_ + 1;		#人気を出力
		$RD[$_]->{time}+=int($R[5] * 1000 / 4 / $RD[$_]->{sp1});
		}
	@RD=sort{$a->{time}<=>$b->{time}}@RD;

	$RACELOG.="それでは <b>".$R[0]."</b>の出走です<br>\n";
	$RACELOG.="初々しい竜たちが勢ぞろい<br>\n" if $R[1]==5;
	$RACELOG.="栄冠を手にするのは 果たしてどの竜なのか<br>\n" if $R[1]==0;
	$RACELOG.="このコースの終盤は坂になっています 一波乱あるかもしれません<br>\n" if $R[4];
	$RACELOG.="いま スタートです<br>\n";

	if ($RD[0]->{strate}< 2)
		{
		$RACELOG.="トップに立ったのは <b>".GetTagImgDra($RD[0]->{fm},$RD[0]->{color}).$RD[0]->{name}."</b><br>\n";
		$RACELOG.="大方の予\想通りといったところでしょうか<br>\n";
		}
		else
		{
		$RACELOG.="なんと <b>".GetTagImgDra($RD[0]->{fm},$RD[0]->{color}).$RD[0]->{name}."</b> がいきなりトップに立ちました<br>\n";
		$RACELOG.="これは 作戦なのか<br>\n";
		}

	#任意の１頭を紹介
	my $i=int(rand($#RD))+1;
	$RACELOG.="現在 ".($i + 1)."番目を走っているのは ".$RD[$i]->{no}."枠 <b>".GetTagImgDra($RD[$i]->{fm},$RD[$i]->{color}).$RD[$i]->{name}."</b><br>\n";
	if ($RD[$i]->{pop} < 4)
		{
		$RACELOG.=$RD[$i]->{pop}."番人気の期待を受け この位置から勝利を狙います<br>\n";
		}
		else
		{
		$RACELOG.="人気は ".$RD[$i]->{pop}."番となりましたが 果たしてこの竜は伏兵となるでしょうか<br>\n";
		}

	$DRTIME[$rcode+1]+=3600*8;
	$RDS[0]++;
}

sub Race2
{
	my $no=$RD[0]->{no};	#以前の１位を控えておく
	foreach(0..$#RD)
		{
		$RD[$_]->{time}+=int($R[5] * 1000 / 4 / $RD[$_]->{sp2});
		}
	@RD=sort{$a->{time}<=>$b->{time}}@RD;

	$RACELOG.="最初のコーナーを回りました<br>\n";
	if ($no == $RD[0]->{no})
		{
		$RACELOG.="現在 トップは変わらず <b>".GetTagImgDra($RD[0]->{fm},$RD[0]->{color}).$RD[0]->{name}."</b><br>\n";
		$RACELOG.="この勢いは 最後まで続くのか<br>\n";
		}
		else
		{
		$RACELOG.="ここで トップが変わる ";
		$RACELOG.="トップは <b>".GetTagImgDra($RD[0]->{fm},$RD[0]->{color}).$RD[0]->{name}."</b><br>\n";
		}

	#レース展開判定 未実装
	$RACELOG.="中間".($R[5] / 2)."kmの通過タイムは ".GetRaceTime($RD[0]->{time})."<br>\n";
	$RACELOG.="ほぼ 平常どおりといえるでしょう 展開にさほど影響はなさそうです<br>\n";

	#差し馬の１頭を紹介
	my $i=int(rand($#RD))+1;
	foreach(1..$#RD)
		{
		$i=$_,last if ($RD[$_]->{strate}==2 || $RD[$_]->{strate}==3);
		}
	$RACELOG.="<b>".GetTagImgDra($RD[$i]->{fm},$RD[$i]->{color}).$RD[$i]->{name}."</b> いい位置だ ここから トップを狙うのか<br>\n";

	$DRTIME[$rcode+1]+=3600*8;
	$RDS[0]++;
}

sub Race3
{
	my $no=$RD[0]->{no};
	foreach(0..$#RD)
		{
		$RD[$_]->{time}+=int($R[5] * 1000 / 4 / $RD[$_]->{sp3});
		}
	@RD=sort{$a->{time}<=>$b->{time}}@RD;

	$RACELOG.="後続竜が差を詰めていきます<br>\n";
	if ($no == $RD[0]->{no})
		{
		$RACELOG.="さあ どうか</b> ";
		$RACELOG.="トップは変わらず <b>".GetTagImgDra($RD[0]->{fm},$RD[0]->{color}).$RD[0]->{name}."</b><br>\n";
		$RACELOG.="このまま 逃げ切れるのか ";
		}
		else
		{
		$RACELOG.="<b>".GetTagImgDra($RD[0]->{fm},$RD[0]->{color}).$RD[0]->{name}."</b> が差した！<br>\n";
		$RACELOG.="さあ どうか</b> ";
		}
	$RACELOG.="後を追うのは <b>".GetTagImgDra($RD[1]->{fm},$RD[1]->{color}).$RD[1]->{name}."</b><br>\n";

	#差し馬の１頭を紹介
	my $i=int(rand($#RD))+1;
	foreach(2..$#RD)
		{
		$i=$_,last if ($RD[$_]->{strate}==2 || $RD[$_]->{strate}==3);
		}
	$RACELOG.="<b>".GetTagImgDra($RD[$i]->{fm},$RD[$i]->{color}).$RD[$i]->{name}."</b> いい足取りだが どうか<br>\n";

	$DRTIME[$rcode+1]+=3600*6;
	$RDS[0]++;
}

sub Race4
{
	my $no=$RD[0]->{no};
	foreach(0..$#RD)
		{
		$RD[$_]->{time}+=int($R[5] * 1000 / 4 / $RD[$_]->{sp4});
		}
	@RD=sort{$a->{time}<=>$b->{time}}@RD;

	my $name1=GetTagImgDra($RD[0]->{fm},$RD[0]->{color})."<b>".$RD[0]->{name}."</b>";
	my $name2=GetTagImgDra($RD[1]->{fm},$RD[1]->{color})."<b>".$RD[1]->{name}."</b>";

	$RACELOG.="最後のコーナーをまわって 直線に入ります<br>\n";
	if ($no == $RD[0]->{no})
			{
			# トップ変わらず
			$RACELOG.="さあ どうか ";
			$RACELOG.="$name2 が追い上げる<br>\n";
			$RACELOG.="$name1 が逃げる このまま逃げ切るか<br>\n";

			if ($RD[1]->{time} - $RD[0]->{time} < 15)
				{
				$RACELOG.="$name2 が迫る！ しかし $name1 も粘る！<br>\n";
				$RACELOG.="$name1 だ！ 逃げ切りました！ 勝ったのは $name1！<br>\n";
				}
				else
				{
				$RACELOG.="$name1 差を広げる！<br>\n";
				$RACELOG.="$name1！ この竜は強い！ 勝ったのは $name1！<br>\n";
				}
			}
		elsif ($no == $RD[1]->{no})
			{
			# ２着
			$RACELOG.="さあ どうか ";
			$RACELOG.="$name1 が追い上げる<br>\n";
			$RACELOG.="$name2 が逃げる このまま逃げ切るか<br>\n";
			if ($RD[1]->{time} - $RD[0]->{time} < 15)
				{
				$RACELOG.="$name1 が迫る！ $name2 が粘る！<br>\n";
				$RACELOG.="$name1 が差した！<br>\n";
				$RACELOG.="$name2 一歩及ばず！ 勝ったのは $name1！<br>\n";
				}
				else
				{
				$RACELOG.="$name1 が差した！<br>\n";
				$RACELOG.="$name1 さらに差を広げる！<br>\n";
				$RACELOG.="$name1！ この竜は強い！ 勝ったのは $name1！<br>\n";
				}
			}
		else
			{
			# トップ完全交代
			$RACELOG.="さあ どうか ";
			$RACELOG.="$name2 が差した！<br>\n";
			$RACELOG.="さらに <b>$name1</b> が後に続く！<br>\n";
			if ($RD[1]->{time} - $RD[0]->{time} < 15)
				{
				$RACELOG.="$name1 が迫る！ $name2 が粘る！<br>\n";
				$RACELOG.="$name1 が差した！<br>\n";
				$RACELOG.="$name2 一歩及ばず！ 勝ったのは $name1！<br>\n";
				}
				else
				{
				$RACELOG.="$name1 が一気に差した！<br>\n";
				$RACELOG.="$name1 さらに差を広げる！<br>\n";
				$RACELOG.="$name1！ この竜は強い！ 勝ったのは $name1！<br>\n";
				}
			}

	ReadDragon();
	ReadJock();
	ReadRanch();
	ReadStable();

	# トップ
	PushDraLog($rcode+1,$R[0]."で「".$RD[0]->{name}."」が勝ちました。");

	my $id=$RD[0]->{dr};
	if (defined $id2dra{$id})
		{
		my $i=$id2dra{$id};
		$DR[$i]->{gr}+=80;
		$DR[$i]->{prize}+=$R[6];

		WritePayLog($DR[$i]->{town},$DR[$i]->{owner},$R[6]*10000);

		if ($R[1] > 2) { $DR[$i]->{sdwin}++;}
		elsif ($R[1]==2) { $DR[$i]->{g3win}++;}
		elsif ($R[1]==1) { $DR[$i]->{g2win}++;}
		else { $DR[$i]->{g1win}++;}
		}

	# トップ騎手
	my $id=$RD[0]->{jock};
	if (defined $id2jk{$id})
		{
		my $i=$id2jk{$id};
		$JK[$i]->{sp}=int(rand(scalar @JKSP)) if !$JK[$i]->{sp};

		#とった作戦に応じて能力上昇
		if ($RD[0]->{str} > 1)
			{
			$JK[$i]->{back}+=15;
			$JK[$i]->{back}=100 if ($JK[$i]->{back} > 100);
			}
			else
			{
			$JK[$i]->{ahead}+=15;
			$JK[$i]->{ahead}=100 if ($JK[$i]->{ahead} > 100);
			}
		if ($R[1] > 2) { $JK[$i]->{sdwin}++;}
		elsif ($R[1]==2) { $JK[$i]->{g3win}++;}
		elsif ($R[1]==1) { $JK[$i]->{g2win}++;}
		else { $JK[$i]->{g1win}++;}
		}

	# トップ牧場
	my $id=$RD[0]->{ranch};
	if (defined $id2rc{$id})
		{
		my $i=$id2rc{$id};
		$RC[$i]->{prize}+=$R[6];
		if ($R[1] > 2) { $RC[$i]->{sdwin}++;}
		elsif ($R[1]==2) { $RC[$i]->{g3win}++;}
		elsif ($R[1]==1) { $RC[$i]->{g2win}++;}
		else { $RC[$i]->{g1win}++;}
		}

	# トップ厩舎
	my $id=$RD[0]->{stable};
	if (defined $id2st{$id})
		{
		my $i=$id2st{$id};
		$ST[$i]->{tr}+=int(rand(20));
		$ST[$i]->{tr}=100 if ($ST[$i]->{tr} > 100);
		$ST[$i]->{con}+=int(rand(20));
		$ST[$i]->{con}=100 if ($ST[$i]->{con} > 100);
		$ST[$i]->{wt}+=int(rand(20));
		$ST[$i]->{wt}=100 if ($ST[$i]->{wt} > 100);

		if ($R[1] > 2) { $ST[$i]->{sdwin}++;}
		elsif ($R[1]==2) { $ST[$i]->{g3win}++;}
		elsif ($R[1]==1) { $ST[$i]->{g2win}++;}
		else { $ST[$i]->{g1win}++;}
		}

	# ２着
	my $id=$RD[1]->{dr};
	if (defined $id2dra{$id})
		{
		my $i=$id2dra{$id};
		$DR[$i]->{gr}+=40;
		$DR[$i]->{prize}+=$R[7];

		WritePayLog($DR[$i]->{town},$DR[$i]->{owner},$R[7]*10000);
		}

	# ２着牧場
	my $id=$RD[1]->{ranch};
	if (defined $id2rc{$id})
		{
		my $i=$id2rc{$id};
		$RC[$i]->{prize}+=$R[7];
		}

	# ３着
	my $id=$RD[2]->{dr};
	if (defined $id2dra{$id})
		{
		my $i=$id2dra{$id};
		$DR[$i]->{gr}+=20;
		$DR[$i]->{prize}+=$R[8];

		WritePayLog($DR[$i]->{town},$DR[$i]->{owner},$R[8]*10000);
		}

	# ３着牧場
	my $id=$RD[2]->{ranch};
	if (defined $id2rc{$id})
		{
		my $i=$id2rc{$id};
		$RC[$i]->{prize}+=$R[8];
		}

	$RACELOG.="<br>";
	foreach(0..$#RD)
		{
		$RACELOG.=($_ + 1)."着 ".GetRaceTime($RD[$_]->{time});
		$RACELOG.=" ".$STRATE[ $RD[$_]->{str} ]." ";
		$RACELOG.=GetTagImgDra($RD[$_]->{fm},$RD[$_]->{color}).$RD[$_]->{name};
		$RACELOG.=" <small>(".$RD[$_]->{lose}.")</small>" if $_;
		$RACELOG.="<br>";
		my $id=$RD[$_]->{dr};
		if (defined $id2dra{$id})
			{
			my $i=$id2dra{$id};
			$DR[$i]->{race}=0;
			$DR[$i]->{con}-=40;
			$DR[$i]->{con}=0 if ($DR[$i]->{con} < 0);

			$DR[$i]->{wt}-=4;
			$DR[$i]->{wt}=38 if ($DR[$i]->{wt} < 38);
			}
		$id=$RD[$_]->{jock};
		$JK[$id2jk{$id}]->{race}=0 if (defined $id2jk{$id});

		undef $RD[$_];
		}
	WriteDragon();
	WriteJock();
	WriteRanch();
	WriteStable();

	$DRTIME[$rcode+1]=$NOW_TIME + 86400 -(($NOW_TIME + $TZ_JST - $DRTIMESET[$rcode+1] * 3600) % 86400);
	$RDS[0]=0;
	$RDS[1]++;
	$RDS[1]=0 if ($RDS[1] > $#MYRACE);
	$RDS[2]=int(rand(2));
}

