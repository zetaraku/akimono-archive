# 引越しセンター 2004/01/20 由來

OutError('移転が不可に設定されています') if !$MOVETOWN_ENABLE;
OutError('街コードが設定されていません') if !$TOWN_CODE;
my $townmaster=ReadTown($TOWN_CODE,'getown');
OutError('移転ルートがつながっていません') if !$townmaster;

DataRead();
CheckUserPass();

$disp.=GetTownListHTML();
OutSkin();
1;


sub GetTownListHTML
{
	my @townlist=ReadTown();
	return '<b>移転可能な街が見つかりません</b>' if !scalar(@townlist);
	
	my $ret;
	$ret.='<BIG>●他の街へ引越し</BIG><br><br>';
	$ret.=$TBT.$TRT.$TD;
	foreach(@townlist)
	{
		$ret.="<SPAN>".$_->{name}."</SPAN><br>";
		$ret.=GetTagA("[確認]","action.cgi?key=jump&town=$_->{code}",0,"_blank");
		$ret.=GetTagA("[移転手続]","action.cgi?key=move-f&$USERPASSURL&towncode=$_->{code}") if !$GUEST_USER;
		$ret.="<br>".$_->{comment}."<br><br>";
	}
	$ret.=$TRE.$TBE;
	return $ret;
}

