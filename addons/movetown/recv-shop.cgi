#!/usr/local/bin/perl
# 移転データ受け取り 2003/10/02 由來
# ** --- recv-shop.cgi,v 1.17 2002/12/02 13:05:10 mu Exp $

require './_config.cgi';
RequireFile('inc-func.cgi');

Error('DISNABLED MOVE-TOWN') if !$MOVETOWN_ENABLE;
Error('NOT SET $TOWN_CODE') if !$TOWN_CODE;

Error("NOT POST") if $ENV{REQUEST_METHOD} ne "POST";
read(STDIN,$query,$ENV{CONTENT_LENGTH});

$townmaster=ReadTown($TOWN_CODE,1);
Error("NO OWN TOWN") if !$townmaster;

my @buffer=split(/\n/,$query);

#移転元の街情報を取得＆正当性チェック
$towncode=shift(@buffer);
$TOWN=ReadTown($towncode);
Error("NOT ALLOW TOWN $towncode") if !$TOWN;
Error("NOT ALLOW ADDR $towncode $ENV{REMOTE_ADDR}") if $TOWN->{myaddr} ne '' && $ENV{REMOTE_ADDR}!~/$TOWN->{myaddr}/;

#パスワードチェック
$login=shift(@buffer);
Error("PASSWORD ERROR $towncode $login") if !CheckHash($login,$TOWN->{password});

#店舗データ取得
$data=shift(@buffer);
eval("\$DTM=".$data.";");
Error("DATA ERROR $towncode") if $DTM->{name} eq '';

#店舗データ取得
$data=shift(@buffer);
eval("\$DTM_STOCK=".$data.";");

#移転元街データ取得
%towndata=split(/\t/,shift(@buffer));
Error("DATA STOCK ERROR $towncode") if $towndata{code} eq '';

#IP取得
$trueip=shift(@buffer);

print "Content-type: text/plain\n\n";

Lock();
DataRead();

$DTM->{nocheckip}=0 if $towndata{group} eq '' || $towndata{group} ne $townmaster->{group};

