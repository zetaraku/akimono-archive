# エラー分析と安全な終了 2005/03/30 由來

my($msg)=@_;
die($msg) if $ERROR_REENTRY;	# ループ防止
$ERROR_REENTRY=1;

@_=(gmtime(time()+60*60*9))[5,4,3,2,1,0];
$_[0]+=1900; $_[1]++;
my $nowtime=sprintf("%d/%02d/%02d %02d:%02d:%02d",@_);

	open(OUT,">>$DATA_DIR/$ERROR_COUNT_FILE$FILE_EXT");
	print OUT "1";
	close(OUT);
	
my $er_m="分析できませんでした。";

$msg=~s/&/&amp;/g;
$msg=~s/"/&quot;/g;
$msg=~s/</&lt;/g;
$msg=~s/>/&gt;/g;
$msg=~s/\n/<br>/g;
if ($msg =~ /at\s(\S+)\sline/) {
	$er_s=$1;
	$er_sm="";
	$er_sm="<br>このファイルを特に改変していない場合は別なファイルにエラーがあります。" if ($msg =~ /func/);
	$er_sm="<br>これは「<b>inc-item-data.cgi</b>」を修正することにより解決します。" if ($msg =~ /data\/item/);
}
if ($msg =~ /line\s(\d+)[,\.]/) {
	$er_l=$1;
}
if ($msg =~ /syntax\serror/ || $msg =~ /Scalar\sfound/ || $msg =~ /Array\sfound/) {
	$er_m="文法ミスです。「\"」「\'」「\;」「\}」などのつけ忘れであることが多いです。";
}
if ($msg =~ /Unrecognized\scharacter/) {
	$er_m="処理できない文字が含まれています。間違えて全角文字を使ってしまったか，<br>全角文字を「\"」や「\'」などでくくるのを忘れていることが多いです。";
}
if ($msg =~ /Illegal\sdivision\sby\szero/) {
	$er_m="ゼロで割る計算をさせています。<br>ある変数で割るときには，その変数がゼロになる場合は計算を回避してください。";
}
if ($msg =~ /Can't\sfind\sstring\sterminator/) {
	$er_m="文字列が「\"」や「\'」などで閉じられていません。";
}
if ($msg =~ /Unmatched\sright/) {
	$er_m="文法ミスです。「\}」や「)」などが余計に多いようです。";
}
if ($msg =~ /Missing\sright/) {
	$er_m="文法ミスです。「\}」や「)」などをつけ忘れているようです。";
}
if ($msg =~ /not\sdefined\sfunction/) {
	$er_m="サブルーチンの名称にミスがあるようです。<br>原因としては，バージョンアップのミス，アイテムデータのイベント関連のミスなどが考えられます。";
}
if ($msg =~ /Can't\slocate/) {
	$er_m="ファイルが存在しません。イベントやアイテムデータを削除したためかもしれません。";
}

PrintErr();

my $error_count=(-s "$DATA_DIR/$ERROR_COUNT_FILE$FILE_EXT");
if ($error_count > 9)
{
	mkdir("$DATA_DIR/lock",$DIR_PERMISSION) unless (-d "$DATA_DIR/lock")
}

UnLock() if $LOCKED;	#ロック解除
CoUnLock() if $COLOCKED;
exit(-1);
1;


sub PrintErr
{
print "Cache-Control: no-cache, no-store\n";
print "Pragma: no-cache\n";
print "Content-type: text/html; charset=Shift_JIS\n\n";
print <<"STR";
<HTML><HEAD>
<Style Type="text/css">
<!--
A:link   { font-weight: bold; text-decoration:none}
A:visited{ font-weight: bold; text-decoration:none}
A:hover  { font-weight: bold; text-decoration:underline;}
BODY,TR,TD,TH { font-family:"MS UI Gothic"; font-size:11pt; }
SPAN { font-family:"Comic Sans MS"; font-size:16pt; color:#664499 ;}
input,input.button{color:#000000;background-color:#FFFFFF;border:1 #5f5f8c solid}
-->
</Style>
<TITLE>$HTML_TITLE:エラー</TITLE>
</HEAD>
<BODY BGCOLOR="#FFFFFF" TEXT="#000000" LINK="#6050cc" VLINK="#6050cc" ALINK="#FF0000">
<center><br><SPAN>Sorry, An Error is Detected.</SPAN><br><br>
<TABLE cellspacing="0" cellpadding="0"><TBODY><TR><TD bgcolor="#6B6599">
<TABLE cellspacing="1" cellpadding="0" border="0" width="700"><TBODY><TR><TD bgcolor="#FFFFFF" align="center">
<br>エラーが発見されたため，実行が中止されました。<br><br>
プレイ中の方にはご不便をおかけしますが，解決までしばらくお待ちください。<br>
なかなか解決しない場合は，お手数ですが<a href="mailto:$ADMIN_EMAIL">管理人までご連絡</a>ください。<br><br>
<A HREF=\"$HOME_PAGE\" TARGET=_top>[ホームに戻る]</A>
<br><div align="right"><small>
<A HREF="http://akimono.org//">商人物語</A></small></div>
</TD></TR></TBODY></TABLE>
</TD></TR></TBODY></TABLE>
<br><TABLE cellspacing="0" cellpadding="1" border="0">
<TBODY><TR vAlign=center align=middle><TD bgcolor="#6B6599">
<TABLE cellspacing="0" cellpadding="5" width="700" border="0">
<TBODY><TR><TD width="80" bgcolor="#ABA5FF" align="center">
<FONT color="#FFFFFF"><small>for Admin</small></FONT></TD>
<TD align="center" bgcolor="#DBD5FF">以下のアドバイスに従ってエラーを解決してください。 … 
<A HREF="http://akimono.org/">[エラー相談]</A>
</TD></TR></TBODY></TABLE></TD></TR></TBODY></TABLE>
<br><TABLE cellspacing="0" cellpadding="5" width="700" border="0">
<TR><TD width="80" bgcolor="#ABA5FF" align="center">
<FONT color="#FFFFFF"><small>エラー状況</small></FONT></TD>
<td bgcolor="#DBD5FF">$MYNAME の実行により発生。<small>($nowtime)</small></tr>
<TR><TD width="80" bgcolor="#ABA5FF" align="center">
<FONT color="#FFFFFF"><small>エラー原因</small></FONT></TD>
<td bgcolor="#DBD5FF">「<b>$er_s</b>」の $er_l行目付近に原因があるようです。$er_sm</tr>
<TR><TD width="80" bgcolor="#ABA5FF" align="center">
<FONT color="#FFFFFF"><small>エラー分析</small></FONT></TD>
<td bgcolor="#DBD5FF">$er_m</tr>
<TR><TD width="80" bgcolor="#ABA5FF" align="center">
<FONT color="#FFFFFF"><small>Error Data</small></FONT></TD>
<td bgcolor="#DBD5FF"><small>$msg</small></tr></table>
</CENTER><br><div align="right">
<FORM ACTION="admin.cgi" METHOD="POST"><INPUT TYPE=PASSWORD size=6 NAME=admin>
<INPUT TYPE=SUBMIT VALUE="Admin"></FORM></div>
</body></html>
STR

my $txt= <<"STR";
$MYNAME の実行により発生。($nowtime)
「$er_s」の $er_l行目付近に原因があるようです。$er_sm
$er_m
$msg
STR

	my $ErrFile = $DATA_DIR."/error.log";
	open(OUT,"> $ErrFile");
	print OUT $txt;
	close(OUT);
	chmod (0666,$ErrFile);
}

