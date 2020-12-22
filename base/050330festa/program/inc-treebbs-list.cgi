# 掲示板一覧表示 2003/09/25 由來

Treelist();
&move_list;
1;

sub Treelist
{
my($no,$reno,$lx,$sub,$town,$name,$msg,$t,$h,$oya);

$disp.=<<"EOM";
$TB$TR$TDB No.
$TDB Title
$TDB Name
$TDB Town
$TDB Date
$TDB etc.$TRE
EOM

	$i=0;
	open(IN,$datafile) or return();
	if ($mode ne "past") { $top = <IN>; }
	while (<IN>) {
		($no,$reno,$lx,$sub,$town,$name,$msg,$t,$h,$oya,$sml) = split(/<>/);
		if ($reno == 0) { $i++; }
		if ($i < $page + 1) { next; }
		if ($i > $page + $p_tree) { next; }

		$disp.=($name eq $adminname) ? $TR.$TDB : $TR.$TD;
		$disp.=$no.$TD;
		$disp.="├" if ($lx==1);
		$disp.="│　└" if ($lx > 1);
		my $newsign="";
		$newsign = " ".$newmark if ($NOW_TIME - $t < $new_time * 3600);
		$sub = &cut_subject($sub);

		# レス記事
		if ($lx != 0) {
			$disp.="◇<a href=\"action.cgi?key=treebbs&$USERPASSURL&no=$no&reno=$reno&oya=$oya&mode=msgview&page=$page\">$sub</a>$newsign\n";
		# 親記事
		} else {
			$disp.="<a href=\"action.cgi?key=treebbs&$USERPASSURL&mode=allread&no=$no&page=$page\">◆</a>";
			$disp.="<a href=\"action.cgi?key=treebbs&$USERPASSURL&no=$no&reno=$reno&oya=$oya&mode=msgview&page=$page\">$sub</a>$newsign\n";
		}
	$disp.=$TD.$name.$TD.$town.$TD."<small>".GetTime2FormatTime($t)."<small>".$TD.$VALUE[$sml]."\n";
	}
	close(IN);
	$disp.=$TRE.$TBE;
}

sub move_list {
	my $next = $page + $p_tree;
	my $back = $page - $p_tree;
	$disp.="<P><table cellpadding=0 cellspacing=0><tr>\n";
	if ($back >= 0) {
		$disp.="<td><FORM ACTION=\"action.cgi\" $METHOD>$MYFORM$USERPASSFORM\n";
		$disp.="<input type=hidden name=page value=\"$back\">\n";
		$disp.="<input type=hidden name=list value=\"$Q{list}\">\n";
		$disp.="<input type=submit value=\"前ページ\"></td></form>\n";
	}
	if ($next < $i) {
		$disp.="<td><FORM ACTION=\"action.cgi\" $METHOD>$MYFORM$USERPASSFORM\n";
		$disp.="<input type=hidden name=page value=\"$next\">\n";
		$disp.="<input type=hidden name=list value=\"$Q{list}\">\n";
		$disp.="<input type=submit value=\"次ページ\"></td></form>\n";
	}
	$disp.="<td width=10></td><td class=num>";

	$x=1;
	$y=0;
	while ($i > 0) {
		if ($page eq $y) { $disp.="<b>[$x]</b>\n"; }
			else { $disp.="[<a href=\"action.cgi?key=treebbs&$USERPASSURL&page=$y&list=$Q{list}\">$x</a>]\n"; }
		$x++;
		$y = $y + $p_tree;
		$i = $i - $p_tree;
	}
	$disp.="</td></tr></table><br>\n";
}

sub cut_subject
{
	if (length($_[0]) <= 40) { return $_[0]; }
	$cut = substr($_[0],0,40);
	chop $cut if $cut=~ /^(?:(?:[\x81-\x9F|\xE0-\xEF][\x40-\x7E|\x80-\xFC])|(?:[\x20-\x7E\xA0-\xDF]))*.$/;
	return $cut;
}
