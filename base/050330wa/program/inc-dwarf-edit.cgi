# 宅配便編集 2005/03/30 由來

my $functionname=$Q{mode};
OutError("bad request") if !defined(&$functionname);
&$functionname;

WriteDwarf();
DataCommitOrAbort();
UnLock();
1;


sub new
{
	my ($to,$item)=($Q{to},$Q{item});
	OutError("宛先を指定してください。") if $to==-1;
	OutError("自分自身に宅配便を出すことはできません。") if ($to == $DT->{id});
	if ($to==99)
		{
		OutError("貿易がつながっていないので指定できません。") unless -e "trade.cgi";
		$Q{notice}=0;
		}
		else
		{
		OutError("存在しない店舗です。") if !defined($id2idx{$to});
		}
	OutError("アイテムの指定が不正です。") if !$ITEM[$item]->{name};
	OutError("アイテムの指定が不正です。") if $ITEM[$item]->{flag}=~/r/;	# r 依頼不可

	$Q{num}||=$DT->{item}[$item-1];
	$Q{num}=CheckCount($Q{num},0,0,$DT->{item}[$item-1]);
	OutError("アイテムの在庫がありません。") if !$Q{num};
	my $price=CheckCount($Q{price},0,0,$MAX_MONEY);
	$price=$price * $Q{num} if $Q{unit};
	OutError("料金を指定してください。") if !$price;
	my $numrate=$ITEM[$item]->{price} * $Q{num};
	OutError("商品と料金の価値がつりあっていません。") if ($price > $numrate * 2) || ($numrate > $price * 2);

	NoticeDwarf() if $Q{notice};

	@DWF=reverse(@DWF);
	$Dcount++;
	my $i=$Dcount;
	$DWF[$i]->{no}=($i > 0) ? ($DWF[$i-1]->{no} + 1) : 1;
	$DWF[$i]->{tm}=$NOW_TIME;
	$DWF[$i]->{from}=$DT->{id};
	$DWF[$i]->{to}=$to;
	$DWF[$i]->{trade}=(($to==99) ? $DWF[$i]->{no} : "");
	$DWF[$i]->{mode}=1;
	($DWF[$i]->{item},$DWF[$i]->{num},$DWF[$i]->{price})=($item,$Q{num},$price);
	@DWF=reverse(@DWF);

	$DT->{item}[$item-1]-=$Q{num};

	my $cost=0;
	$cost=int($price * $DTTaxrate / 100);
	OutError("税金を払うことができません。") if ($cost > $DT->{money});
	$DT->{taxtoday}+=$cost;
	$DT->{money}-=$cost;

	DataWrite();
	$Q{form}="";
}

sub plus
{
	if ($Q{ng})
	{
		# 受け取り拒否
		foreach my $i(0..$Dcount)
		{
		next unless $DWF[$i]->{to}==$DT->{id};
		next unless $DWF[$i]->{mode}==1;
		my $act="act_".$DWF[$i]->{no};
		$DWF[$i]->{mode}=3 , next if ($Q{$act});
		}
		return;
	}

	# 受け取り
	foreach my $i(0..$Dcount)
	{
	next unless $DWF[$i]->{to}==$DT->{id};
	next unless $DWF[$i]->{mode}==1;
	my $act="act_".$DWF[$i]->{no};
	next unless ($Q{$act});
	$DWF[$i]->{mode}=2;
	my ($price,$from,$item,$num)=($DWF[$i]->{price},$DWF[$i]->{from},$DWF[$i]->{item},$DWF[$i]->{num});
	$DT->{paytoday}+=$price;
	$DT->{money}-=$price;
	$DT[$id2idx{$from}]->{money}+=$price;
	$DT[$id2idx{$from}]->{saletoday}+=$price;
	$DT->{item}[$item-1]+=$num;
	$DT->{item}[$item-1]=$ITEM[$item]->{limit} if ($DT->{item}[$item-1]>$ITEM[$item]->{limit});
	}
	OutError("代金を支払うのに必要な資金が足りません。") if ($DT->{money} < 0);
	DataWrite();
}

