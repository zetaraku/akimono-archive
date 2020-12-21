# 海域データアクセス 2004/02/28 由來
# ワールドアトラス仕様

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

sub ReadSeaSub
{
	my($file)=@_;
	my $filename=GetPath($SUBDATA_DIR,$file);
	open(IN,$filename);
	read(IN,my $buf,-s $filename);
	close(IN);
	my @buf=split(',',$buf);
	return @buf;
}

sub WriteSeaSub
{
	my($filename,@subdata)=@_;
	OpenAndCheck(GetPath($SUBDATA_DIR,$filename));
	print OUT join(",",@subdata);
	close(OUT);
}

sub DeleteSeaSub
{
	my($file)=@_;
	unlink (GetPath($SUBDATA_DIR,$file));
}

1;

