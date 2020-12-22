# 掲示板 2004/01/20 由來

$NOITEM=1;
CoLock() if ($Q{mode} eq "form");
DataRead();
CheckUserPass();
RequireFile('inc-treebbs.cgi');
$datafile=GetPath($COMMON_DIR,"treelog");

# データの分析
$mode = $Q{mode} , $mode||="list";
$page = $Q{page};
if ($page eq "") { $page = 0; }
while ($Q{message} =~ /<br>$/) { $Q{message} =~ s/<br>$//g; }

$disp.=GetMenuTag('treebbs',	'[記事一覧]')
	.GetMenuTag('treebbs',	'[新規投稿]','&mode=formview');
$disp.="<hr width=500 noshade size=1>";

$disp.="<BIG>●掲示板</BIG><br><br>";

%filename=qw(form edit msgview view allread all formview view list list);
my $functionname=$filename{$mode};
$functionname||="list";

RequireFile("inc-treebbs-$functionname.cgi");
OutSkin();
1;


sub GetQueryBBS
{
	my $q;
	$ENV{REQUEST_METHOD} eq "POST" ? read(STDIN,$q,$ENV{CONTENT_LENGTH}) : ($q=$ENV{QUERY_STRING});
	return if length($q)<=1;

	my $key;
	undef %Q;
	require $JCODE_FILE;
	foreach(split(/&/,$q))
	{
		($key, $val) = split(/=/);
		$val =~ tr/+/ /;
		$val =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

		# S-JIS変換
		&jcode'convert(*val, "sjis", "", "z");

		$val =~ s/&/&amp;/g;
		$val =~ s/</&lt;/g;
		$val =~ s/>/&gt;/g;
		$val =~ s/"/&quot;/g;

		if ($key ne "message") {
			$val =~ s/\r//g;
			$val =~ s/\n//g;
		}
		$Q{$key} .= "\0" if (defined($Q{$key}));
		$Q{$key} .= $val;
	}
	@Q{qw(nm pw ss)}=split(/!/,$Q{u},3) if exists $Q{u};


	$Q{message} =~ s/\r\n/<br>/g;
	$Q{message} =~ s/\r/<br>/g;
	$Q{message} =~ s/\n/<br>/g;
}
