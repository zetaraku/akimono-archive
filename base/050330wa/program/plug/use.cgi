# use プラグイン 2004/02/28 由來

sub GetUseItemList
{
	return GetUseItemListSub(@item::USE);
}

sub GetUseItemListSub
{
	my(@USE)=@_;
	foreach my $USE (@USE)
	{
		my $ret=CheckUseItem($USE);
		$USE->{dispok}=1 if $ret==2;
		$USE->{useok}=1 if $ret==1;
	}
	return @USE;
}

sub CheckUseItem
{
	my($USE)=@_;
	my $jobfunc="item::_job_use_$USE->{no}_$DT->{job}_";
	if (defined &$jobfunc)
	{
	&$jobfunc($USE->{no});
	}
	else
	{
	$jobfunc="item::_job_use_0_$DT->{job}_";
	&$jobfunc($USE->{no}) if defined &$jobfunc;
	}
	
	my $funcbefore=$USE->{functionbefore};
	if($funcbefore)
	{
		my $ret=&{"item::".$funcbefore}($USE);
		return 2 if $ret==2;
		return 0 if $ret==1;
	}
	foreach my $item (@{$USE->{use}})
	{
		return 0 if $DT->{item}[$item->{no}-1]<$item->{count};
	}
	return 1;
}

sub GetUseItem
{
	my($no)=@_;

	foreach my $USE(@item::USE)
	{
		next if $USE->{no}!=$no;
		my $ret=CheckUseItem($USE);
		$USE->{dispok}=1 if $ret==2;
		$USE->{useok}=1 if $ret==1;
		return $USE;
	}
	return 0;
}

sub UseItem
{
	my($USE,$count)=@_;
	my $usetime=GetItemUseTime($USE);
	
	#熟練度不足で作業不可能かどうかを判定(不可能ならcount=0)
	$count=0 if $DT->{exp}{$USE->{itemno}}<$USE->{needexp};
	
	#必要職業
	$count=0 if ($USE->{needjob} && ($DT->{job} ne $USE->{needjob}));
	
	#必要点数
	$count=0 if ($USE->{needpoint} && ($DT->{point} < $USE->{needpoint}));
	
	#必要人気
	$count=0 if ($USE->{needpop} && ($DT->{rank} < $USE->{needpop}));
	
	#必要イベント
	$count=0 if ($USE->{needevent} && !$DTevent{$USE->{needevent}});
	
	#費用不足でcountを補正  ※ゼロ除算を回避。
	$count=int($DT->{money}/$USE->{money}) if ($DT->{money}<$USE->{money}*$count)&&($USE->{money});
	
	#時間不足でcountを補正
	$count=int(($NOW_TIME-$DT->{time})/$usetime) if ($DT->{time}+$usetime* $count)>$NOW_TIME;
	
	#材料不足でcountを補正
	foreach my $item (@{$USE->{use}})
	{
		my $itemno=$item->{no};
		my $itemcount=$item->{count}*($item->{proba}==0 ? 1 : $count);
	
		if($DT->{item}[$itemno-1]<$itemcount)
		{
			$count=int($DT->{item}[$itemno-1]/$item->{count});
		}
	}
	
	#count確定
	$USE->{result}->{count}=$count;
	return if !$count; #countが0なら失敗
	
	#結果用変数初期化
	$USE->{result}->{useitem}=[];
	$USE->{result}->{additem}=[];
	
	#時間とお金消費
	UseTime($usetime*$count);
	$DT->{money}-=$USE->{money}*$count;
	$DT->{paytoday}+=$USE->{money}*$count;
	
	#アイテム消費
	foreach my $item (@{$USE->{use}})
	{
		my $itemno=$item->{no};
		my $itemcount=MakeAmount($item->{count}*$count,$item->{proba});
		if($itemcount)
		{
			$DT->{item}[$itemno-1]-=$itemcount;
			push(@{$USE->{result}->{useitem}},[$itemno,$itemcount]);
			push(@{$USE->{result}->{usemsg}},$item->{message});
		}
	}
	
	#アイテム取得
	foreach my $item (@{$USE->{result}->{create}})
	{
		my $itemno=$item->{no};
		my $itemcount=MakeAmount($item->{count}*$count,$item->{proba});
		if($itemcount)
		{
			if($itemcount+$DT->{item}[$itemno-1]>$ITEM[$itemno]->{limit})
			{
				$itemcount-=$ITEM[$itemno]->{limit}-$DT->{item}[$itemno-1];
				my $trashitem="これ以上持てないので".$ITEM[$itemno]->{name}."を".($itemcount).$ITEM[$itemno]->{scale}."破棄しました";
				$DTwholestore[$itemno-1]+=$itemcount;
				push(@{$USE->{result}->{trashmsg}},$trashitem);
				$itemcount=$ITEM[$itemno]->{limit}-$DT->{item}[$itemno-1];
			}
			$DT->{item}[$itemno-1]+=$itemcount;
			push(@{$USE->{result}->{additem}},[$itemno,$itemcount]);
			push(@{$USE->{result}->{addmsg}},$item->{message});
		}
	}
	
	#市場在庫チェック＆補正
	CheckWholeStore();
	
	#アイテム別関数存在チェック
	RequireFile('inc-item.cgi');
	my $itemfunc="item::".$USE->{result}->{function};
	$itemfunc="" if !defined(&$itemfunc);
	
	#アイテム別関数呼び出し
	if($itemfunc ne '')
	{
		#変数アクセス簡便化
		@item::DT=@DT;
		$item::DTS=$DT[$USE->{arg}->{targetidx}]; #target店
		$item::count=$USE->{result}->{count};
		$item::USE=$USE;
		$item::DT=$DT;
		@item::ITEM=@ITEM;
		
		$USE->{result}->{function_return}=&$itemfunc();
	}

	#熟練度処理
	if($USE->{exp})
	{
		#熟練度プラス
		my $exp=$DT->{exp}->{$USE->{itemno}};
		$USE->{result}->{expold}=$exp+0;
		my $expplus=$USE->{exp}*$USE->{result}->{count};
		$expplus=1000-$exp if $exp+$expplus>1000;
		$DT->{exp}->{$USE->{itemno}}+=$expplus;
		
		#熟練度合計値チェック
		my $expsum=0;
		foreach(values(%{$DT->{exp}}))
		{
			$expsum+=$_;
		}
		#熟練度オーバー時減少
		if($LIMIT_EXP>0 && $expsum>$LIMIT_EXP)
		{
			$expsum-=$LIMIT_EXP;
			
			my @key=sort { $DT->{exp}{$a} <=> $DT->{exp}{$b} }keys(%{$DT->{exp}});
			my $keycnt=$#key;
			foreach(@key)
			{
				next if $_==$USE->{itemno};
				my $expdown=int($expsum/$keycnt);
				$expdown=$DT->{exp}{$_} if $DT->{exp}{$_}<$expdown;
				$DT->{exp}{$_}-=$expdown;
				delete $DT->{exp}{$_} if !$DT->{exp}{$_};
				$expsum-=$expdown;
				$keycnt--;
			}
		}
	}
}

