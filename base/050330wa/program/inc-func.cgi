# 基本関数定義 2005/03/30 由來

BEGIN{$SIG{__WARN__}=$SIG{__DIE__}=sub{$incdir=$INCLUDE_DIR; $incdir||="../program"; require "$incdir/inc-error.cgi"; die($_[0]);};}

# 初期設定
srand();	#乱数セット
$disp="";	# 出力バッファ初期化
$NOW_TIME=time(); # 現在時刻
$LOCKED='';	# ロック状態初期化
@LOG=();	# ログ初期化

($MYDIR,$MYNAME)=($ENV{SCRIPT_NAME}=~/^.*\/([^\/]+)\/([^\/]+)$/); # 自ファイル名/ディレクトリ名
($REFERER)=($ENV{HTTP_REFERER}=~/.+\/(.+)$/);                     # HTTP REFERER

RequireFile('inc-mt.cgi') if -e "$DATA_DIR/lock"; # メンテモード

Lock(),DataCommitOrAbort(1),UnLock() if -e GetPath($COMMIT_FILE);

my $townfile="$COMMON_DIR/towndata$FILE_EXT";
require $townfile if -e $townfile;
require(GetPath($ITEM_DIR,"item")) if !$NOITEM;
require(GetPath($GUILD_FILE));

CheckMobile();
SetSkin();

@DTindexnamelist=
	qw(
		id lastlogin name shopname pass money time rank showcasecount comment saleyesterday
		saletoday costyesterday rankingcount remoteaddr dignity rankingyesterday
		paytoday payyesterday profitstock taxmode costtoday drmoney taxyesterday trush
		taxtoday guild blocklogin nocheckip foundation
		job icon
	);
@STATEnamelist=
	qw(
		leader money in out develop devem safety safem army robina robinb
	);


sub AUTOLOAD
{
	my($package,$functionname)=$AUTOLOAD=~/^(.*)::(.+)/;
	
	if($package ne 'main')
	{
		@_=caller;
		die(qq|not defined function [$package::$functionname $_[1] line $_[2]] |);
	}
	
	my $requirefile=GetPath("autoload");
	require $requirefile if -e $requirefile; # require autoload index
	
	$requirefile=$autoload{$functionname};
	$requirefile&&=$AUTOLOAD_DIR."/".$requirefile.".cgi";
	require $requirefile if -e $requirefile; # require autoload function
	
	if(!defined(&$functionname))
	{
		my @back=@_;
		RequireFile("inc-autoload.cgi");
		MakeIndexAutoLoad($functionname);
		@_=@back;
	
		if(!defined(&$functionname))
		{
			@_=caller;
			die(qq|not defined function [$functionname $_[1] line $_[2]] |);
			#OutError("not defined function",$functionname) if !defined(&$functionname);
		}
	}
	
	goto &$functionname;
}

sub GetPath
{
	return $DATA_DIR."/".$_[0].$FILE_EXT if @_==1;
	return join("/",@_).$FILE_EXT;
}

#携帯端末系かどうかのチェック&テーブル定義
sub CheckMobile
{
	my $agent=$ENV{HTTP_USER_AGENT};

	if($agent=~/^(DoCoMo|KDDI|J-PHONE|ASTEL|PDXGW)/ || $DEBUG_MOBILE)
	{
		#携帯系
		$MOBILE=1;
		$TB=$TBT=$TR=$TRT=$TDB="";
		$TBE=$TRE=$TD=$TDNW="<BR>";
		$LIST_PAGE_ROWS=$LIST_PAGE_ROWS_MOBILE;
		$METHOD=qq|method="GET"|;
	}
	else
	{
		#パソコン系
		$MOBILE=0;
		$TB	="<TABLE>";
		$TBT	="<TABLE class=t>";
		$TBE	="</TABLE>\n";
		$TR	="<TR>";
		$TRT	="<TR class=t>";
		$TRE	="</TR>\n";
		$TD	="<TD>";
		$TDB	="<TD class=b NOWRAP>";
		$TDNW="<TD NOWRAP>";
		$LIST_PAGE_ROWS=$LIST_PAGE_ROWS_PC;
		$METHOD=qq|method="POST"|;
	}
}

