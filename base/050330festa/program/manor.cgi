# 荘園 2005/03/30 由來

$NOITEM=1;
DataRead();
CheckUserPass();
RequireFile('inc-manor.cgi');

$disp.="<BIG>●領主情報</BIG><br><br>";

my $MANORLORD;

if (defined($id2idx{$STATE->{leader}}))
	{
	my $i=$id2idx{$STATE->{leader}};
	$disp.=$TB.$TR.$TD.GetTagImgKao($DT[$i]->{name},$DT[$i]->{icon});
	$disp.=$TD."<SPAN>領主</SPAN> ： <b>".$DT[$i]->{name}."</b>";
	$disp.=DignityDefine($DT[$i]->{dignity})." <small>（".$DT[$i]->{shopname}."）</small><br>";
	$disp.=">> ".$DT[$i]->{comment};
	$disp.=$TRE.$TBE;

	# 荘園設定を取得
	ReadDTSub($DT[$i],"lord");
	$MANORLORD=$DT[$i]->{_lord};
	}
	else
	{
$disp.=$TB.$TR.$TD.GetTagImgKao($BAL_NAME,"bal");
$disp.=$TD."領主 ： <b>$BAL_NAME</b> <small>（$BAL_JOB）</small><br>";
$disp.=">> 荘園？ んなもん知るか。ぐわっはっは！";
$disp.=$TRE.$TBE;
	}

	ReadDTSub($DT,"seed");
	my $seedlock=0;
	my $ripeflag=0;

$disp.="<br><BIG>●荘園状況</BIG><br><br>";
$disp.=$TB.$TR;
$disp.=$TDB."種".$TDB."販売在庫".$TDB."販売価格".$TDB."自店保有".$TD.$TDB."収穫物".$TDB."買取価格".$TDB."自店保有".$TRE;

foreach my $i(0..$#MANOR)
	{
	my @MYMANOR=@{$MANOR[$i]};
	if ($DT->{_seed}->{"base$i"} && $DT->{_seed}->{"time$i"} < $NOW_TIME)
		{
		#成熟
		$DT->{_seed}->{"ripe$i"}+=$DT->{_seed}->{"base$i"};
		delete $DT->{_seed}->{"base$i"};
		delete $DT->{_seed}->{"time$i"};
		$seedlock++;
		}
	$disp.=$TR.$TD;
	$disp.=($MANORLORD->{"count$i"}) ? "<a href=\"action.cgi?key=manor-m&$USERPASSURL&buy=".$i."&bk=manor\">" : "<b>";
	$disp.=GetTagImgManor($MYMANOR[1]).$MYMANOR[0];
	$disp.=($MANORLORD->{"count$i"}) ? "</a>" : "</b>";
	$disp.=$TD.($MANORLORD->{"count$i"} + 0)." 個";
	$disp.=$TD."@".GetMoneyString($MANORLORD->{"price$i"});
	$disp.=$TD.($DT->{_seed}->{"base$i"} + 0)." 個";
	$disp.=$TD."→".$TD.GetTagImgManor($MYMANOR[3]).$MYMANOR[2];
	$disp.=$TD."@".GetMoneyString($MANORLORD->{"cost$i"});
	$disp.=$TD.($DT->{_seed}->{"ripe$i"} + 0)." 個".$TRE;
	$ripeflag+=$DT->{_seed}->{"ripe$i"};
	}
$disp.=$TBE;

if ($ripeflag)
	{
$disp.=<<"HTML";
	<br>
	<FORM ACTION="action.cgi" $METHOD>
	<INPUT TYPE=HIDDEN NAME=key VALUE="manor-r">
	<INPUT TYPE=HIDDEN NAME=bk VALUE="manor">
	$USERPASSFORM
<BIG>●収穫物売却</BIG>： 収穫物を領主の荘園に 
<INPUT TYPE=SUBMIT VALUE="買い取ってもらう">
	</FORM>
HTML
	}

if ($seedlock)
	{
	Lock();		#他人は同じファイルにアクセスしないのでロックは遅くていい
	WriteDTSub($DT,"seed");
	DataCommitOrAbort();
	UnLock();
	}

if ($STATE->{leader}==$DT->{id})
	{
	$disp.=<<STR;
	<br>
	<FORM ACTION="action.cgi" $METHOD>
	<INPUT TYPE=HIDDEN NAME=key VALUE="manor-f">
	$USERPASSFORM
	<INPUT TYPE=HIDDEN NAME=form VALUE="plus">
	<INPUT TYPE=SUBMIT VALUE='荘園を管理する'>
	</FORM>
STR
	}

OutSkin();
1;

