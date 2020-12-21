# 新規開店 2004/01/20 由來

$image[0]=GetTagImgKao("案内人","guide");
require $JCODE_FILE;
DataRead();

if($Q{admin} ne $MASTER_PASSWORD)
{
	OutError('新規店舗登録権限がありません。') if $NEW_SHOP_ADMIN;
	OutError('あなたはすでに店舗を持っています。') if GetIPList(GetTrueIP());
	OutError('あなたは他の街ですでに店舗を持っています。') if $NEW_OTHERTOWN_BLOCK && GetDoubleIP(GetTrueIP());
	OutError('あなたは現在登録制限されています。') if $NEW_SHOP_BLOCKIP && GetTrueIP() eq $DTblockip;
	OutError('出店キーワードが正しくありません。') if $NEW_SHOP_KEYWORD && $Q{sname} && $Q{newkey} ne $NEW_SHOP_KEYWORD;
	checkMaxUser();
}

if($Q{sname}.$Q{name}.$Q{pass1}.$Q{pass2})
{
	$Q{name}=jcode::sjis($Q{name},$CHAR_SHIFT_JIS&&'sjis');
	$Q{sname}=jcode::sjis($Q{sname},$CHAR_SHIFT_JIS&&'sjis');

	if(($Q{sname}.$Q{name}.$Q{pass1}.$Q{pass2}) =~ /([,:;\t\r\n<>&])/
	|| ($Q{pass1}.$Q{pass2}) =~ /([^A-Za-z0-9_\-])/  #.$Q{name}を削除
	|| $Q{name} eq 'soldoutadmin'
	|| CheckNGName($Q{sname})
	|| CheckNGName($Q{name})  #名前のチェックを追加
	)
	{
		OutError('名前・店名・パスワードに使用できない'.
		         '文字が含まれています。');
	}
	if(!$Q{sname} || !$Q{name} || !$Q{pass1} || !$Q{pass2})
	{
		OutError('名前・店名・パスワードを入力してください。');
	}
	if($Q{pass1} ne $Q{pass2})
	{
		OutError('確認パスワードが違っています。');
	}
	if(length($Q{sname})<4)
	{
		OutError('店名の文字数が少ないです。');
	}
	if(length($Q{name})>12 || length($Q{sname})>20
	|| length($Q{pass1})>12 || length($Q{pass2})>8)
	{
		OutError('名前(全角6文字)・店名(全角10文字)・パスワード(8文字)の文字数が多いです。');
	}
	if( $Q{name} eq $Q{pass1} )
	{
		OutError('名前とパスワードは同じにしないでください。');
	}
	
	Lock();
	DataRead();
	OutError('既に存在する名前です。-> '.$Q{name}) if $name2pass{$Q{name}};
	OutError('既に存在する店名です。-> '.$Q{sname}) if GetDoubleName($Q{sname});;
	
	$idx=$DTusercount;
	$DTlasttime=$NOW_TIME if !$idx;
	$DT[$idx]={};
	$DT=$DT[$idx];
	$DT->{status}	    =1;
	$DT->{id}           =$DTnextid;
	$DT->{lastlogin}    =$NOW_TIME;
	$DT->{name}         =$Q{name};
	$DT->{shopname}     =$Q{sname};
	$DT->{icon}     =$Q{icon};
	$DT->{pass}         =$PASSWORD_CRYPT ? crypt($Q{pass1},GetSalt()) : $Q{pass1};
	$DT->{money}        =100000;
	$DT->{moneystock}   =0;
	$DT->{time}         =$NOW_TIME-12*60*60;
	$DT->{rank}         =5010;
	$DT->{saleyesterday}=0;
	$DT->{saletoday}    =0;
	$DT->{costtoday}    =0;
	$DT->{costyesterday}=0;
	$DT->{paytoday}     =0;
	$DT->{payyesterday} =0;
	$DT->{showcasecount}=1;
	$DT->{itemyesterday}={};
	$DT->{itemtoday}	={};
	$DT->{remoteaddr}   =GetTrueIP();
	$DT->{rankingyesterday}='';
	$DT->{taxtoday}     =0;
	$DT->{taxyesterday} =0;
	$DT->{foundation}   =$NOW_TIME;
	foreach $cnt (0..$DT->{showcasecount}-1)
	{
		$DT->{showcase}[$cnt]=0;
		$DT->{price}[$cnt]=0;
	}
	foreach $cnt (0..$MAX_ITEM-1)
	{
		$DT->{item}[$cnt]=0;
	}

	$DTblockip=$DT->{remoteaddr};

	require "$ITEM_DIR/funcnew.cgi" if $DEFINE_FUNCNEW;
	PushLog(1,0,$Q{sname}."が新装開店しました。") if !$DEFINE_FUNCNEW || !$DEFINE_FUNCNEW_NOLOG;

	RenewLog();
	DataWrite();
	DataCommitOrAbort();
	UnLock();

	$disp=<<STR;
街に新しいお店が誕生しました。<br><br>
$TB$TR$TD
<SPAN>名前</SPAN>：$Q{name}<BR>
<SPAN>店名</SPAN>：$Q{sname}<BR>
<SPAN>パスワード</SPAN>：$Q{pass1}
$TRE$TBE
<BR>※パスワードは必ずメモを取っておいてください。<BR><BR>
$TB$TR
$TD$image[0]$TD
スタートしたら，まず<SPAN>[掲示板]</SPAN>であいさつをすると良いでしょう。<br>
また<SPAN>[図書館]</SPAN>に経営のヒントがありますので一通りご覧下さい。
$TRE$TBE
<BR>
<A HREF=\"index.cgi?u=$Q{name}!$Q{pass1}\">ゲームスタート</A><BR><BR>
ログイン後に[♪]を押すとBGMを演奏することができます。
STR
	OutSkin();
	exit;
}

RequireFile("inc-new.cgi");
OutSkin();
1;

sub checkMaxUser
{
	OutError($TB.$TR.$TD.$image[0].$TD.'申し訳ありませんが，現在満員となっております。<BR>空きが出るのをお待ちください。'.$TRE.$TBE)
		if $DTusercount>=$MAX_USER;
}

sub GetDoubleIP
{
	foreach my $pg(@OtherDir)
	{
	my $datafile='../'.$pg.'/data/user.cgi';
	my($ip)=@_;
	open(IN,$datafile) or return();
	my @data=<IN>;
	close(IN);
	my @list=map{(split(/\t/,$_))[4]}@data;
	@list=grep($_ eq $ip,@list) if $ip ne '';
	return @list if (@list);
	}
}
