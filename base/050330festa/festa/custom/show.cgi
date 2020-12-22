# 催物 2005/01/14 由來
# キャンパスフェスタ仕様

DataRead();
CheckUserPass();

my @draDT=grep($_->{user}->{pt},@DT);
@draDT=sort{$b->{user}->{pt}<=>$a->{user}->{pt}}@draDT;

ShowList();

ShowComment() if $DT->{item}[76-1];

OutSkin();
1;

sub ShowList
{
	my($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
		=GetPage($Q{pg},$RANKING_PAGE_ROWS,scalar @draDT);
	
	my $pagecontrol=GetPageControl($pageprev,$pagenext,"","",$pagemax,$page);

	%skill=qw(magic 70 show 72 obake 74);
	
	$disp.="<BIG>●学園催し物一覧</BIG><br><br>";
	return if !scalar(@draDT);
	$disp.=$pagecontrol;
	$disp.=$TB;
	foreach my $DT (@draDT[$pagestart..$pageend])
	{
		my $itemno=$skill{$DT->{job}};
		my $itemtype=-1;
		my $itempro="";
		foreach my $no (@{$DT->{showcase}})
		{
			$itemtype=0,next if $itemtype!=-1 && $ITEM[$no]->{type}!=$itemtype;
			$itemtype=$ITEM[$no]->{type};
		}
		$itempro=GetTagImgItemType(0,$itemtype,1)." " if $itemtype;
		$disp.=$TR.$TDNW.$tdh_pt.GetTagImgKao($DT->{name},$DT->{icon});
		$disp.=$TD."<b>".$itempro.$DT->{shopname}."</b><br>".$DT->{comment};
		$disp.=$TD.GetTagImgJob($DT->{job}."play",$DT->{icon});
		$disp.=$TD.GetTagImgItemType($itemno)." <SPAN>".$DT->{user}->{tt}."</SPAN><br>支持 ".GetRankMessage($DT->{user}->{pt}).$TRE;
	}
	$disp.=$TBE;
	$disp.=$pagecontrol;
}

sub ShowComment
{
return if !scalar(@draDT);
foreach (@draDT) {
$shoplist.="<OPTION VALUE=\"$_->{id}\">$_->{shopname}";
}
$disp.=<<STR;
<br>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=hidden NAME=key VALUE="show-s">
$USERPASSFORM
<BIG>●評価</BIG>： 
<SELECT NAME=tg>$shoplist</select>
 の催し物に
<SELECT NAME=md><OPTION VALUE="0">拍手
<OPTION VALUE="1">ブーイング
</select> を <INPUT TYPE=SUBMIT VALUE="送る">
</FORM>
STR
}

