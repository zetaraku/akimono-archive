# ギルド下請け 2004/02/28 由來

ReadGuild();
ReadGuildData();

$image[0]=GetTagImgKao("ギルド受付","guild");
$disp.=GetMenuTag('gd','[ギルド一覧]');
if (!$GUEST_USER && !$DT->{guild})
	{
	$disp.=GetMenuTag('gd-m','[入団手続]');
	$disp.=GetMenuTag('gd-f','[結成宣言]');
	$disp.='<hr width=500 noshade size=1>';
	}

if ($DT->{guild})
	{
	$disp.=GetMenuTag('gd-bbs','[作戦室 '.GetTime2FormatTime((stat($COMMON_DIR.'/bbslog-'.$DT->{guild}.'.cgi'))[9]+0,1).']');
	$disp.=GetMenuTag('gd-i','[探偵室]','&cmd=info');
	if ($GUILD_DETAIL{$DT->{guild}}->{leadt} eq $MYDIR && $GUILD_DETAIL{$DT->{guild}}->{leader} == $DT->{id})
		{
		$disp.=GetMenuTag('gd-f','[執務室]');
		$disp.=GetMenuTag('gd-e','[人事室]','&mode=submit');
		$disp.=GetMenuTag('gd-m','[入団許可]','&mode=submit');
		}
		else
		{
		if ($GUILD_DETAIL{$DT->{guild}}->{$MYDIR} == $DT->{id})
			{
			$disp.=GetMenuTag('gd-e','[人事室]','&mode=submit');
			$disp.=GetMenuTag('gd-m','[入団許可]','&mode=submit');
			}
		$disp.=GetMenuTag('gd-e','[退団手続]','&mode=leave');
		}
	$disp.='<hr width=500 noshade size=1>';
	}
$disp.="<BIG>●ギルド公館</BIG><br><br>";
1;

