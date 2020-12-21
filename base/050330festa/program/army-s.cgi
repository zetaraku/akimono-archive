# 兵士雇用反乱処理 2005/01/06 由來

$NOMENU=1;
Lock();
DataRead();
CheckUserPass();
ReadArmy();

my $functionname=$Q{mode};
OutError("bad request") if !defined(&$functionname);
&$functionname;

WriteArmy();
RenewLog();
DataWrite();
DataCommitOrAbort();
UnLock();

$disp.=$TBT.$TRT.$TD.GetTagImgJob($DT->{job},$DT->{icon});
$disp.=$TD.GetMenuTag('army',	'[傭兵所へ]');
$disp.=GetMenuTag('main','[自店に戻る]');
$disp.=$TRE.$TBE;
$disp.="<br>".$ret;
OutSkin();
1;


sub plus
{
my $limit=($DT->{dignity}+0)*1000 - $ARMY{$DT->{id}};
my $price=($DTevent{rebel}) ? 1500 : 1000;
my $usetime=60*40;
UseTime($usetime);

$num=CheckCount($Q{cnt1},$Q{cnt2},0,$limit);
OutError('数量を指定してください。') if !$num;

$num=int($DT->{money}/$price) if $DT->{money}<$num*$price;
$num=0 if $num<0;
OutError('資金が足りません。') if !$num;

$ARMY{$DT->{id}}+=$num;
$DT->{money}-=$num*$price;

$ret="兵士駐屯所にてドワーフ兵士を".$num."人@".GetMoneyString($price)."(計".GetMoneyString($price*$num).")にて雇いました";
$ret.="/".GetTime2HMS($usetime)."消費";
PushLog(0,$DT->{id},$ret);
}

sub fire
{
$num=CheckCount($Q{cnt1},$Q{cnt2},0,$ARMY{$DT->{id}});
OutError('数量を指定してください。') if !$num;

my $usetime=60*10;
UseTime($usetime);
$ARMY{$DT->{id}}-=$num;

$ret="ドワーフ兵士を".$num."人解雇しました";
$ret.="/".GetTime2HMS($usetime)."消費";
PushLog(0,$DT->{id},$ret);
}

sub rebelon
{
OutError('反乱を開始するには rebel と入力してください。') if ($Q{cmd} ne "rebel");
OutError('兵士数が足りません。') if ($ARMY{$DT->{id}} < 2500);

my $usetime=60*30;
UseTime($usetime);
$DTevent{rebel}=$NOW_TIME+86400*3;
$RIOT{$DT->{id}}=1;
$STATE->{safety}=int($STATE->{safety} * 9 / 10) if ($STATE->{safety} > 5000);

$ret="ドワーフ兵士が武装蜂起。反乱が始まりました！";
PushLog(2,0,$DT->{shopname}."の指揮で".$ret);
$ret.="/".GetTime2HMS($usetime)."消費";
}

sub rside
{
OutError('反乱に呼応するには rebel と入力してください。') if ($Q{cmd} ne "rebel");

my $usetime=60*20;
UseTime($usetime);
$RIOT{$DT->{id}}=1;

$ret="反乱に呼応し，参戦しました！";
PushLog(3,0,$DT->{shopname}."が".$ret);
$ret.="/".GetTime2HMS($usetime)."消費";
}

sub lside
{
OutError('反乱に参加しながら領主の味方をすることはできません。') if ($RIOT{$DT->{id}});

my $usetime=60*20;
UseTime($usetime);
if ($STATE->{leader}==$DT->{id})
	{
	$STATE->{army}+=$ARMY{$DT->{id}};
	}
	else
	{
	$STATE->{robina}+=$ARMY{$DT->{id}};
	PushLog(3,0,$DT->{shopname}.'は領主に味方し，義勇兵を派遣しました。');
	}

delete $ARMY{$DT->{id}};
$ret="兵士を領主の護衛軍に派遣しました";
$ret.="/".GetTime2HMS($usetime)."消費";
}
