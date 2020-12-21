# 催物評価処理 2005/01/14 由來
# キャンパスフェスタ仕様

Lock();
DataRead();
CheckUserPass();

ShowBoo();
RenewLog();
DataWrite();
DataCommitOrAbort();
UnLock();

OutSkin();
1;

sub ShowBoo
{
OutError('対象店を選択してください。') if !defined($id2idx{$Q{tg}});
OutError('招待状がないと催し物の評価はできません。') if !($DT->{item}[76-1]);
$DT->{item}[76-1]--;
my $cnt=100;
$cnt=-$cnt if ($Q{md});

my @draDT=grep($_->{user}->{pt},@DT);
foreach my $DT (@draDT)
	{
	if ($DT->{id}==$Q{tg})
		{
		$DT->{user}->{pt}+=$cnt;
		PushLog(0,0,$DT->{shopname}."の催し物に".($Q{md} ? "ブーイング" : "拍手")."が送られました。");
		$disp.=$DT->{shopname}."の催し物に".($Q{md} ? "ブーイング" : "拍手")."を送りました。";
		}
		else
		{
		$DT->{user}->{pt}-=int(($DT->{user}->{pt} - 4000) / 10) if $DT->{user}->{pt} > 4000 && !$Q{md};
		$DT->{user}->{pt}-=int($cnt / scalar(@draDT));
		}
	$DT->{user}->{pt}=10000 if $DT->{user}->{pt} > 10000;
	$DT->{user}->{pt}=1 if $DT->{user}->{pt} < 1;
	}
}