sub MakeAmount
{
	my($cnt,$p)=@_;
	return 0 if ($p <= 0);
	return $cnt if ($p >= 1000);
	if ($cnt < 20) {
		my $i=0;
		foreach(1..$cnt) { $i++ if rand(1000)<$p; }
		return $i;
		}
	# 正規乱数
	$p = ($p / 1000);
	my $ave=$cnt*$p;
	my $sigma=$ave*(1-$p);
	my $t = (-2*$sigma*rand())*(sin(2*3.1415926535*rand()));
	return int( sqrt(($t < 0) ? -$t : $t)+$ave +0.5);
}

sub AddItem
{
	my($DT,$itemno,$count)=@_;
	
	$count=$ITEM[$itemno]->{limit}-$DT->{item}[$itemno-1] if $DT->{item}[$itemno-1]+$count>$ITEM[$itemno]->{limit};

	$DT->{item}[$itemno-1]+=$count;
	
	return $count;
}

sub GetBackUrl
{
	my($urltype,$page,$type)=split(/!/,$Q{bk} || $REFERER);
	return "" if $urltype eq 'none';
	
	my %url=(
		s	=>	"key=stock&$USERPASSURL",
		p	=>	"key=shop-b&$USERPASSURL&pg=$page",
		p2	=>	"key=shop-a&$USERPASSURL&pg=$page&t=2&itn=$type",
		m	=>	"key=shop-m&$USERPASSURL&pg=$page",
		sc	=>	"key=main&$USERPASSURL",
	);
	my $url=$url{$urltype}; $url||="key=$urltype&$USERPASSURL";
	
	return '<A HREF="action.cgi?'.$url.'">[戻る]</A>';
}

1;
