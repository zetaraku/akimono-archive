# 領主邸 2004/01/20 由來

$image[0]=GetTagImgKao("大臣","minister");
Lock();
DataRead();
CheckUserPass();

my $functionname=$Q{mode};
OutError("bad request") if !defined(&$functionname);
&$functionname;
RenewLog();
DataWrite();
DataCommitOrAbort();
UnLock();

OutSkin();
1;

sub inside
{
if ($Q{taxrate} =~ /([^0-9])/
	|| $Q{devem} =~ /([^0-9])/
	|| $Q{safem} =~ /([^0-9])/
	) { OutError('使用できる文字は半角数字だけです'); }
OutError($image[0].'いくら何でもそれは高すぎというものですぞ。') if ($Q{taxrate} > 40) ;
OutError($image[0].'一度にそれだけ対策費をつぎこんでも無意味ですぞ。') if ($Q{devem} > 10000000 || $Q{safem} > 10000000) ;

$Q{taxrate}=0 if $Q{taxrate}<0;
$Q{devem}=0 if $Q{devem}<0;
$Q{safem}=0 if $Q{safem}<0;
my $taxrate=int($Q{taxrate});
$disp.="街の内政方針を変更しました。";

if ($DTTaxrate != $taxrate )
	{
	my $i="引き上げました";
	$i="引き下げました" if $DTTaxrate > $taxrate;
	$DTTaxrate=int($Q{taxrate});
	PushLog(2,0,"領主".$DT->{name}."は街の税率を$taxrate%に$i。");
	$disp.="<br>街の税率を$taxrate%に$i。";
	}
$STATE->{devem}=int($Q{devem});
$STATE->{safem}=int($Q{safem});
}

sub outside
{
OutError('反乱中のため雇用できません。') if $DTevent{rebel};
my $stock=int($STATE->{money} / 1200);
$count=CheckCount($Q{cnt1},$Q{cnt2},0,$stock);
OutError('雇用人数を指定してください') if !$count;
$STATE->{money}-=$count * 1200;
$STATE->{army}+=$count;
$disp.="護衛軍を$count人雇いました。";
}

sub outdel
{
OutError('反乱中のため解雇できません。') if $DTevent{rebel};
$count=CheckCount($Q{cnt1},$Q{cnt2},0,$STATE->{army});
OutError('解雇人数を指定してください') if !$count;
$STATE->{army}-=$count;
$disp.="護衛軍を$count人解雇しました。";
}

sub taxside
{
OutError('対象店を選択してください。') if !defined($id2idx{$Q{tg}});
my $i=$id2idx{$Q{tg}};
if ($Q{md} eq "free")
	{
	PushLog(2,0,"領主".$DT->{name}."は".$DT[$i]->{shopname}."の税を免除しました。") if ($DT[$i]->{taxmode}!=1);
	$DT[$i]->{taxmode}=1;
	$disp.=$DT[$i]->{shopname}."の税を免除しました。";
	}
elsif ($Q{md} eq "double")
	{
	PushLog(2,0,"領主".$DT->{name}."は".$DT[$i]->{shopname}."の税率を倍にしました。") if ($DT[$i]->{taxmode}!=2);
	$DT[$i]->{taxmode}=2;
	$disp.=$DT[$i]->{shopname}."の税率を倍にしました。";
	}
	else
	{
	PushLog(2,0,"領主".$DT->{name}."は".$DT[$i]->{shopname}."の免税を取りやめました。") if ($DT[$i]->{taxmode}==1);
	PushLog(2,0,"領主".$DT->{name}."は".$DT[$i]->{shopname}."の倍税を取りやめました。") if ($DT[$i]->{taxmode}==2);
	delete $DT[$i]->{taxmode};
	$disp.=$DT[$i]->{shopname}."の税を通常に戻しました。";
	}
}

sub treset
{
foreach (@DT) {
	delete $_->{taxmode};
}
PushLog(2,0,"領主".$DT->{name}."は倍税や免税をすべて取りやめました。");
$disp.="全ての店の税率を通常に戻しました。";
}

sub expose
{
OutError('反乱中のため実行できません。') if $DTevent{rebel};
OutError('対象店を選択してください。') if !defined($id2idx{$Q{tg}});
OutError('費用が足りません。') if ($STATE->{money} < 1000000);
my $i=$id2idx{$Q{tg}};
OutError($image[0].'その店舗に対する取り締まりはあまり意味がないようですぞ。') if ($DT[$i]->{rank} < 2000) ;
$STATE->{money}-=1000000;
$DT[$i]->{rank}=int($DT[$i]->{rank} / 10);
$STATE->{safety}+=500;
$STATE->{safety}=10000 if $STATE->{safety} > 10000;
PushLog(2,0,"領主".$DT->{name}."は".$DT[$i]->{shopname}."に対して取り締まりを行いました。");
$disp.=$DT[$i]->{shopname}."に対して取り締まりを行いました。";
}

