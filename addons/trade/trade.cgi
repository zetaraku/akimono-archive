#!/usr/local/bin/perl
# 貿易処理 2005/01/07 由來

# 貿易機能設定 -----------------------------

$TRADE_HOST_ALLOW	='';		# 貿易許可IP：    貿易網参加時に貿易機能提供サイト側より指定
$TRADE_HOST_PASSWORD	='pass';	# 貿易パスワード：貿易網参加時に貿易機能提供サイト側より指定

# ------------------------------------------


require './_config.cgi';
RequireFile('inc-func.cgi');

Error('NOT SET $TOWN_CODE') if !$TOWN_CODE;
Error("NOT ALLOW ADDR $ENV{REMOTE_ADDR}") if $TRADE_HOST_ALLOW ne '' && $ENV{REMOTE_ADDR}!~/$TRADE_HOST_ALLOW/;
Error("NOT POST") if $ENV{REQUEST_METHOD} ne "POST";

read(STDIN,$query,$ENV{CONTENT_LENGTH});
my @buffer=split(/\n/,$query);
my $login=shift(@buffer);
Error("PASSWORD ERROR $login") if !CheckHash($login,$TRADE_HOST_PASSWORD);

my @log=();
my $error=0;
my $ourbuffer="";

print "Content-type: text/plain\n\n";

Lock();
DataRead();

while(1)
{
my $cmd=shift(@buffer);
last if $cmd eq '';
push(@log,"UNKNOWN COMMAND $cmd"),last if !defined(&$cmd);
&$cmd;
last if $error;
}

DataCommitOrAbort();
UnLock();

if(!$error)
{
	print "OK\n";
	print "\n";
	print $outbuffer;
}
else
{
	print "ERROR\n\n\n";
}

#open(OUT,">>$DATA_DIR/tradelog.cgi");
#print OUT $NOW_TIME."\n".join("\n",@log)."\n-----------\n";
#print OUT $outbuffer."\n-----------\n";
#close(OUT);
exit;

sub START
{
	OpenAndCheck(GetPath("tradelock"));
	close(OUT);
	push(@log,"START LOCK:".(-e GetPath("tradelock")));
	ReadDWF();
	@BOX=grep(/,[\w!]+$/,@DWF);
	foreach(@BOX)
	{
		chop;
		my($no,$time,$from,$to,$itemno,$itemcnt,$price,$trademode,$data)=split(/,/);
		if ($trademode==1)
			{
			# 輸出
			next if !defined($id2idx{$from});
			my $shopname=$DT[$id2idx{$from}]->{shopname}.','.$TOWN_TITLE.','.$msg;
			$outbuffer.="$trademode\t$time\t$TOWN_CODE!$no!$ITEM[$itemno]->{code}!$itemcnt!$price\t$TOWN_CODE!$no!$shopname\n";
			}
			else
			{
			# 輸入申込
			next if !defined($id2idx{$to});
			my ($hostcode,$boxno,$itemcode)=split(/!/,$data);
			$itemcode||=$ITEM[$itemno]->{code};
			my $shopname=$DT[$id2idx{$to}]->{shopname}.','.$TOWN_TITLE.','.$msg;
			$outbuffer.="$trademode\t$time\t$hostcode!$boxno!$itemcode!$itemcnt!$price\t$TOWN_CODE!$no!$shopname\n";
			}
	}
	push(@log,"GETLIST:".$outbuffer);
}

sub END
{
	unlink(GetPath("tradelock"));
	push(@log,"END UNLOCK:".(-e GetPath("tradelock")));
}

sub PUTLIST
{
	OpenAndCheck(GetPath($TEMP_DIR,"trade"));
	while(1)
	{
		$_=shift(@buffer);
		last if $_ eq '//' || $_ eq '';
		
		print OUT $_."\n";
	}
	close(OUT);
	push(@log,"PUTLIST:".(-e GetPath($TEMP_DIR,"trade")));
}

sub EDITBOX
{
	push(@log,"EDITBOX");
	my @editbox=split(/,/,shift(@buffer));
	ReadDWF();
	foreach(@editbox)
	{
		my($boxno,$ope)=split(/!/);
		$idx=SearchDWFIndex($boxno);
		next if $idx==-1;
		chop $DWF[$idx];
		($no,$time,$from,$to,$item,$num,$price,$mode,$trade)=split(/,/,$DWF[$idx]);
		$ITEM=$ITEM[$item];

		push(@log,"UNKNOWN EDIT COMMAND $ope\n"),next if !defined(&$ope);
		&$ope;
	}
	WriteDWF();
	RenewLog();
	DataWrite();
}

sub Error
{
	WriteErrorLog($_[0],"trade");
	exit;
}

sub ReadDWF
{
	undef @DWF;
	open(IN,GetPath("dwarf")) or return;
	@DWF=<IN>;
	close(IN);
}

sub WriteDWF
{
	OpenAndCheck(GetPath($TEMP_DIR,"dwarf"));
	print OUT @DWF;
	close(OUT);
}

sub SearchDWFIndex
{
	my($no)=@_;
	foreach(0..$#DWF)
		{
		return $_ if ($DWF[$_]=~/^$no,/);
		}
	return -1;
}

sub inok
{
	push(@log,"-INOK");
	$DT=$DT[$id2idx{$to}];
	$DT->{paytoday}+=$price;
	$DT->{money}-=$price;
	$DT->{item}[$item-1]+=$num;
	$DT->{item}[$item-1]=$ITEM->{limit} if $DT->{item}[$item-1] > $ITEM->{limit};
	PushLog(0,$DT->{id},$ITEM->{name}." ".$num.$ITEM->{scale}."を".GetMoneyString($price)."にて輸入しました");
	$mode=2;
	$DWF[$idx]="$no,$time,$from,$to,$item,$num,$price,$mode,\n";
}

sub outok
{
	push(@log,"-OUTOK");
	$DT=$DT[$id2idx{$from}];
	$DT->{saletoday}+=$price;
	$DT->{money}+=$price;
	PushLog(0,$DT->{id},"輸出した".$ITEM->{name}." ".$num.$ITEM->{scale}."が".GetMoneyString($price)."にて売れました");
	$mode=2;
	$DWF[$idx]="$no,$time,$from,$to,$item,$num,$price,$mode,\n";
}

sub inng
{
	push(@log,"-INNG");
	$DT=$DT[$id2idx{$to}];
	PushLog(0,$DT->{id},$ITEM->{name}." ".$num.$ITEM->{scale}."は輸入できませんでした");
	$mode=3;
	$DWF[$idx]="$no,$time,$from,$to,$item,$num,$price,$mode,\n";
}

sub outng
{
	push(@log,"-OUTNG");
	$DT=$DT[$id2idx{$from}];
	$DT->{item}[$item-1]+=$num;
	$DT->{item}[$item-1]=$ITEM->{limit} if $DT->{item}[$item-1] > $ITEM->{limit};
	PushLog(0,$DT->{id},"輸出した".$ITEM->{name}." ".$num.$ITEM->{scale}."は売れませんでした");
	$mode=3;
	$DWF[$idx]="$no,$time,$from,$to,$item,$num,$price,$mode,\n";
}

