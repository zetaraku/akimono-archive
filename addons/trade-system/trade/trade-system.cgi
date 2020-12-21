#!/usr/local/bin/perl
# 貿易センター 2003/12/07 由來
# ** --- trade-system.cgi mu Exp $

# 貿易設定（変更はなるべくしない） ---------

$TIME_CYCLE=60*30;		# 輸出入の処理間隔(秒)
						#   短くするとサーバに高負荷がかかります。
$EXPIRE_TIME=21*60*60;	# 輸出から取引が終了するまでの時間(秒)
						#   短くすると輸出品を重複登録店舗で受け取るという不正が簡単になります。
$EXTEND_TIME=2*60*60;	# 取引延長時間(秒)
						#   輸出品が無くなった場合(輸出元に接続できない場合等)や，
						#   輸入手続が全く無い場合に，輸出入処理を延長する時間です。
						#   延長時間内に取引が成立すれば，その時点で輸出入処理が行われます。

# ------------------------------------------

$dir=$ENV{SCRIPT_FILENAME}||$0;
$dir=~s|(/?)[^/]+$||;
$dir||=$1 ? '/' : '.';

require "$dir/_config-trade.cgi" if -e "$dir/_config-trade.cgi";

$LOCKFILE="$dir/lockfile";
$SITE_DIR="$dir/site";
$EXPORTTIMEFILE="$dir/time.cgi";

$|=1;
$error=0;
$log="";
$time=time();

if(!$ENV{QUERY_STRING})
{
	# SSI用に空白出力
	print	"Content-type: text/plain\n\n";
}
else
{
	# <IMG>用に1x1dotのpng画像を出力
	print "Content-type: image/png\n\n";
	print	0x89,0x50,0x4e,0x47,0x0d,0x0a,0x1a,0x0a,0x00,0x00,0x00,0x0d,0x49,0x48,0x44,0x52,
			0x00,0x00,0x00,0x01,0x00,0x00,0x00,0x01,0x01,0x03,0x00,0x00,0x00,0x25,0xdb,0x56,
			0xca,0x00,0x00,0x00,0x03,0x50,0x4c,0x54,0x45,0xfc,0xfe,0xfc,0x25,0x90,0xc5,0x6a,
			0x00,0x00,0x00,0x0a,0x49,0x44,0x41,0x54,0x78,0x9c,0x63,0x60,0x00,0x00,0x00,0x02,
			0x00,0x01,0x48,0xaf,0xa4,0x71,0x00,0x00,0x00,0x00,0x49,0x45,0x4e,0x44,0xae,0x42,
			0x60,0x82;
}

$lasttime=(stat($LOCKFILE))[9];
unlink("nowtrade"),$lasttime=0 if -e "nowtrade";

exit if $lasttime>$time-$TIME_CYCLE || !-e $LOCKFILE;

utime($time,$time,$LOCKFILE);

{
	local $SIG{ALRM}=sub{exit};
	alarm(1);
	open(LOCK,$LOCKFILE);
	flock(LOCK,2);
	alarm(0);
}

%exporttime=();
if(open(IN,$EXPORTTIMEFILE))
{
	while(<IN>)
	{
		tr/\r?\n//d;
		my($key,$val)=split /\t/;
		$exporttime{$key}=$val;
	}
	close(IN);
}

opendir(DIR,$SITE_DIR);
@sitelist=(grep(!/\./,readdir(DIR)))[0..9];
@sitelist=grep($_,@sitelist);
closedir(DIR);

foreach my $site (@sitelist)
{
	open(IN,"$SITE_DIR/$site/define.cgi");
	$site{$site}={};
	while(<IN>)
	{
		chop;
		$_=~/^\s*(.+?)\s*=\s*(.+)\s*$/;
		$site{$site}->{$1}=$2;
	}
	close(IN);
}

@tradeitemlist=();
foreach my $site (@sitelist)
{
	next if -e "$SITE_DIR/$site/queue.cgi"; # END してないならskip
	
	my $url=$site{$site}->{url};
	my $password=$site{$site}->{password};
	$log.="GETLIST ".$url."\n\n";
	
	PostHTTP($url,"END",$password),next if(PostHTTP($url,"START",$password) ne 'OK');
	
	push(@tradeitemlist,grep($_ ne '',split(/\n/,$GET_DATA)));
	push(@opensite,$site);
}

