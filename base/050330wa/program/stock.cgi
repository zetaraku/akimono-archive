# 倉庫 2005/01/06 由來

DataRead();
CheckUserPass();

$MENUSAY=GetMenuTag('log','[新聞]')
	.GetMenuTag('shop-a',	'[商店通りへ]')
	.GetMenuTag('shop-m',	'[市場へ]')
	.GetMenuTag('main',	'[店内に戻る]');

RequireFile('inc-html-ownerinfo.cgi');

if ($DT->{trush} > 5000000)
	{
	$disp.="<BIG>●倉庫</BIG><br><br>";
	$disp.=$TB.$TR.$TD.GetTagImgKao("お手伝い","help").$TD;
	$disp.="<SPAN>お手伝い</SPAN>：商品がごみの中にうずもれていて，見つけられません。";
	$disp.="<br>先にお掃除して，ごみを片付けましょう。".$TRE.$TBE;
	$disp.="<br>".GetMenuTag('sweep','[お掃除へ]');
	OutSkin();
	exit;
	}

my $tp=$Q{tp};
my $pg=$Q{pg};

my $DTitem=$DT->{item};
my $DTitemtoday=$DT->{itemtoday};
my $DTitemyesterday=$DT->{itemyesterday};
my $DTexp=$DT->{exp};

foreach my $no(1..$MAX_ITEM)
{
	$ITEM=$ITEM[$no];
	next if (!$DTitem->[$no-1] && !$DTitemtoday->{$no} && !$DTexp->{$no});
	if ($ITEM->{flag}=~/s/)	# s 陳列不可
	{
	$itema{$no}=$ITEM;
	}
	else
	{
	next if ($ITEM->{type} != $tp)&&($tp != 0);;
	$itemb{$no}=$ITEM;
	}
}

GetMarketStatus();

my %showcase=();
my $itemno;
foreach(0..$DT->{showcasecount}-1)
{
	next if !($itemno=$DT->{showcase}[$_]);
	$showcase{$itemno}.="棚".($_+1).GetMoneyString($DT->{price}[$_])." ";
}

if(%itema)
{
	$disp.="<BIG>●保管倉庫</BIG><br><br>";
	$disp.=$TB;
	if($MOBILE)
	{
		$tdh_sp="標準:";
		$tdh_cs="維持:";
		$tdh_st="在庫:";
		$tdh_ex="熟練:";
	}
	else
	{
		$disp.=$TR.$TDB.
			join($TDB,
				qw(
					名称
					標準価格
					維持費
					数量<small>/最大</small>
					熟練
				)
			).$TRE;
	}
	
	foreach my $ITEM (sort{$a->{sort} <=> $b->{sort}} values(%itema))
	{
		my $cnt=$ITEM->{no};
		my $name=GetTagImgItemType($cnt).$ITEM->{name};
		$name="<A HREF=\"action.cgi?key=item&no=$cnt&bk=s&$USERPASSURL\">".$name."</A>" if $DTitem->[$cnt-1];
		
		$disp.=$TR.$TD.
			join($TD,
				$name,
				$tdh_sp.GetMoneyString($ITEM->{price}),
				$tdh_cs.GetMoneyString($ITEM->{cost}),
				$tdh_st.$DTitem->[$cnt-1]."<small>/".$ITEM->{limit}."</small>",
				$tdh_ex.($DTexp->{$cnt} ? int($DTexp->{$cnt}/10)."%" : '　'),
			);
	}
	$disp.=$TBE."<hr width=500 noshade size=1>";
}

$disp.="<BIG>●販売倉庫</BIG><br><br>";
foreach my $cnt (0..$#ITEMTYPE)
{
	$disp.=$cnt==$tp ? "[" : "<A HREF=\"action.cgi?key=stock&$USERPASSURL&tp=$cnt\">";
	$disp.=GetTagImgItemType(0,$cnt) if $cnt && !$MOBILE;
	$disp.=$ITEMTYPE[$cnt];
	$disp.=$cnt==$tp ? "]" :"</A>";
	$disp.=" ";
}

if(!%itemb)
{
	$disp.="<hr width=500 noshade size=1>在庫がありません";
}
else
{
	$disp.=$TB;
	if($MOBILE)
	{
		$tdh_sp="標準:";
		$tdh_cs="維持:";
		$tdh_ts="本昨売:";
		$tdh_ex="熟練:";
		$tdh_sc="陳列:";
		$tdh_mp="相場:";
		$tdh_mb="需給:";
	}
	else
	{
		$disp.=$TR.$TDB.
			join($TDB,
				qw(
					名称
					標準価格
					維持費
					数量<small>/最大</small>
					売上数<small>/前期</small>
					熟練
					陳列
					販売相場
					需要供給バランス
				)
			).$TRE;
	}
	
	foreach my $ITEM (sort{$a->{sort} <=> $b->{sort}} values(%itemb))
	{
		my $cnt=$ITEM->{no};
		my $name=GetTagImgItemType($cnt).$ITEM->{name};
		$name="<A HREF=\"action.cgi?key=item&no=$cnt&bk=s&$USERPASSURL\">".$name."</A>" if $DTitem->[$cnt-1];
		
		$disp.=$TR.$TD.
			join($TD,
				$name,
				$tdh_sp.GetMoneyString($ITEM->{price}),
				$tdh_cs.GetMoneyString($ITEM->{cost}),
				$tdh_st.$DTitem->[$cnt-1]."<small>/".$ITEM->{limit}."</small>",
				$tdh_ts.($DTitemtoday->{$cnt} || $DTitemyesterday->{$cnt} ? ($DTitemtoday->{$cnt}||0)."<small>/".($DTitemyesterday->{$cnt}||0)."</small>" : '　'),
				$tdh_ex.($DTexp->{$cnt} ? int($DTexp->{$cnt}/10)."%" : '　'),
				$tdh_sc.($showcase{$cnt}||'　'),
				$tdh_mp.($ITEM->{marketprice} ? GetMoneyString($ITEM->{marketprice}) : '　'),
			);
		$disp.=$TDNW.$tdh_mb.GetMarketStatusGraph($ITEM->{uppoint}||=10).$TRE;
	}
	$disp.=$TBE;
}
OutSkin();
1;
