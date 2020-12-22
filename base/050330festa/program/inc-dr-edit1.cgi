# ドラゴンレース 調教 2005/03/30 由來

my $stflag=0;
ReadDragon();
ReadStable();
ReadRanch();
foreach(0..$#DR)
	{
	$DR[$_]->{race}=0 if ($DR[$_]->{race}==1);	#落選を待機に改める
	next if ($DR[$_]->{race});			#出走中のドラゴンは変化なし

	if ($NOW_TIME-$DR[$_]->{birth} > $DRretire * 4)
		{
		# 引退
		PushDraLog(0,$DR[$_]->{name}."は引退しました。");
		undef $DR[$_];
		next;
		}

	next if ($NOW_TIME-$DR[$_]->{birth} > ($DRretire * 5 / 2 + $DR[$_]->{hl} * 86400 / 10));	# 体力の限界

	$DR[$_]->{wt}+=int(rand(3)) - 1;			#体重変動
	$DR[$_]->{wt}=38 if ($DR[$_]->{wt} < 38);
	$DR[$_]->{wt}=62 if ($DR[$_]->{wt} > 62);

	$DR[$_]->{con}+=int(rand(3) + $DR[$_]->{hl} / 20) + 1;	#体調回復
	$DR[$_]->{con}=100 if ($DR[$_]->{con} > 100);

	my $id=$DR[$_]->{stable};
	next if (!defined $id2st{$id});			#厩舎に所属していなければ調教なし
	my $cnt=$id2st{$id};

	WritePayLog($DR[$_]->{town},$DR[$_]->{owner},-$STcost);	#預託料
	WritePayLog($ST[$cnt]->{town},$ST[$cnt]->{owner},$STcost);

	$DR[$_]->{con}+=int($ST[$cnt]->{con} / 25)+1;	#体調管理
	if ($ST[$cnt]->{wt} + 100 > rand(200))
		{
		#体重管理
		$DR[$_]->{wt}+=2 if ($DR[$_]->{wt} < 50);
		$DR[$_]->{wt}-=2 if ($DR[$_]->{wt} > 50);
		}

	$DR[$_]->{gr}+=int($ST[$cnt]->{tr} / 10 + rand(7) + 23);
	next if ($DR[$_]->{gr} < 100);

	#成長
	$DR[$_]->{gr}-=100;
		
	my @grow=qw(
		sp spp sr srp ag agp pw pwp hl hlp fl flp
		);
	foreach my $n(0..5)
		{
		my $i=$grow[($n * 2)];
		my $ip=$grow[($n * 2 + 1)];
		my $p=0;
		$p+=2 + int(rand(4)) if ($ST[$cnt]->{emp}==$n);
		$p+=1 + int(rand(4)) if ($ST[$cnt]->{tr} + 80 + $ST[$cnt]->{$i} * 10 > rand(200));
		$p=int($p/2) if ($n < 1);
		next if !$p;
		$DR[$_]->{$i}+=$p;
		$DR[$_]->{$ip}+=$p;
		}
	}

foreach(0..$#ST)
	{
	if ($NOW_TIME-$ST[$_]->{birth} > $STtime)
		{
		# 老朽化
		PushDraLog(0,$ST[$_]->{name}."は老朽化により閉鎖しました。");
		undef $ST[$_];
		$stflag++;
		next;
		}
	my $cost=($ST[$_]->{sp} + $ST[$_]->{sr} + $ST[$_]->{ag} + $ST[$_]->{pw} + $ST[$_]->{hl} + $ST[$_]->{fl}) * $STcost;

	WritePayLog($ST[$_]->{town},$ST[$_]->{owner},-$cost);
	}

WriteDragon();
WriteStable() if $stflag;
$DRTIME[0]=$NOW_TIME + 86400 -(($NOW_TIME + $TZ_JST - $DRTIMESET[0] * 3600) % 86400);
WriteDrLast();
RenewDraLog();
CoDataCA();
CoUnLock();
1;