sub SetSkin
{
	my $skinfile='smain';
	$skinfile='sindex' if ($MYNAME eq 'index.cgi');
	$skinfile.='-mob' if $MOBILE;
	open(IN,$skinfile.'.html');
	read(IN,my $SKIN,-s $skinfile.'.html');
	close(IN);
	%DISP={};
	($DISP{TOP},$DISP{MENU},$DISP{BOTTOM})=split(/<!--SKINPAUSE-->/, $SKIN);
}

sub OutHeader
{
	print "Cache-Control: no-cache, no-store\n";
	print "Pragma: no-cache\n";
	print "Content-type: text/html; charset=Shift_JIS\n\n";
}

sub OutSkin
{
	OutHeader();
	return if $ENV{REQUEST_METHOD} eq "HEAD";
	
	$DISP{TOP} =~ s/#SKINTITLE#/$HTML_TITLE/;
	print $DISP{TOP};
	
	my $backurl=GetBackUrl() if $USER and $NOMENU || $Q{bk};
	print($backurl,'<BR><BR>') if $backurl;
	
	if ($MOBILE)
		{
		print GetMenuTag('menu','[メニュー]'),'<br><br>' if !$NOMENU && $Q{key} ne 'menu';
		$DISP{MENU} =~ s/#SKINTITLE#/$HTML_TITLE/;
		print $DISP{MENU};
		}
	elsif (!$NOMENU)
		{
		require "$CUSTOM_DIR/inc-menu.cgi";
		}
	print $disp;
	print('<BR><BR>',$backurl) if $backurl;
	
	@_=times(); $_[0]+=$_[1];
	$DISP{BOTTOM} =~ s/#SKINCPU#/(int($_[0]*1000)\/1000)/e;
	print $DISP{BOTTOM};
}

sub GetTagImgKao
{
	return qq|<IMG ALT="$_[0]" $_[2]$ICON_SIZE BORDER="0" SRC="$IMAGE_URL/kao/kao$_[1].png">|;
}

sub GetTagImgJob
{
	my($i,$ii)=@_;
	return qq|<IMG ALT="すっぴん" class="j" SRC="$IMAGE_URL/job/job.gif">| if !$i;
	return qq|<IMG ALT="$JOBTYPE{$i}" class="j" SRC="$IMAGE_URL/job/job$i.gif">|;
}

sub GetFileTime
{
	return GetTime2FormatTime((stat(GetPath($_[0])))[9]+0,1);
}

sub GetMenuTag
{
	return qq|<A HREF="action.cgi?key=$_[0]&$USERPASSURL$_[2]">$_[1]</A> | if $USERPASSURL || $_[2];
	return qq|<A HREF="action.cgi?key=$_[0]">$_[1]</A> |;
}

sub GetQuery
{
	RequireFile('inc-dec.cgi'), return if ($ENV{'CONTENT_TYPE'} =~ /multipart\/form-data/);
	my $q;
	$ENV{REQUEST_METHOD} eq "POST" ? read(STDIN,$q,$ENV{CONTENT_LENGTH}) : ($q=$ENV{QUERY_STRING});
	return if length($q)<=1;
	
	my $key;
	undef %Q;
	foreach(split(/&/,$q))
	{
		($key,$_)=split(/=/);
		tr/\?+/  /;
		s/%([a-fA-F0-9][a-fA-F0-9])/pack('H2',$1)/eg;
		tr/"',\x00-\x1f/   /d;
		$Q{$key}=$_;
	}
	@Q{qw(nm pw ss)}=split(/!/,$Q{u},3) if exists $Q{u};
}

sub GetCookieSession
{
	my $cookieon=0;
	my($name,$sess)=($ENV{HTTP_COOKIE}=~/SESSION=(.*)!(\w*)/);
	$cookieon=1 if $name ne "";
	$name="" if $name eq "-check-cookie-";
	return ($name,$sess,$cookieon);
}

sub SetCookieSession
{
	my($name,$sess)=@_;
	$name="-check-cookie-",$sess=time() if $name eq "";
	print "Set-Cookie: SESSION=$name!$sess;\n";
}