my($result,$detailresult)=CheckShopData($DTM);
if($result eq '')
{
	$DTM->{name}=$DTM->{newname};
	$DTM->{pass}=($PASSWORD_CRYPT ? crypt($DTM->{newpass},GetSalt()) : $DTM->{newpass});
	$DTM->{rankingyesterday}=0;
	$DTM->{boxcount}=0;
	$DTM->{lastlogin}=$NOW_TIME;
	$DTM->{item}=[];
	$DTM->{exp}={};
	$DTM->{itemyesterday}={};
	$DTM->{itemtoday}={};
	my %itemcode2no=();
	my $val;
	foreach my $no (1..$MAX_ITEM)
	{
		my $code=$ITEM[$no]->{code};
		$itemcode2no{$code}=$no;
		next if $code eq '';
		
		$val=GetValue($DTM,$DTM_STOCK,'itemcode',$code,$ITEM[$no]->{limit});
		$DTM->{item}->[$no-1]=$val;
		
		$val=GetValue($DTM,$DTM_STOCK,'expcode',$code,1000);
		$DTM->{exp}->{$no}=$val if $val;
		
		$val=GetValue($DTM,$DTM_STOCK,'itemyesterdaycode',$code);
		$DTM->{itemyesterday}->{$no}=$val if $val;
		
		$val=GetValue($DTM,$DTM_STOCK,'itemtodaycode',$code);
		$DTM->{itemtoday}->{$no}=$val if $val;

		sub GetValue
		{
			my($DTM,$DTM_STOCK,$key,$code,$limit)=@_;
			
			my $val=$DTM->{$key}->{$code}+0;
			foreach(@$DTM_STOCK)
			{
				$val+=$_->{$key}->{$code};
				delete $_->{$key}->{$code};
				delete $_->{$key} if !scalar(%{$_->{$key}});
			}
			if($limit && $val>$limit)
			{
				$DTM->{$key}->{$code}=$val-$limit;
				$val=$limit;
			}
			else
			{
				delete $DTM->{$key}->{$code};
			}
			return $val;
		}
	}
	if($DTM_STOCK->[9]->{town})
	{
		my $stock=$DTM_STOCK->[9];
		# debug $stock->{itemcode}->{yyyy}=123;
		foreach(keys(%{$stock->{itemcode}}))
		{
			$detailresult.=$_."\t".$stock->{itemcode}->{$_}."\t";
		}
		$detailresult="trash=$DTM_STOCK->[9]->{town}\t$detailresult" if $detailresult=~s/\t$//;
	}
	$DTM->{usercode}={};
	if($townmaster->{allowuserdata})
	{
		$DTM->{usercode}=$DTM->{user};
		$DTM->{user}={};
		foreach my $key ((split /,/,$townmaster->{allowuserdata}),(grep /^_so_/,keys %{$DTM->{usercode}}))
		{
			next if $key!~/^_so_/ && $townmaster->{allowuserdata} eq 'none';
			my $found=0;
			foreach my $stock ($DTM,@$DTM_STOCK)
			{
				if(exists $stock->{usercode}{$key})
				{
					$DTM->{user}{$key}=$stock->{usercode}{$key} if !$found++;
					delete $stock->{usercode}{$key};
				}
			}
		}
	}
	unshift(@{$DTM_STOCK},
		{
			'town'				=>"$towncode!$towndata{name}",
			'id'				=>$DTM->{id},
			'itemcode'			=>$DTM->{itemcode},
			'expcode'			=>$DTM->{expcode},
			'itemyesterdaycode'	=>$DTM->{itemyesterdaycode},
			'itemtodaycode'		=>$DTM->{itemtodaycode},
			'usercode'			=>$DTM->{usercode},
		}
	);
	$DTM->{id}='';
	foreach(@$DTM_STOCK)
	{
		$DTM->{id}=$_->{id},last if (split(/!/,$_->{town}))[0] eq $TOWN_CODE;
	}
	$DTM->{id}=$DTnextid if $DTM->{id} eq '' || scalar(grep($_==$DTM->{id},map{$_->{id}}@DT));
	OpenAndCheck(GetPath($SUBDATA_DIR,"$DTM->{name}-s"));
	print OUT "stock=".GetDataTree([@{$DTM_STOCK}[0..9]])."\n";
	close(OUT);
	
	foreach my $idx (0..$DTM->{showcasecount}-1)
	{
		my $itemno=$itemcode2no{$DTM->{showcasecode}->[$idx]}+0;
		$itemno=0 if $ITEM[$itemno]->{flag}=~/s/;	# s 陳列不可
		$DTM->{price}->[$idx]=0 if !$itemno;
		$DTM->{showcase}->[$idx]=$itemno;
	}
	$DTblockip=$DTM->{remoteaddr};

	#移動距離に応じた時間消費
	#$DTM->{time}=$NOW_TIME-$MAX_STOCK_TIME if $NOW_TIME-$DTM->{time}>$MAX_STOCK_TIME;
	$DTM->{_MoveTownTime}=GetMoveTownTime($DTM,$townmaster,$TOWN); # 移転時間:保存されない一時的なパラメータ
	EditTime($DTM,-$DTM->{_MoveTownTime});

	push(@DT,$DTM);
	$DT=$DTM;
	require "$ITEM_DIR/funcshopin.cgi" if $DEFINE_FUNCSHOPIN;
	my $usetime="";
	$usetime.='/移転時間'.GetTime2HMS($DTM->{_MoveTownTime})    if $DTM->{_MoveTownTime};
	$usetime.='/予定時間'.GetTime2HMS($DTM->{_MoveTownTimeSrc}) if $DTM->{_MoveTownTimeSrc};
	PushLog(1,0,$DTM->{shopname}."が移転してきました。");
 	PushLog(0,$DT->{id},'移転を実行'.$usetime) if ($usetime);		#時間表示を分離。
	RenewLog();
	DataWrite();
	DataCommitOrAbort();
	WriteErrorLog("SUCCESS $towncode ".$DTM->{shopname},$LOG_MOVESHOP_FILE);
	print "OK\n$detailresult\n";
}
else
{
	print "$result\n$detailresult\n";
}
UnLock();

