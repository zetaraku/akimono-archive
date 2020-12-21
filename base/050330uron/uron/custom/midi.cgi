# MIDIの設定ファイル 2005/03/30 由來

# -------- 設定部分 ----------
# MIDIのファイル名を変更できます。
# CGI別サーバーのところでは，ここを http:// から始まるパスに指定します。

$MIDI_URL = "midi.mid";

# ----------------------------

$NOMENU=1;
$Q{bk}="none";
print "Content-type: text/html\n\n";

my $bgmtag;

if ($ENV{HTTP_USER_AGENT}=~ /MSIE/ && $ENV{HTTP_USER_AGENT}!~ /Opera/)
	{
	$bgmtag=qq|<BGSOUND src="$MIDI_URL" loop=infinite>|;
	}
	else
	{
	$bgmtag=qq|<EMBED src="$MIDI_URL" width=2 height=2 autostart=true loop=true>|;
	}
print "Content-type: text/html\n\n";
print <<"EOM";
<html lang="ja">
<HEAD>
<TITLE>BGM</TITLE>
$bgmtag
</HEAD>
<BODY>
</HTML>
EOM
exit;
1;