# 宅配便リスト表示 2005/01/06 由來

$disp.="<b>[宅配便リスト]</b> "
	.GetMenuTag('dwarf',		'[宅配便を出す]','&form=make');
$disp.=GetMenuTag('dwarf','[貿易品リスト]','&trade=list') if -e "trade.cgi";
$disp.="<hr width=500 noshade size=1>";

if (!$NeverD)
	{
	$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>住み込みドワーフ</SPAN>：ドワーフ宅配便は由緒ある組織じゃ。<br>
ワシに頼んでくれれば，いつでも商品を送り届けるぞい。
$TRE$TBE<br>
HTML
	}
	else
	{
	$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>住み込みドワーフ</SPAN>：新しく $NeverD包の宅配便が届いているぞ。<br>
受け取るか，それとも断るか決めてくれい。
$TRE$TBE<br>
<FORM ACTION="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="plus">
HTML
	}
DwarfReading() if scalar(@RECDWF);
DwarfSending() if scalar(@SENDWF);
1;


sub DwarfReading
{
	$disp.=<<"HTML";
<BIG>●届いた宅配便</BIG><br><br>
$TB$TR
$TD／
$TDB送付品
$TDB代金
$TDB送付元
$TDB状態
$TDB期限
$TRE
HTML

my @MODE;
$MODE[0]=qq|<IMG class="i" SRC="$IMAGE_URL/map/dwfsign4.png">輸入予\約|;
$MODE[1]=qq|<IMG class="i" SRC="$IMAGE_URL/map/dwfsign1.png">新着|;
$MODE[2]=qq|<IMG class="i" SRC="$IMAGE_URL/map/dwfsign2.png">受取済み|;
$MODE[3]=qq|<IMG class="i" SRC="$IMAGE_URL/map/dwfsign3.png">受取拒否|;
$MODE[4]=qq|<IMG class="i" SRC="$IMAGE_URL/map/dwfsign2.png">輸入済み|;
$MODE[5]=qq|<IMG class="i" SRC="$IMAGE_URL/map/dwfsign3.png">輸入失敗|;

foreach my $i(@RECDWF)
	{
	my($no,$from,$item,$num,$price,$mode)=($DWF[$i]->{no},$DWF[$i]->{from},$DWF[$i]->{item},$DWF[$i]->{num},$DWF[$i]->{price},$DWF[$i]->{mode});
	$disp.=$TR.$TD;
	$disp.=($mode==1) ? "<input type=checkbox name=\"act_".$DWF[$i]->{no}."\" value=\"1\">" : " ";
	$disp.=$TD.GetTagImgItemType($item).$ITEM[$item]->{name}.' '.$num.$ITEM[$item]->{scale};
	$disp.='<br><small>(定価 '.GetMoneyString($ITEM[$item]->{price} * $num).')</small>';
	$disp.=$TD.GetMoneyString($price).$TD;
	if ($from==99)
		{
		$disp.='他の街';
		$mode+=2 if $mode>1;
		}
		else
		{
		$disp.=defined($id2idx{$from}) ? ($DT[$id2idx{$from}]->{shopname}) : 'なし';
		}
	$disp.=$TD.$MODE[$mode].$TD;
	$disp.=($DWF[$i]->{trade} eq "") ? "あと".GetTime2HMS($DWF[$i]->{tm}-$NOW_TIME+$BOX_STOCK_TIME) : "－－－－－－";
	$disp.=$TRE;


	}
$disp.=$TBE."<br>";
$disp.=<<"HTML" if ($NeverD);
選択した宅配便について <INPUT TYPE=SUBMIT NAME=ok VALUE="代金を払って受け取る">
<INPUT TYPE=SUBMIT NAME=ng VALUE="受け取りを断る">
</FORM><br>
HTML
}

sub DwarfSending
{
	$disp.=<<"HTML";
<FORM ACTION="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="delete">
<BIG>●送った宅配便</BIG><br><br>
$TB$TR
$TD／
$TDB送付品
$TDB代金
$TDB送付先
$TDB状態
$TDB期限
$TRE
HTML

my @MODE;
$MODE[0]=qq|<IMG class="i" SRC="$IMAGE_URL/map/dwfsign4.png">輸出待ち|;
$MODE[1]=qq|<IMG class="i" SRC="$IMAGE_URL/map/dwfsign4.png">受取待ち|;
$MODE[2]=qq|<IMG class="i" SRC="$IMAGE_URL/map/dwfsign2.png">受取済み|;
$MODE[3]=qq|<IMG class="i" SRC="$IMAGE_URL/map/dwfsign3.png">受取拒否|;
$MODE[4]=qq|<IMG class="i" SRC="$IMAGE_URL/map/dwfsign2.png">輸出完了|;
$MODE[5]=qq|<IMG class="i" SRC="$IMAGE_URL/map/dwfsign3.png">輸出失敗|;

my $tradeonly=1;
foreach my $i(@SENDWF)
	{
	my($no,$to,$item,$num,$price,$mode)=($DWF[$i]->{no},$DWF[$i]->{to},$DWF[$i]->{item},$DWF[$i]->{num},$DWF[$i]->{price},$DWF[$i]->{mode});
	$disp.=$TR.$TD;
	$disp.="<input type=checkbox name=\"del_".$DWF[$i]->{no}."\" value=\"1\">" if ($to!=99);
	$disp.=$TD.GetTagImgItemType($item).$ITEM[$item]->{name}.' '.$num.$ITEM[$item]->{scale};
	$disp.='<br><small>(定価 '.GetMoneyString($ITEM[$item]->{price} * $num).')</small>';
	$disp.=$TD.GetMoneyString($price).$TD;
	if ($to==99)
		{
		$disp.='他の街';
		$mode=0 if $mode==1;
		$mode+=2 if $mode>1;
		}
		else
		{
		$tradeonly=0;
		$disp.=defined($id2idx{$to}) ? ($DT[$id2idx{$to}]->{shopname}) : 'なし';
		}
	$disp.=$TD.$MODE[$mode].$TD;
	$disp.=($DWF[$i]->{trade} eq "") ? "あと".GetTime2HMS($DWF[$i]->{tm}-$NOW_TIME+$BOX_STOCK_TIME) : "－－－－－－";
	$disp.=$TRE;
	}
$disp.=$TBE."<br>";
$disp.=<<"HTML" if !$tradeonly;
選択した宅配便を <INPUT TYPE=SUBMIT VALUE="削除する">
</FORM>
HTML
}

