# お掃除 2005/01/06 由來

Lock();
DataRead();
CheckUserPass();

$time=int(GetStockTime($DT->{time})/ 3600);
$count=CheckCount($Q{cnt1},$Q{cnt2},0,$time);
OutError('時間を指定してください') if ($count < 1);
my $usetime=GetTimeDeal($DT->{trush});
$usetime=$count * 3600 if ($usetime > $count * 3600);
my $deal=$count * 3600 / $TIME_SEND_MONEY * $TIME_SEND_MONEY_PLUS;
$deal=$DT->{trush} if ($DT->{trush} < $deal);

$DT->{trush}-=$deal;
UseTime($usetime);

RequireFile('inc-html-ownerinfo.cgi');

$disp.="<BIG>●お掃除レポート</BIG><br><br>お掃除を行いました。<br><br>";
$disp.=$TB.$TR.$TD;
$disp.="<SPAN>予\定所要時間</SPAN>：".$count."時間<br>";
$disp.="<SPAN>実際かかった時間</SPAN>：".GetTime2HMS($usetime)."<br>";
$disp.="<SPAN>最初あったごみの量</SPAN>：".int(($DT->{trush}+$deal)/10000)."kg<br>";
$disp.="<SPAN>片付けたごみの量</SPAN>：".int($deal/10000)."kg<br>";
$disp.="<SPAN>残ったごみの量</SPAN>：".int($DT->{trush}/10000)."kg";
$disp.=$TRE.$TBE;

DataWrite();
DataCommitOrAbort();
UnLock();

OutSkin();
1;
