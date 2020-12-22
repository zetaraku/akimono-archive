# 城下町 2004/01/20 由來

DataRead();
CheckUserPass(1);

# 画像定義
DevelopImage();
RequireFile('inc-town.cgi');

my $Street=int(($#Pname -2) / 4);
my $Pnum=($Street * 4) + 5;
foreach(0..$Pnum)
	{
	$image[$_]=$Pimage[$_];
	$image[$_]||=$tree;
	$image[$_]=qq|<acronym title="$Pname[$_]">|.$image[$_]."</acronym>" if $Pname[$_];
	my $link=($GUEST_USER ? $Pguest[$_]:$Plink[$_]);
	$image[$_]=(($link =~ /\./) ? GetTagA($image[$_],$link,0,"_blank") : GetMenuTag($link,$image[$_])) if $link;
	}

# ふきだし系
CharaDefine();
StyleDefine();

$disp.=<<"HTML";
<table class=t cellpadding=0 cellspacing=0>
$TRT$TD$image[0]<td colspan=3 align=center>$img_ex[0]$TD$image[1]$TRE
$TRT<TD height=32 colspan=2 align=right class="ra">$chara[0]<TD width=32 class="rc"><TD colspan=2 class="ra">$chara[1]$TRE
HTML
foreach(0..$Street) {
	my $n=($_ * 4)+2;
	my $m=($_ * 3)+2;
	$disp.=$TRT.$TD.$image[$n].$TD.$image[$n+1]."\n";
	$disp.='<TD class="rb" align="center">'.$chara[$m];
	$disp.=$TD.$image[$n+2].$TD.$image[$n+3].$TRE."\n";
	$disp.=$TRT.'<TD height=32 colspan=2 align=right class="ra">'.$chara[$m+1];
	$disp.='<TD width=32 class="rc"><TD colspan=2 class="ra">'.$chara[$m+2].$TRE."\n";
	}
$disp.=<<"HTML";
$TRT<td colspan=2 align="right">$img_ex[1]
<td colspan=3>
HTML

LoginMember();
$disp.=$TRE.$TBE;

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
$vspace='<IMG WIDTH="48" HEIGHT="16" SRC="'.$IMAGE_URL.'/map/dummy.png">';
$i[1]=qq|<IMG WIDTH=96 HEIGHT=80 SRC="$IMAGE_URL/map/mapshop.png">|;
$i[2]=qq|<IMG WIDTH=240 HEIGHT=80 SRC="$IMAGE_URL/map/consul.png">|;
$i[2]=qq|<IMG WIDTH=240 HEIGHT=80 SRC="$IMAGE_URL/map/consul2.png">| if ($DTevent{rebel});
$tree=qq|<IMG WIDTH=128 HEIGHT=80 SRC="$IMAGE_URL/map/tree1.png">|;
$img_ex[0]=GetMenuTag('lord','<acronym title="領主邸">'.$i[2].'</acronym>');
$img_ex[1]=GetMenuTag('shop-a','<acronym title="商店通り"><IMG WIDTH="96" HEIGHT="80" SRC="'.$IMAGE_URL.'/map/mapshop.png"><IMG WIDTH="96" HEIGHT="80" SRC="'.$IMAGE_URL.'/map/mapshop.png"></acronym>');

if ($STATE->{develop} > 4500)
	{
	$i[0]=qq|<IMG WIDTH=112 HEIGHT=80 SRC="$IMAGE_URL/map/house1a.png">|;
	}
	else
	{
	$i[0]=qq|<IMG WIDTH=112 HEIGHT=80 SRC="$IMAGE_URL/map/house1b.png">|;
	}
if ($STATE->{develop} > 6500)
	{
	$tree=qq|<IMG WIDTH=128 HEIGHT=80 SRC="$IMAGE_URL/map/tree2.png">|;
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
	return qq|<acronym title="$ii"><IMG class="c" SRC="$IMAGE_URL/map/c-a$i.png"></acronym>|;
}

sub LoginMember
{
my $logmemb="";
foreach(@DT)
	{
	next if ($_->{lastlogin} < $NOW_TIME - 600);
	$logmemb .= $_->{shopname}."， ";
	}
$logmemb = substr($logmemb,0,(length($logmemb)-3)) if ($logmemb);
$logmemb = "なし" if !$logmemb;

$disp.=<<"HTML";
<table width=256>$TR$TDB<small>現在活動中の店</small>$TRE
$TR$TD<small>$logmemb</small>$TRE$TBE
HTML
}

