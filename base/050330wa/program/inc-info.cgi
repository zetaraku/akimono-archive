# 店舗情報 2005/01/06 由來

$disp.="<BIG>●店舗情報</BIG><br><br>";

my $tm=$NOW_TIME-$DT->{time};
if($tm<0)
{
	$tm=-$tm;
	$tm='行動可能まであと '.GetTime2HMS($tm);
}else{
	if($tm>$MAX_STOCK_TIME){$tm=$MAX_STOCK_TIME;}
	$tm=GetTime2HMS($tm);
}
my $rankmsg=GetRankMessage($DT->{rank});

my $expsum=0;
foreach(values(%{$DT->{exp}})){$expsum+=$_;}
$expsum=int($expsum/10)."%";

my $job="すっぴん";
$job=$JOBTYPE{$DT->{job}} if ($DT->{job});

my $level=DignityDefine($DT->{dignity},2);
$level=$DIGNITY[0] if !$level;

if(!$MOBILE)
{
	my @taxmode=('','(免税)','(倍税)');
	$disp.=$TB;
	$disp.=$TR;
	$disp.="<td width=48 rowspan=2>".GetTagImgKao($DT->{name},$DT->{icon});
	$disp.="<td align=center colspan=4><SPAN>RANK ".($id2idx{$DT->{id}}+1)."</SPAN> ： ".GetTagImgGuild($DT->{guild})."<b>".$DT->{shopname}."</b>";
	$disp.="<td align=center rowspan=2>".GetTagImgJob($DT->{job},$DT->{icon}).$TRE;
	$disp.=$TR."<td width=56 class=b>爵位$TD$level <small>(経験値 ".($DT->{dignity}+0)."pt)";
	$disp.=$TDB.'ジョブ<td width=64>'.$job.$TRE;
	$disp.=$TR."<td colspan=2 class=b>点数".$TD.$DT->{point}.$TDB."資金";
	$disp.=$DT->{money}>=0 ? "<td colspan=2>".GetMoneyString($DT->{money}).$TRE : "<td colspan=2><font color=\"#cc2266\"><b>-".GetMoneyString(-$DT->{money})."</b></font>".$TRE;
	$disp.=$TR."<td colspan=2 class=b>持ち時間".$TD.$tm.$TDB."創業<td colspan=2>".GetTime2HMS($NOW_TIME-$DT->{foundation}).$TRE;
	$disp.=$TR."<td colspan=2 class=b>人気".$TD.$rankmsg.$TDB."ごみ<td colspan=2>".GetCleanMessage($DT->{trush}).$TRE;
	$disp.=$TR."<td colspan=2 class=b>今期売上".$TD.GetMoneyString($DT->{saletoday}).$TDB."前期売上<td colspan=2>\\".$DT->{saleyesterday}.$TRE;
	$disp.=$TR."<td colspan=2 class=b>今期支払".$TD.GetMoneyString($DT->{paytoday}).$TDB."前期支払<td colspan=2>\\".$DT->{payyesterday}.$TRE;
	$disp.=$TR."<td colspan=2 class=b>今期維持費<BR><SMALL>(決算時徴収)</SMALL>".$TD.GetMoneyString(int($DT->{costtoday}))."+".GetMoneyString($SHOWCASE_COST[$DT->{showcasecount}-1]);
	$disp.=   $TDB."前期維持費<td colspan=2>\\".$DT->{costyesterday}.$TRE;
	$disp.=$TR."<td colspan=2 class=b>今期売却税".$TD.GetMoneyString($DT->{taxtoday}).$TDB."前期売却税<td colspan=2>\\".($DT->{taxyesterday}+0).$TRE;
	$disp.=$TR."<td colspan=2 class=b>基本売却税率".$TD.GetUserTaxRate($DT,$DTTaxrate).'%'.$taxmode[$DT->{taxmode}+0].$TDB."熟練度合計<td colspan=2>".$expsum.$TRE;
	$disp.=$TR."<td colspan=2 class=b>優勝回数".$TD.($DT->{rankingcount}+0)."回 ".GetTopCountImage($DT->{rankingcount}+0).$TRE;
	$disp.=$GUILD{$DT->{guild}} ? $TDB."ギルド会費<br><SMALL>(決算時徴収)</SMALL><td colspan=2>\\".int($DT->{saletoday}*$GUILD{$DT->{guild}}->[$GUILDIDX_feerate]/1000)."<SMALL>/売上の".($GUILD{$DT->{guild}}->[$GUILDIDX_feerate]/10)."%</SMALL>" : $TD."　<td colspan=2>　";
	$disp.=$TRE.$TBE;
}
else
{
	$disp.="名前:".$DT->{name}."<BR>";
	$disp.="店名:".GetTagImgGuild($DT->{guild}).$DT->{shopname}."<BR>";
	$disp.="RANK:".($id2idx{$DT->{id}}+1)."<BR>";
	$disp.="人気:".$rankmsg."<BR>";
	$disp.="ごみ:".GetCleanMessage($DT->{trush})."<BR>";
	$disp.="資金:".GetMoneyString($DT->{money})."<BR>";
	$disp.="今売:".GetMoneyString($DT->{saletoday})."<BR>";
	$disp.="今払:".GetMoneyString($DT->{paytoday})."<BR>";
	$disp.="今維:".GetMoneyString(int($DT->{costtoday}))."+".GetMoneyString($SHOWCASE_COST[$DT->{showcasecount}-1])."<BR>";
	$disp.="時間:".$tm."<BR>";
	$disp.="点数:".$DT->{point}."<BR>";
	$disp.="職業:".$job."<BR>";
}
1;
