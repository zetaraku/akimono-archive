# ドック編成処理 2004/02/28 由來
# ワールドアトラス版

OutError("出港中の船団は編成変更できません。") if -e (GetPath($SUBDATA_DIR,$DT->{id}."-exp".$Q{ship}));

# 設定
my @SHIP=(
	[20,8,0,0,0,0,6,3,6],
	[12,20,8,0,0,0,10,5,10],
	[0,12,20,8,0,0,12,6,12],
	[0,0,12,20,8,0,14,7,14],
	[0,0,0,12,20,8,16,8,16],
	[0,0,0,0,12,20,18,9,18],
	[0,0,0,0,20,20,20,10,20],
);

# 現状での船舶保持数を計算
foreach(0..4)
	{
	next if !$subdata[$_];
	$DT->{item}[$subdata[$_]-1]++;
	}

undef @subdata;
my $csr=0;	# 書き込み位置

foreach my $num(5..11)
	{
	foreach my $cnt(1..5)
		{
		my $data=$num."_".$cnt;
		next if !$Q{$data};
		OutError("5個以上選択されています") if $scr > 4;
		$subdata[$scr]=$num;
		$scr++;
		$DT->{item}[$num-1]--;
		my @buf=@{$SHIP[$num-5]};
		foreach my $i(0..8)
			{
			$subdata[$i+5]+=$buf[$i];
			}
		}
	OutError("所持数を超えて船が選択されています") if $DT->{item}[$num-1] < 0;
	}

if (!$scr)
{
$DT->{item}[$Q{ship}-1]=0;
unlink (GetPath($SUBDATA_DIR,$DT->{id}."-abi".$Q{ship}));
}
else
{
if ($DT->{job} eq "pirate" || $DT->{job} eq "pros")
	{
	$subdata[11]*=2;
	$subdata[12]*=4;
	$subdata[13]*=2;
	}
$DT->{item}[$Q{ship}-1]=1;
WriteShipSub($DT->{id}."-abi".$Q{ship},@subdata);
}
DataWrite();
DataCommitOrAbort();
UnLock();


sub WriteShipSub
{
	my($filename,@subdata)=@_;
	OpenAndCheck(GetPath($SUBDATA_DIR,$filename));
	print OUT join(",",@subdata);
	close(OUT);
}
1;

