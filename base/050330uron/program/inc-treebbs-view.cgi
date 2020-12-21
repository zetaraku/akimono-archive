# 掲示板記事表示 2003/10/08 由來

Msgview() if ($Q{mode} eq "msgview");
&msg_form;
1;


sub Msgview
{
	my($no,$re,$lx,$sub,$eml,$nam,$msg,$lt,$ho,$oya,$sml,$v_nam,$v_eml,$v_msg,$v_tim,$v_sub,$v_sml,$date);

	$flag=0;
	@new=();
	open(IN,$datafile) or return();
	$top = <IN>;
	while (<IN>) {
		($no,$re,$lx,$sub,$eml,$nam,$msg,$lt,$ho,$oya,$sml) = split(/<>/);
		if ($Q{oya} == $oya) { push(@new,$_); }
		elsif ($flag && $Q{oya} != $oya) { last; }
		if ($Q{no} == $no) {
			$flag=1;
			$v_nam = $nam;
			$v_eml = $eml;
			$v_msg = $msg;
			$v_tim = $lt;
			$v_sub = $sub;
			$v_sml = $sml;
		}
	}
	close(IN);

	# レスタイトル
	$res_sub = $v_sub;
	if ($res_sub =~ /^Re\^(\d+)\:(.*)/) {
		$renum = $1 + 1;
		$res_sub = "Re\^$renum\:$2";
	}
	elsif ($res_sub =~ /^Re\:(.*)/) { $res_sub = "Re\^2:$1"; }
	else { $res_sub = "Re: $res_sub"; }

	&auto_link($v_msg);
	$v_msg =~ s/"/&quot;/g;
	$date = GetTime2FormatTime($v_tim);
$disp.=<<HTML;
<table width=500>
$TR$TDB■ $v_sub$TRE
$TR$TD<SPAN>発言者</SPAN>：<b> $v_nam</b> $v_eml<br>
<SPAN>発言日</SPAN>： $date$TRE
$TR$TD◇
<blockquote>$v_msg</blockquote>
</td></tr></table>
HTML

	if (@new > 1) {
		$disp.="<hr width=500 size=1><table width=500><tr><td><BIG>▼関連発言</BIG>\n";
		$x=0;
		$disp.="<UL>\n";
		foreach (@new) {
			($no,$re,$lx,$sub,$eml,$nam,$msg,$lt,$ho,$oya,$sml) = split(/<>/);
			while ($x > $lx) { $disp.="</UL>\n"; $x--; }
			while ($x < $lx) { $disp.="<UL>\n"; $x++; }
			$sub = &cut_subject($sub);
			if ($lx != 0) {
				$disp.="<LI><a href=\"action.cgi?key=treebbs&$USERPASSURL&no=$no&reno=$re&oya=$oya&mode=msgview&page=$page\">$sub</a> - <B>$nam</B> $dat ";
			} else {
				$disp.="<a href=\"action.cgi?key=treebbs&$USERPASSURL&mode=allread&no=$no&page=$page\">◆</a> - <a href=\"action.cgi?key=treebbs&no=$no&$USERPASSURL&reno=$re&oya=$oya&mode=msgview&page=$page\">$sub</a> - <B>$nam</B> $dat";
			}

			if ($Q{no} == $no) {
				$disp.="<SPAN>No\.$no</SPAN>\n";
			} else {
				$disp.="No\.$no\n";
			}
		}
		while ($x > 0) { $disp.="</UL>\n"; $x--; }
		$disp.="</UL>\n";
	}
	$disp.=$TRE.$TBE;
}

sub msg_form {
	my($cname, $cmail, $curl, $cpwd, $cpv, $csmail);
	# 返信時
	if ($mode eq 'msgview') {
		$disp.=<<STR;
<hr width=500 noshade size=1>
<BIG>●返信フォーム</BIG><br><br>
<FORM ACTION="action.cgi" enctype="multipart/form-data" $METHOD>
$MYFORM$USERPASSFORM
<input type=hidden name=mode value="form">
<input type=hidden name=page value="$page">
<input type=hidden name=action value="res_msg">
<input type=hidden name=no value="$Q{no}">
<input type=hidden name=oya value="$Q{oya}">
STR
	# 新規時
	} else {
		my $image=GetTagImgKao("案内人","guide");
		$disp.=<<STR;
$TB$TR$TD$image
$TD◇題名は，内容が分かるようにお願いします。<br>
◇質問するときには先に図書館で調べましょう。
$TRE$TBE<br>
<FORM ACTION="action.cgi" enctype="multipart/form-data" $METHOD>
$MYFORM$USERPASSFORM
<input type=hidden name=mode value="form">
<input type=hidden name=page value="$page">
<input type=hidden name=no value="new">
STR
	}

$disp.=<<"STR";
<input type=hidden name=name value="$DT->{shopname}">
<input type=hidden name=town value="$TOWN_TITLE">
$TBT$TRT
<td nowrap><SPAN>タイトル</SPAN>
<td><input type=text name=sub size=38 value=\"$res_sub\"></td></tr>
$TRT<td nowrap><SPAN>メッセージ</SPAN><td>
<textarea name=message rows=10 cols=62 wrap=soft></textarea></tr>
STR

	my $i=0;
	foreach (@KIND){
		$select_option .= "<option value=$i>$_\n";
		$i++;
	}

$disp.=<<"EOM";
$TRT<td nowrap><SPAN>発言種類</SPAN></td><td><select name=smail>
$select_option
</select></tr>$TBE
<input type=submit value=" 記事を投稿する ">
</form>
EOM
}

sub auto_link
{
	$_[0] =~ s/([^=^\"]|^)(https?\:\/\/[\w\.\~\-\/\?\&\=\;\#\:\%\+\@]+)/$1<a href='$2' target='_blank'>$2<\/a>/g;
}

sub cut_subject
{
	if (length($_[0]) <= 40) { return $_[0]; }
	$cut = substr($_[0],0,40);
	chop $cut if $cut=~ /^(?:(?:[\x81-\x9F|\xE0-\xEF][\x40-\x7E|\x80-\xFC])|(?:[\x20-\x7E\xA0-\xDF]))*.$/;
	return $cut;
}