%tradeitemlist=();
%tradeitemlistsale=();
%tradeitemsale=();
%tradeitemsaletime=();
%tradeitembuy=();
%tradehostcode=();
foreach(@tradeitemlist)
{
	my($trademode,$tradetime,$tradecode,$shopcode)=split(/\t/);
	
	my($hostcode,$boxno,$itemcode,$itemcnt,$price)=split(/!/,$tradecode);
	next if $itemcnt=~/\D/ or $price=~/\D/;
	
	$tradehostcode{$hostcode}++;
	
	$tradeitemlist{$tradecode}=1;
	if(!$trademode)
	{#輸入申し込み
		$tradeitembuy{$tradecode}.="$shopcode\t";
		$tradeitembuycount{$tradecode}++;
		$exporttime{$tradecode}||=$tradetime;
	}
	else
	{#輸出品
		$tradeitemlistsale{$tradecode}=$_;
		$tradeitemsale{$tradecode}=$shopcode;
		$tradeitemsaletime{$tradecode}=$tradetime;
		$exporttime{$tradecode}=$tradetime;
	}
}

%boxeditlist=();
%boxnewlist=();
foreach my $tradecode (keys(%tradeitemlist))
{
	my $buyshopcodelist=$tradeitembuy {$tradecode};
	my $saleshopcode   =$tradeitemsale{$tradecode};
	
	if($buyshopcodelist ne '' && $saleshopcode ne '')
	{
		$log.="COMMAND BUY AND SALE";	# 買い注文のある貿易品

		# 取引時間を終了していないアイテム
		if ($tradeitemsaletime{$tradecode} + $EXPIRE_TIME > $time)
			{
			push(@boxnewlist,$tradeitemlistsale{$tradecode}."\t".$tradeitembuycount{$tradecode});
			next;
			}

		# 取引時間終了の貿易品を処理
		my $buycount=$tradeitembuycount{$tradecode};

		#輸出処理
		my($hostcode,$boxno)=split(/!/,$saleshopcode);
		$boxeditlist{$hostcode}.="$boxno!outok,";
		
		#輸入処理
		my @buylist=grep($_ ne '',split(/\t/,$buyshopcodelist));
		my $buyshop=int(rand($#buylist+1));
		foreach my $cnt (0..$#buylist)
		{
			my($hostcode,$boxno)=split(/!/,$buylist[$cnt]);
			$boxeditlist{$hostcode}.="$boxno!".($buyshop==$cnt?'inok':'inng').",";
		}
	}
	elsif($buyshopcodelist ne '' && $tradehostcode{(split(/!/,$tradecode))[0]})
	{
		$log.="COMMAND BUY-".$tradecode;	# 買い注文があるのに貿易品がない

		#輸入失敗処理(出品無)
		my @buylist=grep($_ ne '',split(/\t/,$buyshopcodelist));
		foreach(@buylist)
		{
			next if $exporttime{$tradecode}>$time-$EXPIRE_TIME-$EXTEND_TIME; # 延長時間内であれば保留
			my($hostcode,$boxno)=split(/!/,$_);
			$boxeditlist{$hostcode}.="$boxno!inng,";
		}
	}
	elsif($saleshopcode ne '')
	{
		$log.="COMMAND SALE-".$tradecode;	# 買い注文のない貿易品

		# 取引時間を終了していないアイテム
		if($tradeitemsaletime{$tradecode}>$time-$EXPIRE_TIME-$EXTEND_TIME)
		{
			push(@boxnewlist,$tradeitemlistsale{$tradecode}."\t".$tradeitembuycount{$tradecode});
			next;
		}

		# 取引時間を終了して誰にも買われなかったさびしいアイテム
		my($hostcode,$boxno)=split(/!/,$saleshopcode);
		$boxeditlist{$hostcode}.="$boxno!outng,";
	}
	else
	{
		$log.="NO COMMAND ERROR-".$tradecode;
	}
}

foreach my $site (@opensite) #keys(%tradehostcode))
{
	my $queuefile="$SITE_DIR/$site/queue.cgi";
	open(OUT,">$queuefile");
	
	my $boxedit=$boxeditlist{$site};
	if($boxedit ne '')
	{
		$boxedit=substr($boxedit,0,length($boxedit)-1);
		print OUT "EDITBOX\n$boxedit\n";
	}
	print OUT "PUTLIST\n".$EXPIRE_TIME."\n".join("\n",@boxnewlist)."\n//\n";
	close(OUT);
}

foreach my $site (@sitelist)
{
	my $filename="$SITE_DIR/$site/queue.cgi";
	next if ! -e $filename;

	my $url=$site{$site}->{url};
	my $password=$site{$site}->{password};
	my $queue="";
	open(IN,$filename);
	while(<IN>){$queue.=$_;}
	close(IN);
	
	$log.="QUEUE ".$queue."\n\n";
	next if PostHTTP($url,$queue."END",$password) ne 'OK';
	rename($filename,"$SITE_DIR/$site/queue-backup.cgi");
}

if(open(OUT,">$EXPORTTIMEFILE"))
{
	foreach(grep $exporttime{$_}>$time-$EXPIRE_TIME*2-$EXTEND_TIME*2,keys %exporttime)
	{
		print OUT "$_\t$exporttime{$_}\n";
	}
	close OUT;
}

open(OUT,">$dir/log.cgi");
print OUT $log;
close(OUT);

close(LOCK);
exit;

sub PostHTTP
{
	my($url,$query,$password)=@_;
	$url=~/^http:\/\/(.+?)(\/.+)$/;
	my($host,$file)=($1,$2);
	$query=GetHash(time(),$password)."\n".$query;
	my $length=length($query);
	
	# socket open
	my $addr=(gethostbyname($host))[4];
	my $name=pack("S n a4 x8",2,80,$addr);
	return "" if !socket(S,2,1,0);
	return "" if !connect(S,$name);
	binmode(S);
	select(S);
	$|=1;
	select(STDOUT);
	
	print S "POST $file HTTP/1.0\r\n";
	print S "User-Agent: Akimono TRADE\r\n";
	print S "Host: $host\r\n";
	print S "Referer: http://$host$file\r\n";
	print S "Content-Length: $length\r\n";
	print S "\r\n";
	print S $query;
	
	$log.=
		"---- http://$host$file --------------------\r\n".
		"POST $file HTTP/1.0\r\n".
		"User-Agent: Akimono TRADE\r\n".
		"Host: $host\r\n".
		"Referer: http://$host$file\r\n".
		"Content-Length: $length\r\n".
		"\r\n".
		$query."\r\n";
	
	{
		local $SIG{ALRM}=sub{close(S);$error=1;return "";};
		alarm(60);
		while(<S>){$_=~s/[\r\n]//g; last if $_ eq "";}
		$GET_RETURN_CODE=<S>; chop $GET_RETURN_CODE;
		$GET_CHECK_SUM=<S>;   chop $GET_CHECK_SUM;
		$GET_DATA="";
		while(<S>){$GET_DATA.=$_;}
		alarm(0);
	}
	close(S);
	$log.=
		"----------------------------\r\n".
		$GET_RETURN_CODE."\r\n".
		$GET_CHECK_SUM."\r\n".
		$GET_DATA."\r\n";
	
	if($error)
	{
		$GET_RETURN_CODE='ERROR';
		$GET_CHECK_SUM='';
		$GET_DATA='';
		$error=0;
	}
	return $GET_RETURN_CODE;
}

sub GetHash
{
	my($time,$str)=@_;
	my $len=length($str);
	my $hash=$time;
	my $seed=0;
	for(my $i=0; $i<$len; $i++)
	{
		my $val=unpack('C',substr($str,$i,1));
		$seed= $i&1 ? $seed*($val+1) : $seed/($val+1);
		$seed+=$val;
	}
	$seed=int($seed);
	for(my $i=0; $i<$len; $i++)
	{
		my $val=unpack('C',substr($str,$i,1));
		$val*=($seed+1);
		$seed=($val+substr($hash,-3,3)) & 255;
		$hash.=$val*($seed & 15);
		my $len1=int(length($hash)/2);
		my $len2=length($hash)-$len1;
		$hash=substr($hash,$len1,$len2).substr($hash,0,$len1);
	}
	$hash=substr($hash,int(length($hash)/4),32);
	return $hash.$time.sprintf("%02d",length($time));
}

__END__

