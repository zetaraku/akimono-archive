# ユーザー情報変更処理 2005/03/30 由來

Lock();
DataRead();
CheckUserPass();
$Q{er}='other';

my $functionname=$Q{mode};
OutError("bad request") if !defined(&$functionname);
&$functionname;

RenewLog();
DataWrite();
DataCommitOrAbort();
UnLock();

OutSkin();
1;


sub comment
{
	require $JCODE_FILE;
	$comment=jcode::sjis($Q{cmt},$CHAR_SHIFT_JIS&&'sjis');

	if(($comment) =~ /([,:;\t\r\n<>&])/
	|| CheckNGName($comment)
	)
		{
		OutError('コメントに使用できない文字が含まれています。');
		}
	OutError('コメントの文字数が多いです。') if length($comment)>36;
	$comment=~s/&/&amp;/g;
	$comment=~s/>/&gt;/g;
	$comment=~s/</&lt;/g;
	$DT->{comment}=$comment;
	$disp.="コメント更新しました";
}

sub icon
{
	$DT->{icon}=$Q{icon};
	$disp.="店長アイコン変更しました";
}

sub shopname
{
	OutError('資金が足りません。') if $DT->{money}<50000;
	require $JCODE_FILE;
	$Q{rename}=jcode::sjis($Q{rename},$CHAR_SHIFT_JIS&&'sjis');
	if(($Q{rename}) =~ /([,:;\t\r\n<>&])/
	|| CheckNGName($Q{rename})
	)
		{
		OutError('店名に使用できない文字が含まれています。');
		}
	OutError('店名は20文字以内です。') if length($Q{rename})>20;
	OutError('店名が短すぎます。') if length($Q{rename})<4;
	OutError('既に存在する店名です。-> '.$Q{rename}) if GetDoubleName($Q{rename});;
	PushLog(1,0,$DT->{shopname}."が「".$Q{rename}."」に店名を改めました。");
	$DT->{shopname}=$Q{rename};
	$DT->{money}-=50000;
	$disp.=$DT->{shopname}."へ改名しました。<BR>トップより入店し直してください。<BR><BR>";
	$disp.="<A HREF='index.cgi'>トップへ</A>";
}

sub owname
{
	OutError('資金が足りません。') if $DT->{money}<50000;
	require $JCODE_FILE;
	$Q{owname}=jcode::sjis($Q{owname},$CHAR_SHIFT_JIS&&'sjis');
	if(($Q{owname}) =~ /([,:;\t\r\n<>&])/
	|| CheckNGName($Q{owname})
	)
		{
		OutError('名前に使用できない文字が含まれています。');
		}
	OutError('名前は12文字以内です。') if length($Q{owname})>12;
	OutError('名前が短すぎます。') if length($Q{owname})<2;
	OutError('既に存在する名前です。-> '.$Q{owname}) if $name2pass{$Q{owname}};
	PushLog(1,0,$DT->{name}."が「".$Q{owname}."」に改名しました。");
	$DT->{name}=$Q{owname};
	$DT->{money}-=50000;
	$disp.=$DT->{name}."へ改名しました。<BR>トップより入店し直してください。<BR><BR>";
	$disp.="<A HREF='index.cgi?u=$DT->{name}'>トップへ</A>";
}

sub repass
{
	OutError('確認入力と不一致のため変更中止します。') if $Q{pw1}ne$Q{pw2};
	OutError('変更パスワードが入力されていません。') if $Q{pw1}eq'';
	OutError('パスワードに使用できない文字がありましたので変更中止します。') if $Q{pw1}=~/[^a-zA-Z0-9_\-]/;
	OutError('パスワードは 8文字までです。') if length($Q{pw1})>8;
	$DT->{pass}=$PASSWORD_CRYPT ? crypt($Q{pw1},GetSalt()) : $Q{pw1};
	$disp.="パスワード変更しました<BR>トップより入店し直してください<BR><BR>";
	$disp.="<A HREF='index.cgi?nm=$DT->{name}&pw=$Q{pw1}'>トップへ</A>";
}

sub restart
{
	OutError('再出発したい場合は restart と入力してください。') if $Q{rss} ne 'restart';
	OutError('創業後3時間以内は再出発できません') if (($NOW_TIME-$DT->{foundation}) < 3600*3);

	my ($id,$name,$shopname,$pass,$icon)=($DT->{id},$DT->{name},$DT->{shopname},$DT->{pass},$DT->{icon});
	while(my($key,$val)=each %$DT) { delete $DT->{$key}; }
	($DT->{id},$DT->{name},$DT->{shopname},$DT->{pass},$DT->{icon},$DT->{time})=($id,$name,$shopname,$pass,$icon);
	$DT->{status}	      =1;
	$DT->{lastlogin}    =$NOW_TIME;
	$DT->{money}        =100000;
	$DT->{rank}         =5010;
	$DT->{foundation}   =$NOW_TIME;
	$DT->{showcasecount}=1;
	require "$ITEM_DIR/funcnew.cgi" if $DEFINE_FUNCNEW;
	opendir(SESS,$SUBDATA_DIR);
	my @dir=readdir(SESS);
	closedir(SESS);
	foreach(map{"$SUBDATA_DIR/$_"}grep(/^$DT->{id}\-.+\.cgi$/,@dir))
	{
		unlink $_;
	}
	PushLog(1,0,$DT->{shopname}."が気持ちを新たに出直しました。");
	$disp.="データが初期化されました。<BR><BR>気持ちを新たにがんばってください♪";
}

sub cls
{
	OutError('店じまいしたい場合は closeshop と入力してください。') if $Q{cls}ne'closeshop';
	SetCookieSession();
	$USERPASSURL=$USERPASSFORM="";
	CloseShop($DT->{id},'自主閉店');
	PushLog(1,0,$DT->{shopname}."が閉店しました。");
	$disp.="店じまいの手続きが完了いたしました。<BR><BR>"
		  ."本ゲームへの参加，本当にありがとうございました。";
	$DTblockip=$DT->{remoteaddr};
}

sub guild
{
	OutError('退団するにはleaveと入力してください') if $Q{guild} ne 'leave';
	OutError('ギルドに入団していないので退団の必要がありません') if !$DT->{guild};
	ReadGuild();
	my $name=$GUILD{$DT->{guild}}->[$GUILDIDX_name];
	$name="解散したギルド" if $name eq '';;
	PushLog(1,0,$DT->{shopname}."がギルド「".$name."」から退団しました。");
	$disp.=$name."から退団しました。";
	delete $DT->{user}{_so_e};
	$DT->{guild}="";
}

