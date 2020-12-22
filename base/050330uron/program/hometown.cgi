# 住宅街 2004/01/20 由來

DataRead();
CheckUserPass();

# 画像定義
DevelopImage();
RequireFile('inc-hometown.cgi');
CheckBride();

my $Street=int(($#Pcode -4) / 4);
my $Pnum=($Street * 4) + 7;
foreach(0..$Pnum)
	{
	$image[$_]=$tree,next if !$Pcode[$_];
	$image[$_]=$place[$Pcode[$_]];
	}

# ふきだし系
CharaDefine();
StyleDefine();

$disp.=<<"HTML";
<table class=t cellpadding=0 cellspacing=0>
$TRT$TD$image[0]$TD$image[1]
<TD class="rb" align="center">
$TD$image[2]$TD$image[3]$TRE
HTML

foreach(0..$Street) {
	my $n=($_ * 4)+4;
	my $m=($_ * 3);
	$disp.=$TRT.'<TD height=32 colspan=2 align=right class="ra">'.$chara[$m];
	$disp.='<TD width=32 class="rc"><TD colspan=2 class="ra">'.$chara[$m+1].$TRE."\n";
	$disp.=$TRT.$TD.$image[$n].$TD.$image[$n+1]."\n";
	$disp.='<TD class="rb" align="center">'.$chara[$m+2];
	$disp.=$TD.$image[$n+2].$TD.$image[$n+3].$TRE."\n";
	}
$disp.=$TBE;
OutSkin();
1;


sub StyleDefine
{
	my $ii=<<'HTML';
<Style Type="text/css">
<!--
HTML
	my $i=<<"HTML";
<Style Type="text/css">
<!--
acronym  { border-style:none;}
IMG.c {width:24; height:32}
$tdr
HTML
	$DISP{TOP} =~ s/$ii/$i/;
}

sub DevelopImage
{
$space='<IMG class="i" SRC="'.$IMAGE_URL.'/map/dummy.png">';
$vspace='<IMG WIDTH="64" HEIGHT="16" SRC="'.$IMAGE_URL.'/map/dummy.png">';
$arrow='<IMG class="i" SRC="'.$IMAGE_URL.'/map/maparrow.png">';
$tree=qq|<IMG WIDTH="128" HEIGHT="80" SRC="$IMAGE_URL/map/tree1.png">|;
if ($STATE->{develop} > 6500)
	{
	$tree=qq|<IMG WIDTH="128" HEIGHT="80" SRC="$IMAGE_URL/map/tree2.png">|;
	$tdr="TD.ra {background-image : url($IMAGE_URL/map/maproad3a.png);}\n"
		."TD.rb {background-image : url($IMAGE_URL/map/maproad3b.png);}\n"
		."TD.rc {background-image : url($IMAGE_URL/map/maproad3c.png);}";
	}
	elsif ($STATE->{develop} > 5500)
	{
	$tdr="TD.ra {background-image : url($IMAGE_URL/map/maproad2a.png);}\n"
		."TD.rb {background-image : url($IMAGE_URL/map/maproad2b.png);}\n"
		."TD.rc {background-image : url($IMAGE_URL/map/maproad2c.png);}";
	}
	else
	{
	$tdr="TD.ra {background-image : url($IMAGE_URL/map/maproad1a.png);}\n"
		."TD.rb {background-image : url($IMAGE_URL/map/maproad1b.png);}\n"
		."TD.rc {background-image : url($IMAGE_URL/map/maproad1c.png);}";
	}
}

sub TagChara
{
	my($ii,$i)=@_;
	return qq|<acronym title="$ii"><IMG class="c" SRC="$IMAGE_URL/map/c-b$i.png"></acronym>|;
}

sub CheckBride
{
	undef @place;
	my @buf = sort { $b <=> $a } @Pcode;
	my $MAXADD=$buf[0];
	$place[100]=$space.GetMenuTag('bride','<acronym title="教会"><IMG WIDTH=112 HEIGHT=80 SRC="'.$IMAGE_URL.'/map/house1d.png"></acronym>');

	my @BRIDEnamelist=qw(
		no tm mode ida idb stbase ctbase money place reform
		);
	open(IN,GetPath('bride'));
	my @bride=<IN>;
	close(IN);
	my $married=0;
	foreach my $cnt(0..$#bride)
		{
		chop $bride[$cnt];
		my @buf=split(/,/,$bride[$cnt]); my $i=0;
		foreach (@BRIDEnamelist) { $BRIDE[$cnt]->{$_}=$buf[$i];$i++;}
		undef $BRIDE[$cnt],next if !defined($id2idx{$BRIDE[$cnt]->{ida}}) || !defined($id2idx{$BRIDE[$cnt]->{idb}});	# 閉店，移転による消滅。
		if ($BRIDE[$cnt]->{place})
			{
			my $n=$DT[$id2idx{$BRIDE[$cnt]->{ida}}]->{name}."&".$DT[$id2idx{$BRIDE[$cnt]->{idb}}]->{name}."宅";
			$place[$BRIDE[$cnt]->{place}]=qq|<acronym title="$n"><IMG WIDTH="128" HEIGHT="80" SRC="$IMAGE_URL/map/house2$BRIDE[$cnt]->{reform}.png"></acronym>|;
			$place[$BRIDE[$cnt]->{place}]=GetMenuTag('bride',$place[$BRIDE[$cnt]->{place}],'&no='.$BRIDE[$cnt]->{no}) if ($DT->{id} == $BRIDE[$cnt]->{ida}) || ($DT->{id} == $BRIDE[$cnt]->{idb});
			next;
			}
		$married=$BRIDE[$cnt]->{no} if ($DT->{id} == $BRIDE[$cnt]->{ida}) || ($DT->{id} == $BRIDE[$cnt]->{idb});
		}
	foreach(101..$MAXADD)
		{
		next if $place[$_];
		$place[$_]='<acronym title="住宅用地"><IMG WIDTH="128" HEIGHT="80" SRC="'.$IMAGE_URL.'/map/housez.png"></acronym>';
		$place[$_]=GetMenuTag('bride',$place[$_],'&form='.$_.'&idx='.$married) if $married;
		}
}

