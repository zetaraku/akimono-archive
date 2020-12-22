# ギルドコマンド処理 2005/01/06 由來

$NOMENU=1;
$Q{bk}=$Q{er}="gd";
my $usetime=3*60*60;

Lock();
DataRead();
CheckUserPass();
OutError('ギルドに入っていません') if !$DT->{guild};
ReadGuild();
ReadGuildData();

my $functionname=$Q{mode};
OutError('bad request') if !defined(&$functionname);
&$functionname;

WriteGuildData();
RenewLog();
DataWrite();
DataCommitOrAbort();
UnLock();
$disp.=$ret;
OutSkin();
1;

sub fund
{
$count=CheckCount($Q{cnt1},$Q{cnt2},0,$DT->{money});

OutError('寄付金額を指定してください') if !$count;
OutError('最低でも'.GetMoneyString(100000).'は自店に残しましょう') if ($DT->{money} - $count) < 100000;

$ret="ギルド「".$GUILD{$DT->{guild}}->[$GUILDIDX_name]."」に".GetMoneyString($count)."寄付";
EditGuildMoney($DT->{guild} ,$count);
$DT->{money}-=$count;
$DT->{paytoday}+=$count;
PushLog(0,0,$DT->{shopname}."がギルド「".$GUILD{$DT->{guild}}->[$GUILDIDX_name]."」に".GetMoneyString($count)."寄付しました。");
}

sub break
{
OutError('肩書きがつかないと実行できません') if (!$DT->{user}{_so_e});
OutError('時間が足りません') if GetStockTime($DT->{time})<$usetime;
UseTime($usetime);
my $tg=$Q{tg};
OutError('標的を指定してください') if !$tg;
OutError('そのギルドに対して攻撃はできません') if ($GUILD_DATA{$tg}->{money} <= $GUILD_DATA{$DT->{guild}}->{money});

$ret="ギルド「".$GUILD{$DT->{guild}}->[$GUILDIDX_name]."」のブレイク。";
my $attack=0;
my $powerdeg=$GUILD_DATA{$DT->{guild}}->{atk} - $GUILD_DATA{$tg}->{def} + int(rand(50));
$attack= int( ($GUILD_DATA{$tg}->{money} + 1000000) * $powerdeg / 1600) if ($powerdeg > 0);

$GUILD_DATA{$DT->{guild}}->{atk}=int($GUILD_DATA{$DT->{guild}}->{atk} *9 /10);
$GUILD_DATA{$tg}->{def}=int($GUILD_DATA{$tg}->{def} *4 /5);

$ret.="しかし「".$GUILD{$tg}->[$GUILDIDX_name]."」は防御！",PushLog(2,0,$ret),return if (!$attack);

$ret.="「".$GUILD{$tg}->[$GUILDIDX_name]."」から".GetMoneyString($attack)."を奪取！";
EditGuildMoney($tg ,-$attack);
PushLog(2,0,$ret);

$income=int($attack / 10) + 1000;
$attack=int($attack * 9 / 10);
EditGuildMoney($DT->{guild} ,$attack);
$DT->{money}+=$income;
$DT->{saletoday}+=$income;
PushLog(0,$DT->{id},"ブレイク成功の報奨金として".GetMoneyString($income)."入手。");
$ret.="<br>ブレイク成功の報奨金として".GetMoneyString($income)."入手。";
if ($GUILD_DATA{$tg}->{money} < 0)
	{
	unlink($COMMON_DIR."/".$tg.".pl") ;
	$GUILD_DATA{$DT->{guild}}->{def}=int($GUILD_DATA{$DT->{guild}}->{def} * 3 / 2);
	$GUILD_DATA{$DT->{guild}}->{def}=1000 if ($GUILD_DATA{$DT->{guild}}->{def} > 1000);
	}
}

sub force
{
my $checkok;
$ckeckok=1 if ($GUILD_DETAIL{$DT->{guild}}->{leadt} eq $MYDIR && $GUILD_DETAIL{$DT->{guild}}->{leader} == $DT->{id});
$ckeckok=1 if ($GUILD_DETAIL{$DT->{guild}}->{$MYDIR} == $DT->{id});
OutError('bad request') if (!$ckeckok);
OutError('肩書きがつかないと実行できません') if (!$DT->{user}{_so_e});
OutError('時間が足りません') if GetStockTime($DT->{time})<$usetime;
UseTime($usetime);
OutError('増強の必要がありません') if ($GUILD_DATA{$DT->{guild}}->{atk} > 990);
my $guild=$GUILD_DATA{$DT->{guild}};
my $cnt=int($guild->{money} / 4);
$guild->{money} -= $cnt;
$guild->{atk} += int($cnt/25000);
$guild->{atk} = 1000 if $guild->{atk} > 1000;
$ret = "ギルド「".$GUILD{$DT->{guild}}->[$GUILDIDX_name]."」が軍備を増強しました。";
PushLog(0,0,$ret);
}