exit;

sub Error
{
	WriteErrorLog($_[0],$LOG_MOVESHOP_FILE);
	exit;
}

sub CheckShopData
{
	my($DT)=@_;
	return('DENY','msg=移転先に空きがありませんでした') if scalar(@DT)>=$MAX_MOVE_USER;
	return('DENY','msg=移転先に同じ名前(ID)の店舗が存在しました') if scalar(grep($_ eq $DT->{newname},map{$_->{name}}@DT));
	return('DENY','msg=移転先に同じ店名の店舗が存在しました') if scalar(grep($_ eq $DT->{shopname},map{$_->{shopname}}@DT));
	return('DENY','msg=移転先に存在しないギルドに所属しています') if $DT->{guild} ne '' && !scalar(grep($_ eq $DT->{guild},keys(%GUILD)));
	return('DENY','msg=重複登録疑惑による移転制限です') if $townmaster->{blocksameip} ne '' && !$DT->{nocheckip} && scalar(GetIPList($trueip));
	return('DENY','msg=資金が足りません') if $townmaster->{allowmoney} ne '' && $townmaster->{allowmoney}>$DT->{money}+$DT->{moneystock};
	return('DENY','msg=資金が多すぎます') if $townmaster->{denymoney}  ne '' && $townmaster->{denymoney}<$DT->{money}+$DT->{moneystock};
	return('DENY','msg=ギルド制限です')   if $townmaster->{allowguild} ne '' && !scalar(grep($_ eq $DT->{guild},split(/[^\w]+/,$townmaster->{allowguild}))) && $DT->{guild} ne '';
	return('DENY','msg=ギルド制限です')   if $townmaster->{denyguild}  ne '' && scalar(grep($_ eq $DT->{guild},split(/[^\w]+/,$townmaster->{denyguild}))) && $DT->{guild} ne '';
	return('DENY','msg=トップ回数が足りません') if $townmaster->{allowtopcount} ne '' && $townmaster->{allowtopcount}>$DT->{rankingcount};
	return('DENY','msg=トップ回数が多すぎます') if $townmaster->{denytopcount}  ne '' && $townmaster->{denytopcount}<$DT->{rankingcount};
	return('DENY','msg=開業期間が短いです') if $townmaster->{allowfoundation} ne '' && $townmaster->{allowfoundation}>$NOW_TIME-$DT->{foundation};
	return('DENY','msg=開業期間が長いです') if $townmaster->{denyfoundation}  ne '' && $townmaster->{denyfoundation}<$NOW_TIME-$DT->{foundation};
	return('DENY','msg=どのギルドにも所属していません') if $townmaster->{onlyguild}  ne '' && $DT->{guild} eq '';
	return('DENY','msg=ギルドに所属しています') if $townmaster->{noguild}  ne '' && $DT->{guild} ne '';
	return('DENY','msg=移転先に存在しない職業に所属しています') if $DT->{job} ne '' && !scalar(grep($_ eq $DT->{job},keys(%JOBTYPE)));
	return('DENY','msg=職業制限です')   if $townmaster->{allowjob} ne '' && !scalar(grep($_ eq $DT->{job},split(/\W+/,$townmaster->{allowjob}))) && $DT->{job} ne '';
	return('DENY','msg=職業制限です')   if $townmaster->{denyjob}  ne '' &&  scalar(grep($_ eq $DT->{job},split(/\W+/,$townmaster->{denyjob}))) && $DT->{job} ne '';
	return('DENY','msg=どの職業にも就いていません') if $townmaster->{onlyjob}  ne '' && $DT->{job} eq '';
	return('DENY','msg=職業に就いています') if $townmaster->{nojob}  ne '' && $DT->{job} ne '';
	return "";
}

