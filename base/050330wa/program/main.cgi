# 店長室 2004/01/20 由來

Turn();
DataRead();
CheckUserPass();
($Q{ck} ? SetCookie($Q{nm},$Q{pw}) : SetCookie("","")) if $Q{pw};

if (!$MOBILE)
	{
	RequireFile('inc-main.cgi');
	$disp.="<BR>",RequireFile('inc-sc.cgi');
	}
	else
	{
	RequireFile('inc-info.cgi');
	}
$disp.="<BR>";
ReadLog($DT->{id},0,'',$DT->{shopname});
RequireFile('inc-html-log.cgi');

OutSkin();
1;

sub SetCookie
{
	my($nm,$pw)=@_;
	my $time=$nm ne "" ? $NOW_TIME+($EXPIRE_TIME<60*60*24*365 ? $EXPIRE_TIME*2 : 60*60*24*365) : 0;
	my($sec,$min,$hour,$mday,$mon,$year,$wday)=gmtime($time);
	my $expire=
		sprintf("%s, %02d-%s-%04d %02d:%02d:%02d GMT",
			('Sunday','Monday','Tuesday','Wednesday',
			 'Thursday','Friday','Saturday')[$wday],
			$mday,
			('Jan','Feb','Mar','Apr','May','Jun',
			 'Jul','Aug','Sep','Oct','Nov','Dec')[$mon],
			$year+1900,
			$hour,
			$min,
			$sec
		);
	print "Set-Cookie: USERNAME=$nm; expires=$expire;\n";
	print "Set-Cookie: PASSWORD=$pw; expires=$expire;\n";
	#print "Set-Cookie: shop=;\n";
}
