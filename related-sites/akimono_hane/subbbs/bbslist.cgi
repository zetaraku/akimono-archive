#店内掲示板一覧

$NOITEM=1;
DataRead();
CheckUserPass();
my @DTS=grep($_->{user}->{subbbs},@DT);
BBSList();
OutSkin();
1;

sub BBSList
{
	my($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
		=GetPage($Q{pg},$RANKING_PAGE_ROWS,scalar @DTS);
	
	my $pagecontrol=GetPageControl($pageprev,$pagenext,"","",$pagemax,$page);

	if(!$GUEST_USER)
	{

	$disp.=GetMenuTag('subbbs',	'[自店掲示板'.GetTime2FormatTime((stat($SUBDATA_DIR."/$DT->{id}-bbs.cgi"))[9]+0,1).']','&dts='.$DT->{id}.'&'.$USERPASSURL)
		.GetMenuTag('bbslist',	'[店内掲示板一覧]');

	$disp.="<hr width=500 noshade size=1>";
	}

	$disp.="<BIG>●店内掲示板一覧</BIG><br><br>";
	return if !scalar(@DTS);
	$disp.=$pagecontrol;
	$disp.=$TB;

	$disp.=$TR;
	$disp.=$TDB."店長";
	$disp.=$TDB."店名";
	$disp.=$TDB."最終更新";
	$disp.=$TRE;

	foreach my $DT (@DTS[$pagestart..$pageend])
	{
		$disp.=$TR.$TDNW.$tdh_pt.GetTagImgKao($DT->{name},$DT->{icon});
		$disp.=$TD;
		$disp.="<a href=\"action.cgi?key=subbbs&dts=$DT->{id}&$USERPASSURL\">" if(!$GUEST_USER);
		$disp.="<b>$DT->{shopname}</b>";
		$disp.="</a>" if(!$GUEST_USER);
		$disp.="<br>".$DT->{comment};
		$disp.=$TD;
		$disp.=GetTime2FormatTime((stat($SUBDATA_DIR."/$DT->{id}-bbs.cgi"))[9]+0,1);
		$disp.=$TRE;
	}
	$disp.=$TBE;
	$disp.=$pagecontrol;
}