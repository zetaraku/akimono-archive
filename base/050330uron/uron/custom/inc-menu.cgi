# メニュー設定ファイル 2005/03/30 由來

# メニューに表示させるリストを設定できます。
# 最初の一行が「メニュー項目名」，
# 次の行からは「サブメニュー名」，「プログラム名」です。
#   ※プログラム名にはアドレスも指定可能です。

my @MENU=(
	# ゲスト権限の場合のメニュー
	['街案内',[
		['風景',	'town'],
		['新聞',	'log'],
		['図書館',	'action.cgi?key=library',	"_blank"],
	]],

	# 以下プレイヤー権限の場合のメニュー
	['自店',[
		['店内',	'main'],
		['倉庫',	'stock'],
		['お掃除',	'sweep'],
		['収支',	'balance'],
		['手続',	'other'],
		['LogOut',	'index.cgi'],
	]],
	['取引',[
		['市場',	'shop-m'],
		['商店通り',	'shop-a'],
		['依頼所',	'req'],
		['宮殿',	'palace'],
	]],
	['情報',[
		['風景',	'town'],
		['新聞',	'log'],
		['殿堂',	'orilist'],
		['図書館',	'action.cgi?key=library',	"_blank"],
	]],
	['施設',[
		['領主邸',	'lord'],
		['ギルド',	'gd'],
		['競技場',	'slime'],
		['傭兵所',	'army'],
		['住宅地',	'hometown'],
	]],
	['交流',[
		['郵便局',	'letter'],
		['宅配便',	'dwarf'],
		['掲示板 '.GetTime2FormatTime((stat($COMMON_DIR.'/treelog.cgi'))[9]+0,1),	'treebbs'],
		['wis',	'wis'],
	]],
);

# 以下はプログラムです。編集するには技術が必要です。------------------------------

my $now=$DTlasttime+$TZ_JST-$DATE_REVISE_TIME;
my $nextday=$now+$ONE_DAY_TIME-($now % $ONE_DAY_TIME);
$DISP{MENU} =~ s/#SKINMENUTITLE#/$TOWN_TITLE/;

if($USER && $USER ne 'soldoutadmin')
	{
	$DISP{MENU} =~ s/#SKINJOB#/GetTagImgJob($DT->{job},$DT->{icon})/e;
	my $i;
	my $MENUMSG;
	my $file=GetPath($SUBDATA_DIR,$DT->{id}."-wis");
	$MENUMSG.=<<"STR";
<i id="lay"></i>
<SCRIPT LANGUAGE="JavaScript">
<!--
menudata=[
STR
	$MENUMSG.="'";
	$MENUMSG.=(-e $file) ? WisRead($file) : "<BIG>活動中</BIG> &gt; <small>".LoginMember()."</small>";
	$MENUMSG.="',";
	foreach(1..$#MENU)
		{
		my $msg=@{$MENU[$_]}[0];
		my @list=@{@{$MENU[$_]}[1]};
		$i.=qq|<A href="javascript:mymenu($_)">【$msg】</A> |;
		$MENUMSG.="'";
		$MENUMSG.="<BIG>$msg</BIG> &gt; ";
		foreach my $sublist(@list)
			{
			my @SUBMENU=@{$sublist};
			$MENUMSG.=(($SUBMENU[1] =~ /\./) ? GetTagA("[".$SUBMENU[0]."]",$SUBMENU[1],0,$SUBMENU[2]) : GetMenuTag($SUBMENU[1],"[".$SUBMENU[0]."]"));
			}
		$MENUMSG.=qq|<A href="javascript:mymenu(0)">【×】</A> |;
		$MENUMSG.="',";
		}
	$MENUMSG.=<<"STR";
];
function mymenu(i){
document.getElementById("lay").innerHTML = menudata[i];
}
mymenu(0);
// -->
</SCRIPT>
STR
	$i.=qq|<A HREF="action.cgi?key=bgm&$USERPASSURL&mode=$Q{key}" target="_top">[♪]</a> |;
	$i.='[次回決算 '.GetTime2FormatTime($nextday-$TZ_JST+$DATE_REVISE_TIME).' まであと'.GetTime2HMS(int(($nextday-$now)/60)*60+59).']';
	$DISP{MENU} =~ s/#SKINMENU#/$i/;
	$DISP{MENU} =~ s/#SKINMENUSUB#/$MENUMSG/;
	}
	else
	{
	$DISP{MENU} =~ s/#SKINTITLE#/$HTML_TITLE/;
	$DISP{MENU} =~ s/#SKINJOB#/GetTagImgJob("guest",0)/e;
	my $i;
	my $MENUMSG;
	my $msg=@{$MENU[0]}[0];
	my @list=@{@{$MENU[0]}[1]};
	$MENUMSG.=qq|<BIG>$msg</BIG> > |;
	foreach my $sublist(@list)
		{
		my @SUBMENU=@{$sublist};
		$MENUMSG.=(($SUBMENU[1] =~ /\./) ? GetTagA("[".$SUBMENU[0]."]",$SUBMENU[1],0,"_blank") : GetMenuTag($SUBMENU[1],"[".$SUBMENU[0]."]"));
		}
	$i.=($MYNAME eq 'index.cgi')? qq|<A HREF="$HOME_PAGE" TARGET=_top>[ホーム]</A> | : qq|<A HREF="index.cgi" TARGET=_top>[トップ]</A> |;
	$i.='[次回決算 '.GetTime2FormatTime($nextday-$TZ_JST+$DATE_REVISE_TIME).' まであと'.GetTime2HMS(int(($nextday-$now)/60)*60+59).']';
	$DISP{MENU} =~ s/#SKINMENU#/$i/;
	$DISP{MENU} =~ s/#SKINMENUSUB#/$MENUMSG/;
	}
print $DISP{MENU};
1;


sub LoginMember
{
my $logmemb="";
my $i=0;
foreach(@DT)
	{
	next if ($_->{lastlogin} < $NOW_TIME - 120);
	$logmemb .= "， ".$_->{shopname};
	$i++;
	$logmemb .= "ほか", last if ($i > 3);
	}
$logmemb = substr($logmemb,3) if ($logmemb);
$logmemb = "なし" if !$logmemb;
return $logmemb
}

sub WisRead
{
	my ($file)=@_;
	open(IN,$file) or return;
	read(IN,my $buf,-s $file);
	close(IN);
	unlink $file;
	return $buf;
}

