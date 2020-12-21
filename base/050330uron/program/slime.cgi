# ドラゴンレース 2005/03/30 由來

$NOITEM=1;
RequireFile('inc-dragon.cgi');
DragonLasttime();

DataRead();
CheckUserPass(1);
RequireFile("inc-dr-edit".$drlock.".cgi") if ($drlock);

$disp.=GetMenuTag('slime',		'[あきスポ]','&mode=info')
	.GetMenuTag('slime',		'[登竜レース]','&mode=rd')
	.GetMenuTag('slime',		'[重賞レース]','&mode=rd&code=1');
if (!$GUEST_USER)
	{
	$disp.=GetMenuTag('slime',		'[牧場]','&mode=ranch')
		.GetMenuTag('slime',		'[厩舎]','&mode=stable')
		.GetMenuTag('slime',		'[騎手]','&mode=jock');
	}
$disp.="<hr width=500 noshade size=1>";
$Q{mode}||="info";
RequireFile("inc-dragon-$Q{mode}.cgi");
OutSkin();
1;

sub DragonLasttime
{
undef @DRTIME;
$drlock=0;
my $fn=GetPath($COMMON_DIR,"dr-last");
if (-e $fn)
	{
	require $fn;
	$drlock=2 if ($NOW_TIME > $DRTIME[1] || $NOW_TIME > $DRTIME[2]);
	$drlock=1 if ($NOW_TIME > $DRTIME[0]);
	CoLock() if $drlock;
	}
	else
	{
	#更新時刻初期設定
	CoLock();
	foreach(0..2) { $DRTIME[$_]=$NOW_TIME + 86400 -(($NOW_TIME + $TZ_JST - $DRTIMESET[$_] * 3600) % 86400); }
	WriteDrLast();
	CoDataCA();
	CoUnLock();
	}
}

