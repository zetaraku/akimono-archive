# 荘園種買取処理 2005/03/30 由來

$NOITEM=1;
$NOMENU=1;
Lock();
DataRead();
CheckUserPass();
OutError("領主がいないので荘園制度が機能していません") if !defined($id2idx{$STATE->{leader}});
RequireFile('inc-manor.cgi');

	# 荘園設定を取得
	my $id=$id2idx{$STATE->{leader}};
	ReadDTSub($DT[$id],"lord");
	my $MANORLORD=$DT[$id]->{_lord};

	ReadDTSub($DT,"seed");

foreach my $i(0..$#MANOR)
	{
	my @MYMANOR=@{$MANOR[$i]};
	my $stock=$DT->{_seed}->{"ripe$i"};
	next if !$stock;
	my $price=$MANORLORD->{"cost$i"};

	delete $DT->{_seed}->{"ripe$i"};
	$DT->{money}+=$stock*$price;
	$DT->{saletoday}+=$stock*$price;

	$MANORLORD->{"stock$i"}+=$stock;
	$STATE->{money}-=$stock*$price;
	$STATE->{out}+=$stock*$price;
	$STATE->{develop}+=$stock;
	$STATE->{develop}=10000 if $STATE->{develop} > 10000;
	OutError("街の資金が足りないので買い取れません") if ($STATE->{money} < 0);

	my $ret=$MYMANOR[2]."を".$stock.'個@'.GetMoneyString($price)."(計".GetMoneyString($price*$stock).")にて荘園に売却";
	$disp.=$ret."<br>";
	PushLog(0,$DT->{id},$ret);
	}

	WriteDTSub($DT[$id],"lord");
	WriteDTSub($DT,"seed");
RenewLog();
DataWrite();
DataCommitOrAbort();
UnLock();
OutSkin();
1;
