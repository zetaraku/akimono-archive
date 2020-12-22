#!/usr/local/bin/perl
# 管理メイン 2005/03/30 由來

require './_config.cgi';
GetQuery();
RequireFile("inc-makeitem.cgi") if $Q{key} eq "makeitem";

($MYDIR,$MYNAME)=($ENV{SCRIPT_NAME}=~/^.*\/([^\/]+)\/([^\/]+)$/); # 自ファイル名/ディレクトリ名
@log=();

OutError('管理者パスワードが設定されていません') if $MASTER_PASSWORD eq '';
OutError('管理者メールアドレスが設定されていません') if $ADMIN_EMAIL eq '';
OutError('街コードが設定されていません') if ($MOVETOWN_ENABLE && !$TOWN_CODE);
OutError('$DATA_DIR の設定不良，もしくは，$DATA_DIR ディレクトリが作成されていません') if !-e $DATA_DIR;
OutError('$SESSION_DIR $TEMP_DIR $LOG_DIR $BACKUP_DIR $SUBDATA_DIR 辺りの設定が異常です') if $SESSION_DIR eq '' || $TEMP_DIR eq '' || $LOG_DIR eq '' || $BACKUP_DIR eq '' || $SUBDATA_DIR eq '';

$checkdatadir=' ディレクトリ '.$DATA_DIR.' のパーミッションを見直してください';

if($Q{admin} ne $MASTER_PASSWORD)
{
	$disp.=<<"HTML";
	<FORM ACTION="$MYNAME" METHOD="POST">
	<TABLE cellspacing="0" cellpadding="1" bgcolor="#6B6599" border="0">
	<TBODY><TR vAlign=center align=middle><TD>
	<TABLE cellspacing="0" cellpadding="5" width="700" border="0">
	<TBODY><TR><TD width="80" bgcolor="#ABA5FF" align="center">
	<FONT color="#FFFFFF"><small>for Admin</small></FONT></TD>
	<TD align="center" bgcolor="#DBD5FF" colspan="2">管理者パスワード 
	<INPUT TYPE=PASSWORD size=8 NAME=admin> <INPUT TYPE=SUBMIT VALUE="管理メニューへ"> 
	... <small><A HREF="http://akimono.org/">商人物語</A></small>
	</TD></TR></TBODY></TABLE></TD></TR></TBODY></TABLE></FORM>
HTML
}
elsif($Q{mode} ne "")
{
	RequireFile("inc-admin-func.cgi");
}
else
{
	RequireFile("inc-admin.cgi");
}

OutHeader();
foreach(@log)
{
	$_="<b>$_</b>" if substr($_,0,1) eq ' ';
	print $_."<br>";
}
print $disp;
print <<"HTML" if scalar(@log);
	<hr noshade size=1>
	<FORM ACTION="$MYNAME" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=admin VALUE="$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="管理メニューへ戻る">
	</FORM>
HTML
print "</center></BODY>";
print "</HTML>";
exit;


sub OutHeader
{
print "Cache-Control: no-cache, must-revalidate\n";
print "Pragma: no-cache\n";
print "Content-type: text/html; charset=Shift_JIS\n\n";
print <<STR;
<HTML><HEAD>
<Style Type="text/css">
<!--
A:link   { font-weight: bold; text-decoration:none}
A:visited{ font-weight: bold; text-decoration:none}
A:hover  { font-weight: bold; text-decoration:underline;}
FORM {margin: 2pt;}
BODY,TR,TD,TH { font-family:"MS UI Gothic"; font-size:11pt; }
BIG { font-weight: bold; font-size:11pt; color:#664499 ;}
SPAN { font-weight: bold; font-size:11pt; color:#bb44bb ;}
input,select,textarea{color:#000000;background-color:#FFFFFF;border:1 #5f5f8c solid}
input.button{color:#000000;background-color:#FFFFFF;border:1 #5f5f8c solid}
hr 	{color:#666666;}
-->
</Style>
<TITLE>$HTML_TITLE:管理室</TITLE>
</HEAD><BODY BGCOLOR="#FFFFFF" TEXT="#000000" LINK="#6050cc" VLINK="#6050cc" ALINK="#FF0000">
<center>
<BIG>商人物語 $HTML_TITLE 管理室</BIG><br><br>
STR
}

sub GetQuery
{
	my($q,@q,$key,$val);
	$q="";
	
	if($ENV{'REQUEST_METHOD'} eq "POST")
	{
		read(STDIN,$q,$ENV{'CONTENT_LENGTH'});
	}
	$q.="&".$ENV{'QUERY_STRING'};

	@q=split(/&/,$q);
	foreach (@q)
	{
		($key,$val)=split(/=/);
		$val =~ tr/\?/ /;
		$val =~ tr/+/ /;
		$val =~ s/\t/ /g;
		$val =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("H2",$1)/eg;
		$val =~ s/"/ /g;
		$val =~ s/'/ /g;
		$val =~ s/,/ /g;
		$val =~ s/[\r\n]//g;
		$Q{$key}=$val;
	}
	if($Q{u} ne '')
	{
		$Q{nm}="";
		$Q{pw}="";
		$Q{ss}="";
		($Q{nm},$Q{pw},$Q{ss})=split(/[!:]/,$Q{u},3);
	}
}

sub OutError
{
	print "Cache-Control: no-cache, must-revalidate\n";
	print "Pragma: no-cache\n";
	print "Content-type: text/html; charset=Shift_JIS\n\n";
	print "<HTML><HEAD><TITLE>管理メニュー</TITLE></HEAD>";
	print "<BODY>";
	print $_[0]."<br>";
	print '<font color=red><b>マニュアルを参照して正しく設定して下さい</b></font>' if !$_[1];
	print qq|<FORM ACTION="$MYNAME" METHOD="POST"><INPUT TYPE=HIDDEN NAME=admin VALUE="$Q{admin}">|;
	print qq|<INPUT TYPE="SUBMIT" VALUE="管理メニューへ戻る"></FORM>|;
	print "</BODY>";
	print "</HTML>";
	exit;
}

sub GetFileList
{
	opendir(DIR,$_[0]);
	my @list=map{$_[0]."/".$_}grep(/$_[1]/ && !/^\.\.?$/,readdir(DIR));
	closedir(DIR);
	
	return @list;
}