sub DataRead
{
	my $datafile=GetPath($DATA_FILE);
	
	open(IN,$datafile);
	read(IN,my $buf,-s $datafile);
	close(IN);
	my @DATA=split(/\n/,$buf);
	
	OutError("no data") if !@DATA;
	
	my $idx=0;
	my $maxdata=@DATA;
	
	$DTlasttime=$DATA[$idx++];
	($DTpeople,$DTnextid,$DTblockip,$DTTaxrate,$DTState)=split(/,/,$DATA[$idx++]);
	@DTwholestore=split(/,/,$DATA[$idx++],$MAX_ITEM);
	%DTevent=split(/,/,$DATA[$idx++]);
	undef %STATE;
	my @buf=split(/:/,$DTState); my $i=0;
	foreach (@STATEnamelist) { $STATE->{$_}=$buf[$i];$i++;}
	foreach(keys(%DTevent)){require(GetPath($ITEM_DIR,"event",$_));}
	
	tie($DTtown,"AutoVar",[\$DTtown,$DATA[$idx++],"HASH",","]) if $DATA[$idx] ne '//';
	
	while($DATA[$idx++] ne '//'){}
	
	undef @DT;
	undef %id2idx;
	undef %name2idx;
	undef %name2pass;
	
	my @list;
	my $cnt=0;
	my $id;
	my $name;
	
	while($idx<$maxdata)
	{
		my %DT;
		$DT[$cnt]=\%DT;
		
		@DT{@DTindexnamelist}=split(/,/,$DATA[$idx++]);
		$DT{point}=GetDTPoint(\%DT);
		$DT{status}=1;
		
		$id=$DT{id};
		$name=$DT{name};
		
		$id2idx{$id}=$name2idx{$name}=$cnt;
		$name2pass{$name}=$DT{pass};
		
		$DTnextid=$id+1 if $DTnextid<=$id;
		
		if($MAX_ITEM)
		{
			@list=split(/:/,$DATA[$idx],7);
			@DT{qw(showcase price)}=map{[split(/,/,$_)]}@list[0,1];
			tie $DT{item},"AutoVar",[\$DT{item},$list[2],"ARRAY",","];
			@DT{qw(itemyesterday itemtoday exp)}=map{{split(/,/,$_)}}@list[3,4,5];
			$list[6] ? tie($DT{user},"AutoVar",[\$DT{user},$list[6],"HASH",'[\t,]']) : ($DT{user}={});
		}
		$idx++;
		$cnt++;
	}
	$DTusercount=$cnt;
}

sub GetDTPoint
{
	my($DT)=@_;
	my $p=($DT->{profitstock}*3+$DT->{saletoday}-$DT->{taxtoday}-$DT->{paytoday})/500000+1;
	my $r=0.5 + ( 5 / ($DT->{rankingcount} + 10) );	#優勝回数による補正
	$p= 15 - (50 / $p) if ($p > 10);		#高すぎる点数を補正
	$p= 1 / (2 - $p) if ($p < 1);			#低すぎる点数を補正
	return int( $DT->{rank} * $r * $p );
}