sub trade
{
	OutError("貿易がつながっていないので指定できません。") unless -e "trade.cgi";
	OutError("貿易品を指定してください。") if !defined($Q{code});

	my($boxno,$item,$num,$price)=split(/:/,$Q{code});
	OutError("アイテムの指定が不正です。") if !$ITEM[$item]->{name};
	OutError("アイテムの指定が不正です。") if $ITEM[$item]->{flag}=~/r/;	# r 依頼不可

	$num=CheckCount($num,0,0,$MAX_MONEY);
	OutError("個数の指定が不正です。".$num) if !$num;
	$price=CheckCount($price,0,0,$MAX_MONEY);
	OutError("料金の指定が不正です。") if !$price;
	OutError("資金を準備しておいてください。") if $price > $DT->{money};
	OutError("その貿易品はすでに売約済です。") if grep($_->{trade} eq $boxno,@DWF);

	@DWF=reverse(@DWF);
	$Dcount++;
	my $i=$Dcount;
	$DWF[$i]->{no}=($i > 0) ? ($DWF[$i-1]->{no} + 1) : 1;
	$DWF[$i]->{tm}=$NOW_TIME;
	$DWF[$i]->{from}=99;
	$DWF[$i]->{to}=$DT->{id};
	$DWF[$i]->{trade}=$boxno;
	$DWF[$i]->{mode}=0;
	($DWF[$i]->{item},$DWF[$i]->{num},$DWF[$i]->{price})=($item,$num,$price);
	@DWF=reverse(@DWF);
}

sub delete
{
	$WriteMode=0;
	foreach my $i(0..$Dcount)
	{
	next unless $DWF[$i]->{from}==$DT->{id};
	my $act="del_".$DWF[$i]->{no};
	next unless ($Q{$act});
	if ($DWF[$i]->{mode}!=2)	# 受取済みなら返却の必要なし
		{
		$WriteMode=1;
		my ($item,$num)=($DWF[$i]->{item},$DWF[$i]->{num});
		$DT->{item}[$item-1]+=$num;
		$DT->{item}[$item-1]=$ITEM[$item]->{limit} if ($DT->{item}[$item-1]>$ITEM[$item]->{limit});
		}
	undef $DWF[$i];
	}
	DataWrite() if $WriteMode;
}

sub WriteDwarf
{
	undef @RECDWF;	# 保存と再定義を同時に
	undef @SENDWF;
	$NeverD=0;
	my @buf;
	foreach my $i(0..$Dcount)
		{
		next unless defined($DWF[$i]->{no});
		$buf[$i]=join(",",map{$DWF[$i]->{$_}}@DWFnamelist)."\n";
		if ($DWF[$i]->{to}==$DT->{id})
			{
			push(@RECDWF, $i);
			$NeverD++ if $DWF[$i]->{mode}==1;
			}
		push(@SENDWF, $i) if ($DWF[$i]->{from}==$DT->{id});
		}
	OpenAndCheck(GetPath($TEMP_DIR,"dwarf"));
	print OUT @buf;
	close(OUT);
}

sub NoticeDwarf
{
	ReadLetter();

	@LETTER=reverse(@LETTER);
	$Lcount++;
	my $i=$Lcount;
	$LETTER[$i]->{no}=($i) ? ($LETTER[$i-1]->{no} + 1) : 1 ;
	$LETTER[$i]->{time}=$NOW_TIME;
	$LETTER[$i]->{fromt}=$MYDIR;
	$LETTER[$i]->{fromid}=1;
	$LETTER[$i]->{tot}=$MYDIR;
	$LETTER[$i]->{toid}=$Q{to};
	$LETTER[$i]->{title}="宅配便到着のお知らせ";
	$LETTER[$i]->{msg}="こちらドワーフ宅配便です。".$DT->{shopname}."さんより，小包が届けられましたので，ご確認をお願いいたします。";
	$LETTER[$i]->{mode}=1;	#未読設定
	$LETTER[$i]->{other}=$DT->{shopname};
	@LETTER=reverse(@LETTER);

	WriteLetter();
	CoDataCA();
	CoUnLock();
}

