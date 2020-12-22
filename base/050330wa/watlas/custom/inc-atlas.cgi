# アトラスの更新 2004/02/28 由來
# ワールドアトラス仕様


foreach my $data(1..6)
{
	ReadSea($data);
	next if $Townnum < 1;
	$Civ=int($Civ - ($Civ / 12) - rand(5));
	$Civ=0 if ($Civ < 0);
	$Pro=int($Pro - ($Pro / 12) - rand(5));
	$Pro=0 if ($Pro < 0);
	foreach(1..$Townnum)
	{
	my($date,$name,$other)=split(',',$SEA[$_],3);
	next if $date > $NOW_TIME;
	$SEA[$_]="";
	PushLog(2,0,"都市$nameは，産物が底を突き交易価値を失いました。");
	}
	WriteSea($data);
}


sub ReadSea
{
	my($filenum)=@_;
	undef @SEA;
	$Civ=$Pir=$Pro=$Townnum=0;
	open(IN,GetPath("sea$filenum")) or return;
	@SEA=<IN>;
	close(IN);
	($Civ,$Pir,$Pro)=split(',',$SEA[0]);
	chop($Pro);
	$Townnum=scalar(@SEA) - 1;
}

sub WriteSea
{
	my($filenum)=@_;
	$SEA[0]="$Civ,$Pir,$Pro\n";
	OpenAndCheck(GetPath($TEMP_DIR,"sea$filenum"));
	print OUT @SEA;
	close(OUT);
}

1;

