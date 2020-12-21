# ドワーフ宅配便 2004/01/20 由來

$image[0]=GetTagImgKao("住み込みドワーフ","dwarf");
$Q{mode}='new',  if ($Q{form} eq "make")&&($Q{ok}); 	# 送信モード切替

Lock() if $Q{mode};
CoLock() if $Q{mode}&&$Q{notice};
DataRead();
CheckUserPass();

@DWFnamelist=qw(
		no tm from to item num price mode trade
		);
ReadDwarf() unless ($Q{trade});

RequireFile('inc-dwarf-edit.cgi') if ($Q{mode});	# 各種処理

if ($Q{form})
{
RequireFile('inc-dwarf-form.cgi');
}
elsif ($Q{trade})
{
RequireFile('inc-dwarf-trade.cgi');
}
else
{
RequireFile('inc-dwarf.cgi');
}

OutSkin();
1;


sub ReadDwarf
{
	undef @RECDWF;
	undef @SENDWF;
	undef @DWF;
	$NeverD=0;
	open(IN,GetPath("dwarf")) or return;
	my @dwf=<IN>;
	close(IN);
	$Dcount=$#dwf;
	return if $Dcount < 0;
	foreach my $cnt(0..$Dcount)
		{
		chop $dwf[$cnt];
		my @buf=split(/,/,$dwf[$cnt]); my $i=0;
		foreach (@DWFnamelist) { $DWF[$cnt]->{$_}=$buf[$i];$i++;}
		undef $DWF[$cnt],next if ($DWF[$cnt]->{tm}+$BOX_STOCK_TIME < $NOW_TIME);	# 期限切れを削除。
		if ($DWF[$cnt]->{to}==$DT->{id})
		{
		push(@RECDWF, $cnt);
		$NeverD++ if $DWF[$cnt]->{mode}==1;
		}
		push(@SENDWF, $cnt) if ($DWF[$cnt]->{from}==$DT->{id});
	}
}

sub SearchDwarfIndex
{
	my($no)=@_;
	foreach(0..$Dcount)
		{
		return $_ if ($no==$DWF[$_]->{no});
		}
	return -1;
}