sub CheckUserPass
{
	my($guestok)=@_;
	$MYFORM="<INPUT TYPE=HIDDEN NAME=key VALUE=\"$Q{key}\">\n";
	
	my $username=$Q{nm};
	my $password=$Q{pw};
	my $session=$Q{ss};
	my($Cname,$Csess,$cookieon)=GetCookieSession();
	#$disp.="($ENV{HTTP_COOKIE},$Cname,$Csess,$cookieon)"; #デバッグ用
	if($username eq '' && $Cname ne '')
		{$username=$Cname;$session=$Csess;}
	else
		{$Cname=$Csess="";}
	
	if($guestok && $username eq '' && $password eq '')
	{
		$DT={};
		$DT->{id}=-1;
		$DTid=$DTidx=0;
		$GUEST_USER=1;
		$USER=$USERPASSURL=$USERPASSFORM="";
		return;
	}
	
	OutError("bad request") if $username eq '';
	OutError("no user",$username) if !exists $name2pass{$username} && $username ne 'soldoutadmin';
	
	my $fn=$SESSION_DIR."/".$username.".cgi";
	
	if($session ne '')
	{
		SetCookieSession(),OutError("timeout") if (stat($fn))[9]<$NOW_TIME-$SESSION_TIMEOUT_TIME || !open(SESS,$fn);
		$_=<SESS>;
		close(SESS);
		chop;
		SetCookieSession(),OutError("timeout") if $_ ne $session;
		utime($NOW_TIME,$NOW_TIME,$fn);
		SetCookieSession($username,$session) if $Cname ne '';
		$MASTER_USER=1 if $username eq 'soldoutadmin';
	}
	else
	{
		if($password ne '')
		{
			$session=CheckLogin($username,$password,$fn);
			if($cookieon&&!$MASTER_USER)
			{
				SetCookieSession($username,$session);
				$Cname=$username;
				$Csess=$session;
			}
		}
		else
		{
			OutError("no user",$username);
		}
	}
	
	$USER=$username;
	$USERSESSION=$session;
	$USERPASSURL=$USERPASSFORM="";
	if($Cname eq "")
	{
		$USERPASSURL ="u=$username!!$session";
		$USERPASSFORM="<INPUT TYPE=HIDDEN NAME=u VALUE=\"$username!!$session\">";
	}
	$COOKIESESSION=$Cname ne "";
	$DTidx=$name2idx{$USER};
	$DT=$DT[$DTidx];
	$DTid=$DT->{id};
	
	$DT->{lastlogin}=$NOW_TIME if !$MASTER_USER;
	
	require "$ITEM_DIR/funcinit.cgi" if $DEFINE_FUNCINIT;
}

sub Get02D
{
	return $_[0]<10 ? '0'.$_[0] : $_[0];
}

sub GetTime2HMS
{
	my($tm,$mode)=@_;
	
	my $s=$tm%60;
	return Get02D($s).'秒' if $tm<60;
	
	my $m=($tm-$s)%3600;
	return ($m/60).'分' if $tm<3600;
	
	my $h=($tm-$s-$m)/3600;
	return $h.'時間'.($m && !$mode ? Get02D($m/60).'分':'') if $h<24*3;
	
	return int($h/24).'日';
}

sub GetTagA
{
	#my($str,$href,$nolink,$target)=@_;
	
	return $_[0]." " if $_[2];
	return qq|<a href="$_[1]">$_[0]</a> | if $_[3] eq '';
	return qq|<a target="$_[3]" href="$_[1]">$_[0]</a> |;
}

sub Turn
{
	$DTlasttime=(stat(GetPath($LASTTIME_FILE)))[9];
	return if !$DTlasttime;
	RequireFile('inc-turn.cgi') if $NOW_TIME-$DTlasttime>$UPDATE_TIME;
}

sub GetMoneyString
{
	my($num)=@_;
	$num=$num+0;
	my $i;
	if ($num =~ /^[-+]?\d\d\d\d+/g) {
		for ($i = pos($num) - 3, $j = $num =~ /^[-+]/; $i > $j; $i -= 3) {
		substr($num, $i, 0) = ',';
		}
	}
	return $term[0].$num.$term[1];
}

require "$ITEM_DIR/funcbase.cgi" if $DEFINE_FUNCBASE;

package AutoVar;

sub Get
{
	my $tied=tied ${$_[0]};
	my $data=$tied ? $tied->[1] : ${$_[0]};
	my $ref=ref $data;
	return $data if !$ref;
	return join $_[1]||",",($ref eq 'ARRAY' ? @$data : %$data);
}

sub TIESCALAR { bless $_[1],$_[0];}

sub FETCH
{
	return $_[0]->[1] if ref $_[0]->[1];
	my @array=split /$_[0]->[3]/,$_[0]->[1];
	my $array=$_[0]->[2] eq 'ARRAY' ? [@array] : {@array};
	$_[0]->[1]=$array;
	untie ${$_[0]->[0]};
	return $array;
}

sub STORE
{
	$_[0]->[1]=$_[1];
	$_[0]->[2]=(ref $_[1])||'ARRAY';
	$_[0]->[3]||=',';
	untie ${$_[0]->[0]} if $_[0]->[2];
	return;
}

1;
