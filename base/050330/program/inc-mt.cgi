# メンテナンス表示 2005/03/30 由來

my $msg="";
if(-f "./lock")
{
	open(IN,"./lock");
	$msg=join("",<IN>);
	close(IN);
}
elsif(-f "$DATA_DIR/lock")
{
	open(IN,"$DATA_DIR/lock");
	$msg=join("",<IN>);
	close(IN);
}

if($ENV{REMOTE_ADDR} ne $msg)
{
	PrintMt();
	exit;
}
1;


sub PrintMt
{
my $er;
if (-e "$DATA_DIR/error.log")
	{
	$er=<<"STR";
	<br><TABLE cellspacing="0" cellpadding="1" border="0">
	<TBODY><TR vAlign=center align=middle><TD bgcolor="#6B6599">
	<TABLE cellspacing="0" cellpadding="5" width="700" border="0">
	<TBODY><TR><TD width="80" bgcolor="#ABA5FF" align="center">
	<FONT color="#FFFFFF"><small>for Admin</small></FONT></TD>
	<TD align="center" bgcolor="#DBD5FF">エラーのためシステムを停止しました。 … 
	<A HREF="$DATA_DIR/error.log">[エラー情報]</A> ： <A HREF="http://akimono.org/">[エラー相談]</A>
	</TD></TR></TBODY></TABLE></TD></TR></TBODY></TABLE>
STR
	}

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
<TITLE>$HTML_TITLE:メンテ中</TITLE>
</HEAD>
<BODY BGCOLOR="#FFFFFF" TEXT="#000000" LINK="#6050cc" VLINK="#6050cc" ALINK="#FF0000">
<center><br><SPAN>Sorry, Now Under Site Maintenance.</SPAN><br><br>
<TABLE cellspacing="0" cellpadding="0"><TBODY><TR><TD bgcolor="#6B6599">
<TABLE cellspacing="1" cellpadding="0" border="0" width="700"><TBODY><TR><TD bgcolor="#FFFFFF" align="center">
<br>ただいまメンテナンス作業中のため，ゲームが停止しております。<br><br>
プレイ中の方にはご不便をおかけしますが，もうしばらくお待ちください。<br>
数時間以上経っても戻らない場合は，お手数ですが<a href="mailto:$ADMIN_EMAIL">管理人までご連絡</a>ください。<br><br>
<A HREF=\"$HOME_PAGE\" TARGET=_top>[ホームに戻る]</A>
<br><div align="right"><small>
<A HREF="http://akimono.org/">商人物語</A></small></div>
</TD></TR></TBODY></TABLE>
</TD></TR></TBODY></TABLE>
$er<br>$msg</CENTER>
<br><div align="right">
<FORM ACTION="admin.cgi" METHOD="POST"><INPUT TYPE=PASSWORD size=6 NAME=admin>
<INPUT TYPE=SUBMIT VALUE="Admin"></FORM></div>
</body></html>
STR
}

