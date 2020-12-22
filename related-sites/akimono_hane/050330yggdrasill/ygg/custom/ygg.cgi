# 世界樹 不思議な木を改変

RequireFile('inc-ygg.cgi');

Lock();
DataRead();
CheckUserPass();

$ygg_pt=GetTownData("yggpt");
$ygg_pt=$YGG_PT_BASE if !$ygg_pt;

$water_name=$ITEM[$YGG_USE_NO]->{name};

if($Q{mode} eq "water")
{
OutError("これ以上$water_nameを与えることはできません") if($ygg_pt>=$YGG_PT_MAX);
OutError("これ以上$water_nameを与えることはできません") if($DT->{user}->{ygg}>=$YGG_USE_MAX);
OutError("$water_nameを持っていません") if !$DT->{item}[$YGG_USE_NO-1];
OutError("時間が足りません") if(GetStockTime($DT->{time})<$YGG_USE_TIME);
PushLog(0,0,"$DT->{name}が$YGG_NAMEに水を与えました");
$ygg_pt+=int($YGG_PT_RATE);
$ygg_pt=int($YGG_PT_MAX) if($ygg_pt>$YGG_PT_MAX);
SetTownData("yggpt",$ygg_pt);
$DT->{item}[$YGG_USE_NO-1]--;
$DT->{time}+=$YGG_USE_TIME;
$DT->{user}->{ygg}++;
}

RequireFile('inc-html-ownerinfo.cgi');

$disp.="<BIG>●$YGG_NAME</BIG><br><br>";
$disp.=$TB.$TR.$TD.GetTagImgKao("案内人","guide").$TD;
$disp.="これは$HTML_TITLEに伝わる$YGG_NAMEです。<br>";

$disp.="$water_nameを与えることで生命力を回復します。<br>";
$disp.="<b>現在の生命力：$ygg_pt<b>";

$img=1;
if($ygg_pt>=$YGG_PT_NEED)
{
$img=2;
}

$disp.=qq|<td><IMG width="128" height="80" BORDER="0" SRC="$IMAGE_URL/map/tree$img.png" alt="$YGG_NAME"></td></tr></table><br>|;
$utm=GetTime2HMS($YGG_USE_TIME);
if(($DT->{item}[$YGG_USE_NO-1])&&(GetStockTime($DT->{time})>=$YGG_USE_TIME)&&($DT->{user}->{ygg}<$YGG_USE_MAX)&&($ygg_pt<$YGG_PT_MAX))
{
$disp.=GetTagImgItemType($YGG_USE_NO)."<b>$water_name残り：$DT->{item}[$YGG_USE_NO-1]$ITEM[$YGG_USE_NO]->{scale}";
$disp.=<<"HTML";
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="ygg">
<INPUT TYPE=HIDDEN NAME=mode VALUE="water">
$USERPASSFORM
<INPUT TYPE=SUBMIT VALUE="$water_nameを与える">（消費時間:$utm）</FORM></b>
HTML
}

RenewLog();
DataWrite();
DataCommitOrAbort();
UnLock();
OutSkin();
1;