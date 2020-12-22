# 掲示板全記事表示 2003/11/03 由來

&allread;
1;


sub allread {
	my($no,$re,$lx,$sub,$eml,$nam,$msg,$t,$ho,$oya,$sml,$date);

	$x=0;
	$disp.="<table width=500>$TR$TD<BIG>▼レス全表\示</BIG>\n";
	$disp.="<UL>\n";
	open(IN,$datafile) or return();
	$top = <IN>;
	$flag=0;
	while (<IN>) {
		($no,$re,$lx,$sub,$eml,$nam,$msg,$lt,$ho,$oya,$sml) = split(/<>/);
		if ($Q{no} == $oya) {
			$flag=1;
			push(@new,$_);

			while ($x > $lx) { $disp.="</UL>\n"; $x--; }
			while ($x < $lx) { $disp.="<UL>\n"; $x++; }

			$sub = &cut_subject($sub);

			$disp.="<LI><a href=\"#$no\">$sub</a> - <B>$nam</B> $dat <font color=\"$no_color\">No\.$no</font>\n";
		}
		elsif ($flag && $Q{no} != $oya) { last; }
	}
	close(IN);
	while ($x > 0) { $disp.="</UL>\n"; $x--; }
	$disp.="</UL>$TRE$TBE\n";

	foreach (@new) {
		($no,$re,$lx,$sub,$eml,$nam,$msg,$lt,$ho,$oya,$sml) = split(/<>/);

		&auto_link($msg);
		$msg =~ s/"/&quot;/g;
		$date = GetTime2FormatTime($lt);
$disp.=<<HTML;
<hr width=500 size=1><table width=500 id="$no">
$TR$TDB■ $sub$TRE
$TR$TD<SPAN>発言者</SPAN>：<b> $nam</b> $eml<br>
<SPAN>発言日</SPAN>： $date$TRE
$TR$TD◇
<blockquote>$msg</blockquote>
</td></tr></table>
HTML
	}
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
