# アイテムデータ生成 2005/03/30 由來
# ** --- makeitem.cgi,v 1.39 2002/12/02 13:05:10 mu Exp $

# 変数初期化
$g_define={};
$g_define->{itemusetimerate}=1;
$g_define->{function}={};
$g_define->{localfuncmark}='_local_';
$g_define->{cmdhead}='@@';
$g_define->{cmdfoot}='';
$linecount=0;
($MYDIR,$MYNAME)=($ENV{SCRIPT_NAME}=~/^.*\/([^\/]+)\/([^\/]+)$/); # 自ファイル名/ディレクトリ名
$g_define->{dirname}=$MYDIR; # 設置ディレクトリ名(@@if等で利用可)

OutError('管理者パスワードが不正です') if $Q{admin} ne $MASTER_PASSWORD;
OutHeader();
$mode=$Q{mode};

print "</center>\n";
print <<"HTML" if $ENV{HTTP_REFERER} ne '';
	<FORM ACTION="$ENV{HTTP_REFERER}" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=admin VALUE="$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="管理メニューへ戻る">
	</FORM>
HTML

if(!-e "./lock" and !-e "$DATA_DIR/lock")
{
	print("自動的にメンテモードに移行できませんでした。手動でメンテモードにしてから再生成お願いします。"),exit
		if !mkdir("$DATA_DIR/lock",$DIR_PERMISSION);
	$LOCK_AUTO_MAKE=1;
	sleep(1); # 念のためwait
}

DeleteItemData();                          # 一旦古いアイテムデータを消す
print("deleted"),exit if $mode eq 'delete'; # アンインストモードなら終了

# アイテムディレクトリ作成
mkdir("$ITEM_DIR",$DIR_PERMISSION);
mkdir("$ITEM_DIR/event",$DIR_PERMISSION);
mkdir("$ITEM_DIR/event-s",$DIR_PERMISSION);
mkdir("$ITEM_DIR/event-e",$DIR_PERMISSION);
mkdir("$ITEM_DIR/event-n",$DIR_PERMISSION);
mkdir("$ITEM_DIR/use",$DIR_PERMISSION);
mkdir("$ITEM_DIR/use-s",$DIR_PERMISSION);
mkdir("$ITEM_DIR/item-t",$DIR_PERMISSION);
mkdir("$ITEM_DIR/item-s",$DIR_PERMISSION);
mkdir("$ITEM_DIR/item-b",$DIR_PERMISSION);

AnalyzeItemData("FH00","inc-item-data.cgi");  # inc-item-data.cgi解析
AnalyzeItemData("FH00","inc-rebel-data.cgi");  # 反乱データを追加解析

OutItemData();      # item書き出し
OutEventData();     # event書き出し
OutFunctionData();  # function書き出し
OutDefineData();	# define書き出し
OutResultMessage(); # 結果 html 出力

print "</body></html>";

rmdir("$DATA_DIR/lock") if $LOCK_AUTO_MAKE;

exit;

sub GetTime
{
	my($val)=@_;
	my $tm=0;

	if(defined($g_define->{$val}))
	{
		$tm=$val=$g_define->{$val};
	}
	if($val =~ /(^[\-\d\.]+)(|[a-z]+)$/)
	{
		$tm=$1+0;
		if($2 eq 'm'){$tm*=60;}
		if($2 eq 'h'){$tm*=60*60;}
		if($2 eq 'd'){$tm*=60*60*24;}
		if($2 eq 'k'){$tm*=1000;}
	}
	return $tm;
}

sub GetNumber
{
	my($val)=@_;
	my $num=$val;
	
	if(defined($g_define->{$val}))
	{
		$num=$val=$g_define->{$val};
	}
	if($val =~ /^([\-\d\.]+)(|m|h|d|k|%)$/i)
	{
		$num=$1+0;
		if($2 eq 'm' || $2 eq 'M'){$num*=60;}
		if($2 eq 'h' || $2 eq 'H'){$num*=60*60;}
		if($2 eq 'd' || $2 eq 'D'){$num*=60*60*24;}
		if($2 eq 'k' || $2 eq 'K'){$num*=1000;}
		if($2 eq '%'){$num*=10;}
	}
	return eval($num);
}

sub GetTypeNumber
{
	my($val)=@_;
	
	my @list=grep(/^type\d+$/,keys(%{$g_define}));
	
	foreach(@list)
	{
		$_=~/^type(\d+)$/;
		return $1 if $g_define->{$_} eq $val;
	}
	
	return GetNumber($val);
}

sub GetJobCode
{
	my($val)=@_;
	
	foreach(grep(/^job-[a-z]+$/,keys %{$g_define}))
	{
		my $job=(/^job-([a-z]+)$/)[0];
		return $job if $g_define->{$_} eq $val;
		return $job if $job eq $val;
	}
	
	return 0;
}

sub GetItemNumber
{
	my($val)=@_;
	
	$val=GetString($val);
	
	return GetNumber($val) if $val =~ /^\d+$/;
	foreach(@out_item)
	{
		return $_->{no} if $_->{code} eq $val || $_->{name} eq $val;
	}
	
	push(@errormsg,"アイテム無\t".$val);
	return $val;
}

sub GetString
{
	my($val)=@_;
	my $str=$val;
	
	$str=~tr/'",\x00-\x1f//d; #'
	$str=~s/\\$/\\\\/g;
	
	$str=~s/(\(|)\$\$(\w+)(\)|)/${$2}/g;
	$str=~s/(\(|)\$(\w+)(\)|)/$g_define->{$2}/g;
	
	return $str;
}

sub GetDefineString
{
	my($val)=@_;
	
	$val=$g_define->{$val};
	$val=~s/\\$/\\\\/g;
	
	return "'$val'";
}

sub GetLine
{
	my($filehandle)=@_;
  GetLineLoop:
	my $line=<$filehandle>;
	$linecount++;
	
	if($line eq "" || $line =~ /^$g_define->{cmdhead}END$g_define->{cmdfoot}/){return "";}
	
	$line =~ s/\t|\n|\r|\s+/ /g;
	$line =~ s/([^\$\@\%])#.*$/$1/g;
	$line =~ s/^\s*#.*$//g;
	#print $line."<br>";
	while($line =~ s/ ,/,/){}
	while($line =~ s/, /,/){}
	$line =~ s/ /  /g;
	goto GetLineLoop if $line !~ /\S/;

	return " ".$line." ";
}

sub ClearBuffer
{
	my($mode)=@_;
	
	if($mode eq 'item')
	{
		$flag_price=0;
		$flag_point=0;

		$g_item={};
		$g_item->{scale}=$g_define->{scale};
		$g_item->{pricebase}=0;
		$g_item->{pricehalf}=0;
		$g_item->{plus}=0;
		$g_item->{popular}=0;
		$g_item->{point}=0;
		$g_item->{flag}='';
		#$g_item->{code}="$linecount";
		
		$g_use={};
		$g_use->{no}=-1;
		$g_use->{exptime}=0;
		
	}
	elsif($mode eq 'use')
	{
		my $time   =$g_use->{time};
		my $exptime=$g_use->{exptime};
		my $exp    =$g_use->{exp};
		my $scale  =$g_use->{scale};
		my $action =$g_use->{action};
		my $no     =$g_use->{no}+1;
		my $code   =$g_use->{code};
		my $itemno =$g_use->{itemno};
		
		$code  =$g_item->{code}  if $code eq '';
		$itemno=$g_item->{no}    if $itemno eq '';
		$scale =$g_item->{scale} if $scale eq '';
		
		$g_use={};
		$time=60*60 if !$time;
		$g_use->{time}   =0;
		#$exptime=$time if $exptime==0;
		#$g_use->{exptime}=$exptime;
		$g_use->{exptime}=0;
		$g_use->{exp}    =$exp;
		$g_use->{scale}  =$scale;
		$g_use->{action} =$action;
		
		$g_use->{no}     =$no;
		$g_use->{code}   =$code;
		$g_use->{itemno} =$itemno;
		$g_use->{use}    =[];
		$g_use->{get}    =[];
		$g_use->{localfunc}="";
		
		$g_use->{job}    =[];
	}
	elsif($mode eq 'event')
	{
		$g_event_no++;
		$g_event={};
		$g_event->{param}=[];
		$g_event->{group}=$g_event_no;
		#$g_event->{code}="$linecount";
	}
}

sub OutBuffer
{
	my($mode)=@_;
	
	if($mode eq 'item')
	{
		push(@out_item,$g_item);
	}
	elsif($mode eq 'use')
	{
		$out_use{$g_use->{code}}[$g_use->{no}]=$g_use;
	}
	elsif($mode eq 'event')
	{
		push(@out_event,$g_event);
	}
	elsif($mode eq 'define')
	{
		
	}
	return;
}

sub GetBuffer
{
	my($mode,$line)=@_;
	my $oldline="";
	
	my $STRING='"[^"]*(?:""[^"]*)*"|\S*';
	
  GetBufferLoop:
	
	$_=$line;
	study $line;
	
	if($mode eq 'define')
	{
		if($line =~ s/\sSCALE\s+(\S+)\s//i){$g_define->{scale}=GetString($1);}
		if($line =~ s/\sTYPE\s*(\d+)\s+(\S+)\s//i){$g_define->{"type$1"}=GetString($2);}
		if($line =~ s/\sSET\s+([a-zA-Z0-9_]+)\s+(\S+)\s//i){$g_define->{$1}=GetString($2);}
		if($line =~ s/\sJOB\s+([a-z]{1,10})\s+(\S+)\s//i){$g_define->{"job-$1"}=GetString($2);}
		
		if($line =~ s/\sMAXMONEY\s+(\S+)\s//i){$g_define->{maxmoney}=GetNumber($1);}
		if($line =~ s/\sTIMEEDITSHOWCASE\s+(\S+)\s//i){$g_define->{timeeditshowcase}=GetTime($1);}
		if($line =~ s/\sTIMESHOPPING\s+(\S+)\s//i){$g_define->{timeshopping}=GetTime($1);}
		if($line =~ s/\sTIMESENDITEM\s+(\S+)\s//i){$g_define->{timesenditem}=GetTime($1);}
		if($line =~ s/\sTIMESENDMONEY\s+(\S+)\s//i){$g_define->{timesendmoney}=GetTime($1);}
		if($line =~ s/\sCOSTSHOWCASE\s*(\d+)\s+(\S+)\s//i){$g_define->{"costshowcase$1"}=GetNumber($2);}
		if($line =~ s/\sTIMESENDITEMPLUS\s+(\S+)\s//i){$g_define->{timesenditemplus}=GetTime($1);}
		if($line =~ s/\sTIMESENDMONEYPLUS\s+(\d+)\s//i){$g_define->{timesendmoneyplus}=GetNumber($1);}
		if($line =~ s/\sITEMUSETIMERATE\s+(\S+)\s//i){$g_define->{itemusetimerate}=GetNumber($1);}
		
		if($line =~ s/\sVERSION\s+($STRING)\s//i)
		{
			my $version=$1;
			$version=~s/\$Revision(?:\:\s*([\d\.]+)\s*)?\$/$1/;
			$version=GetString($version);
			$g_define->{"version"}=$version;
		}
	}
	elsif($mode eq 'item')
	{
		if($line =~ s/\sNO\s+(\S+)\s//i){$g_item->{no}=GetNumber($1);}
		if($line =~ s/\sCODE\s+([\w\-]+)\s//i){$g_item->{code}=GetString($1);}
		if($line =~ s/\sTYPE\s+(\S+)\s//i){$g_item->{type}=GetTypeNumber($1);}
		if($line =~ s/\s(\\|MONEY|PRICE)\s*(\\|)(\S+)\s//i)
		{
			$g_item->{price}=GetNumber($3);
			$flag_price=1;				#価格が設定された

			# 価格が存在するときは標準値を自動設定
			if ($g_item->{price} > 0)
				{
				#倉庫最大数
					if (!$g_item->{limit})
					{
				$g_item->{limit}=int(1000000 / $g_item->{price});
				$g_item->{limit}=1 if $g_item->{limit} < 1;		#最低値
				$g_item->{limit}=2000 if $g_item->{limit} > 2000;	#最高値
				$g_item->{limit}=int($g_item->{limit} / 10 + 0.5)*10 if $g_item->{limit}>100;	#10より大きいときは四捨五入

				#倉庫最大数が設定されたので，市場最大数も自動設定
				$g_item->{wslimit}=$g_item->{limit};
					}

				#維持費
				$g_item->{cost}=int($g_item->{price}/10) if !$g_item->{cost};

				#売れ行き
					if (!$g_item->{popular})
					{
				$g_item->{popular}=int($g_item->{price} *2*6*6/10);

				#売れ行きが設定されたので，人気標準値も自動設定
				$g_item->{point}=int($g_item->{popular} * 100 / 24 / 36);
					}
				}
		}

		if($line =~ s/\sPOP\s+(\S+)\s//i)
		{
			push(@errormsg,"$NOW_FILENAME ($linecount) pointより前の行にpopを記述してください") if $flag_point;
			my $num=$1;
			if($num =~ /^lv([\d\.]+)$/i)
				{
				push(@errormsg,"$NOW_FILENAME ($linecount) popより前の行にpriceを記述してください") if !$flag_price;
				if ($1 > 0)
					{
					$g_item->{popular}=int($g_item->{popular}/ $1 * 5);	#レベル指定（計算式逆になる）
					$g_item->{popular}=1 if ($g_item->{popular}<1);
					}
					else
					{
					$g_item->{popular}=0;
					}
				}
				else
				{
				$g_item->{popular}=GetTime($num);
				}
			#売れ行きが設定されたので，人気標準値も自動設定
			$g_item->{point}=int($g_item->{popular} * 100 / 24 / 36);
		}

		if($line =~ s/\s(POINT)\s+(\S+)\s//i)
		{
			my $num=$2;
			if($num =~ /^lv([\-\d\.]+)$/i)
				{
				push(@errormsg,"$NOW_FILENAME ($linecount) pointより前の行にpriceまたはpopを記述してください") if (!$g_item->{point} &&  !$flag_price);
				$g_item->{point}=int($g_item->{point}* $1 / 5);	#レベル指定
				}
				else
				{
				$g_item->{point}=GetNumber($num);
				}
			$flag_point=1;					#人気が設定された
		}

		if($line =~ s/\s(COST)\s*(\\|)(\S+)\s//i){$g_item->{cost}=GetNumber($3);}
		if($line =~ s/\sBASE\s+(\S+)\s*\/(\S+)\s//i){$g_item->{pricebase}=GetNumber($1);$g_item->{'pricehalf'}=GetNumber($2);}

		if($line =~ s/\sPLUS\s+(\S+)\s//i){$g_item->{plus}=GetTime($1);}
		if($line =~ s/\sSCALE\s+(\S+)\s//i){$g_item->{scale}=GetString($1);}
		if($line =~ s/\sPARAM\s+(\S+)\s//i){$g_item->{param}=GetString($1);}
		if($line =~ s/\sNAME\s+(\S+)\s//i){$g_item->{name}=GetString($1);}
		if($line =~ s/\sINFO\s+(\S+)\s//i){$g_item->{info}=GetString($1);}
		if($line =~ s/\sLIMIT\s+(\S+)\s//i)
		{
			my @val=split(/\//,$1);
			if($val[0] =~ /^lv([\d\.]+)$/i)
				{
				$g_item->{limit}=int($g_item->{limit}* $1 / 5);	#レベル指定
				}
				elsif ($val[0])
				{
				$g_item->{limit}=GetNumber($val[0]);
				}
			$g_item->{wslimit}=$g_item->{limit} if $val[1]eq'';
			$g_item->{wslimit}=GetNumber($val[1]) if $val[1]ne'';
		}
		
		if($line =~ s/\sFUNC\s+(\S+)\s//i)
		{
			my $name=$1;
			($g_item->{func},$g_item->{localfunc})=GetLocalFunction($name,"");
		}
		if($line =~ s/\sFUNCT\s+(\S+)\s//i)
		{
			my $name=$1;
			($g_item->{functurn},$g_item->{localfuncturn})=GetLocalFunction($name,"");
		}
		if($line =~ s/\sFUNCS\s+(\S+)\s//i)
		{
			my $name=$1;
			($g_item->{funcsale},$g_item->{localfuncsale})=GetLocalFunction($name,"");
		}
		if($line =~ s/\sFUNCB\s+(\S+)\s//i)
		{
			my $name=$1;
			($g_item->{funcbuy},$g_item->{localfuncbuy})=GetLocalFunction($name,"");
		}
		
		if($line =~ s/\sFLAG\s+(\S+)\s//i)
		{
			my $flag=$1;
			my @flag=();
			push(@flag,'s') if $flag=~/\bnoshowcase\b/; # s 陳列不可
			push(@flag,'r') if $flag=~/\bnorequest\b/;  # r 依頼不可
			push(@flag,'o') if $flag=~/\bonlysend\b/;   # o 依頼は出品のみ
			push(@flag,'t') if $flag=~/\bnotrash\b/;    # t 破棄不可
			push(@flag,'h') if $flag=~/\bhuman\b/;      # h ヒューマノイド
			$g_item->{flag}=join("",@flag);
		}
	}
	elsif($mode eq 'use')
	{
		if($line =~ s/\sCODE\s+(\S+)\s//i){$g_use->{code}=GetString($1);}
		if($line =~ s/\sNO\s+(\d+)\s//i){$g_use->{no}=GetNumber($1);}
		if($line =~ s/\s(\\|MONEY|PRICE)\s*(\\|)(\S+)\s//i){$g_use->{money}=GetNumber($3);}
		if($line =~ s/\sTIME\s+(\S+)\s//i){$g_use->{time}=int(GetNumber($1)*$g_define->{itemusetimerate}); $g_use->{exptime}=$g_use->{time} if $g_use->{exptime}==0}
		if($line =~ s/\sARG\s+(\S+)\s//i){$g_use->{arg}=GetString($1);}
		if($line =~ s/\sARGMESSAGE\s+(\S+)\s//i){$g_use->{argmessage}=GetString($1);}
		if($line =~ s/\sARGSELECT\s+(\S+)\s//i){$g_use->{argselect}=GetString($1);}
		if($line =~ s/\sSCALE\s+(\S+)\s//i){$g_use->{scale}=GetString($1);}
		if($line =~ s/\sACTION\s+(\S+)\s//i){$g_use->{action}=GetString($1);}
		if($line =~ s/\sNAME\s+(\S+)\s//i){$g_use->{name}=GetString($1);}
		if($line =~ s/\sINFO\s+(\S+)\s//i){$g_use->{info}=GetString($1);}
		if($line =~ s/\sEXP\s+(\S+)\s//i){$g_use->{exp}=GetNumber($1);}
		if($line =~ s/\sEXPTIME\s+(\S+)\s//i){$g_use->{exptime}=int(GetNumber($1)*$g_define->{itemusetimerate});}
		if($line =~ s/\sPARAM\s+(\S+)\s//i){($g_use->{param1},$g_use->{param2},$g_use->{param3},$g_use->{param4})=split(/,/,$1);}
		if($line =~ s/\sNEEDEXP\s+(\S+)\s//i){$g_use->{needexp}=GetNumber($1);}
		if($line =~ s/\sNEEDJOB\s+(\S+)\s//i){$g_use->{needjob}=GetJobCode($1);}
		if($line =~ s/\sNEEDPOINT\s+(\S+)\s//i){$g_use->{needpoint}=GetNumber($1);}
		if($line =~ s/\sNEEDEVENT\s+(\S+)\s//i){$g_use->{needevent}=GetString($1);}
		if($line =~ s/\sNEEDPOP\s+(\S+)\s//i){$g_use->{needpop}=(GetNumber($1) * 10);}
		
		if($line =~ s/\sFUNC\s+(\S+)\s//i)
		{
			my $name=$1;
			($g_use->{func},$g_use->{localfunc})=GetLocalFunction($name,$g_use->{no}+1);
		}
		if($line =~ s/\sFUNCB\s+(\S+)\s//i)
		{
			my $name=$1;
			($g_use->{funcbefore},$g_use->{localfuncbefore})=GetLocalFunction($name,"b".($g_use->{no}+1));
		}
		if($line =~ s/\sFUNCI\s+(\S+)\s//i)
		{
			my $name=$1;
			($g_use->{funcinfo},$g_use->{localfuncinfo})=GetLocalFunction($name,"i".($g_use->{no}+1));
		}
		
		if($line =~ s/\s(USE|GET|NEED)\s+([^:]+)//i)
		{
			my @val=split(/\s+/,$2); #,$3,$4,$5);
			my $idx=$1;
			if($val[2]eq''){$val[2]=1000;}
			if($idx=~/need/i){$idx="use"; $val[2]=0;}
			foreach(0,2){$val[$_]=GetNumber($val[$_]);}
			$val[1]=$val[1];
			push(@{$g_use->{$idx}},join("\t",@val));
		}
		
		if($line =~ s/\sOKMSG\s+(\S+)\s//i){$g_use->{okmsg}=GetString($1);}
		if($line =~ s/\sNGMSG\s+(\S+)\s//i){$g_use->{ngmsg}=GetString($1);}
	
		if($line =~ s/\sJOB\s+(\S+)\s+(\S+)\s//i)
		{
			push(@{$g_use->{job}},$1."\t".$2);
		}
	}
	elsif($mode eq 'event')
	{
		if($line =~ s/\sGROUP\s+(\S+)\s//i){$g_event->{group}=GetString($1);}
		if($line =~ s/\sCODE\s+(\S+)\s//i){$g_event->{code}=GetString($1);}
		if($line =~ s/\sSTART\s+(\S+)\s//i){$g_event->{startproba}=GetNumber($1);}
		if($line =~ s/\sSTARTFUNC\s+(\S+)\s//i)
		{
			my $name=$1;
			($g_event->{startfunc},$g_event->{localfuncstart})=GetLocalFunction($name,'start');
		}
		if($line =~ s/\sENDFUNC\s+(\S+)\s//i)
		{
			my $name=$1;
			($g_event->{endfunc},$g_event->{localfuncend})=GetLocalFunction($name,'end');
		}
		if($line =~ s/\sBASETIME\s+(\S+)\s//i){$g_event->{basetime}=GetTime($1);}
		if($line =~ s/\sPLUSTIME\s+(\S+)\s//i){$g_event->{plustime}=GetTime($1);}
		if($line =~ s/\sINFO\s+(\S+)\s//i){$g_event->{info}=GetString($1);}
		if($line =~ s/\sSTARTMSG\s+(\S+)\s//i){$g_event->{startmsg}=GetString($1);}
		if($line =~ s/\sENDMSG\s+(\S+)\s//i){$g_event->{endmsg}=GetString($1);}
		
		if($line =~ s/\sPARAM\s+(\S+)\s+(\S+)\s//i)
		{
			push(@{$g_event->{param}},$1."\t".$2);
		}
		if($line =~ s/\sFUNC\s+(\S+)\s//i)
		{
			my $name=$1;
			($g_event->{nowfunc},$g_event->{localfuncnow})=GetLocalFunction($name,'now');
		}
	}
	elsif(substr($mode,0,4) eq 'func')
	{
		$line=~s/^\s*//g;
		$line=~s/\s*$//g;
		$g_define->{function}->{$mode}.=$line." ";
		$line="";
	}
	
	if($line =~ /\S/)
	{
		if($oldline eq $line)
			{push(@errormsg,"$NOW_FILENAME ($linecount) ".$line);}
		else
			{$oldline=$line; goto GetBufferLoop;}
	}
}

sub DeleteItemData
{
	delete_dir($ITEM_DIR,1);
}

sub delete_dir
{
	my($dir,$owndelete)=@_;
	
	return if !-d $dir;
	
	opendir(DIR,$dir);
	my @filelist=grep(!/^\.\.?$/,readdir(DIR));
	closedir(DIR);
	foreach my $file (@filelist)
	{
		$file="$dir/$file";
		unlink($file) if -f $file;
		delete_dir($file,1) if -d $file;
	}
	rmdir($dir) if $owndelete;
}


sub GetFileList
{
	opendir(DIR,$_[0]);
	my @list=map{$_[0]."/".$_}grep(/$_[1]/ && !/^\.\.?$/,readdir(DIR));
	closedir(DIR);
	
	return @list;
}

sub AnalyzeItemData
{
	my($filehandle,$filename)=@_;
	push(@errormsg,$filename.' がループしています'),return if $analyzefile{$filename}; # @@includeループを検出した場合は読み込み中止
	$analyzefile{$filename}=1;
	$filehandle++;
	push(@errormsg,$filename.' がオープン出来ませんでした'),return if !open($filehandle,"$CUSTOM_DIR/$filename") && !open($filehandle,"$INCLUDE_DIR/$filename");
	$analyzeoldmode=-1 if !defined($analyzeoldmode);
	$analyzemode=''    if !defined($analyzemode);
	$analyzeskip=0     if !defined($analyzeskip);
	$NOW_FILEHANDLE=$filehandle;
	$NOW_FILENAME=$filename;
	$linecount=0;
	while(my $line=GetLine($filehandle))
	{
		if($line=~s/^\s*$g_define->{cmdhead}if$g_define->{cmdfoot}\s+(\w+)\s*(==|!=|ne|eq)\s*\"?(\w*)\"?//i)
		{
			my($key,$op,$val)=($1,$2,$3);
			next if  $op eq '=='   && $g_define->{$key} != $val;
			next if  $op eq '!='   && $g_define->{$key} == $val;
			next if  $op =~ /eq/i  && $g_define->{$key} ne $val;
			next if  $op =~ /ne/i  && $g_define->{$key} eq $val;
			#push(@errormsg,"$NOW_FILENAME ($linecount) ".$key.$op.$val);
		}
		
		if($line=~/^\s*$g_define->{cmdhead}SKIP$g_define->{cmdfoot}\s*$/i)
		{
			$analyzeskip++;
			next;
		}
		
		if($line=~/^\s*$g_define->{cmdhead}ENDSKIP$g_define->{cmdfoot}\s*$/i)
		{
			$analyzeskip--;
			$analyzeskip=0 if $analyzeskip<0;
			next;
		}
		
		next if $analyzeskip;
		
		if($line=~s/^\s*$g_define->{cmdhead}SETMACRO$g_define->{cmdfoot}\s+(\w+)\s+(["'|])(.+)\2//i) #"
		{
			$analyzemacro{$1}=$3;
		}
		$line=~s/^\s*$g_define->{cmdhead}USEMACRO$g_define->{cmdfoot}\s*(\w+)\s*/$analyzemacro{$1}/i;
		
		if($line=~/^\s*$g_define->{cmdhead}(ITEM|USE|EVENT|DEFINE|FUNC(?:ITEM|EVENT|BASE|UPDATE|INIT|TURN|CUSTOM|NEW|SHOPIN|SHOPOUT|SALE|BUY))$g_define->{cmdfoot}\s+(.*)$/i)
		{
			OutBuffer($analyzeoldmode) if $analyzeoldmode!=-1;
			$line=" ".$2." ";
			$analyzemode=$1;
			$analyzemode=~tr/A-Z/a-z/;
			$analyzeoldmode=$analyzemode;
			ClearBuffer($analyzemode);
		}
		
		if($line=~/^\s*$g_define->{cmdhead}include$g_define->{cmdfoot}\s+"(.+)"/i)
		{
			my @stock=($NOW_FILEHANDLE,$NOW_FILENAME,$linecount);
			AnalyzeItemData($filehandle,$1);
			($NOW_FILEHANDLE,$NOW_FILENAME,$linecount)=@stock;
			next;
		}
		
		GetBuffer($analyzemode,$line);
	}
	OutBuffer($analyzeoldmode);
	$analyzeoldmode=-1;
	$analyzemode='';
	close($filehandle);
	delete $analyzefile{$filename};
}

sub GetDefineList
{
	my($idx,$sep,$baseidx)=@_;
	my $ret="";
	$sep||=" ";
	
	my @list=grep(/^$idx\d+$/,sort(keys(%{$g_define})));
	my @list2=();
	foreach (@list)
	{
		$_=~/^$idx(\d+)$/;
		$list2[$1]=$g_define->{$_};
		if($quote){$list2[$1]="'$list2[$1]'";}
	}
	push(@errormsg,"\@DEFINE $idx のリスト数が合いません") if grep($_ ne '',@list2)!=$#list2-$baseidx+1;
	$ret=join($sep,@list2);
	return $ret;
}

sub OutItemData
{
	open(OUT,">$ITEM_DIR/item$FILE_EXT");
	
	push(@dispmsg,("ディレクトリ名","\t".$g_define->{dirname}));
	
	push(@dispmsg,("バージョン","\t".$g_define->{version}));
	print OUT "\$ITEM_VERSION='$g_define->{version}';\n";
	
	push(@dispmsg,"陳列棚維持費");
	my $ary=GetDefineList("costshowcase"," ",1);
	push(@dispmsg,"\t".$ary);
	print OUT "\@SHOWCASE_COST=qw($ary);\n";
	
	push(@dispmsg,"最大資金");
	push(@dispmsg,"\t".$g_define->{maxmoney});
	print OUT "\$MAX_MONEY=$g_define->{maxmoney};\n";
	
	push(@dispmsg,"作業所要時間");
	push(@dispmsg,"\tEDIT SHOWCASE\t".$g_define->{timeeditshowcase});
	#push(@dispmsg,"\tSHOPPING     \t".$g_define->{timeshopping}."★このパラメータは廃止しました") if $g_define->{timeshopping};
	push(@dispmsg,"\tSEND ITEM    \t".$g_define->{timesenditem});
	push(@dispmsg,"\tSEND MONEY   \t".$g_define->{timesendmoney});
	#push(@dispmsg,"\tSEND ITEM PLUS   \t".$g_define->{timesenditemplus});
	push(@dispmsg,"\tSEND MONEY PLUS  \t".$g_define->{timesendmoneyplus});
	print OUT "\$TIME_EDIT_SHOWCASE=$g_define->{timeeditshowcase};\n";
	#print OUT "\$TIME_SHOPPING=$g_define->{timeshopping};\n";
	print OUT "\$TIME_SEND_ITEM=$g_define->{timesenditem};\n";
	print OUT "\$TIME_SEND_MONEY=$g_define->{timesendmoney};\n";
	#print OUT "\$TIME_SEND_ITEM_PLUS=$g_define->{timesenditemplus};\n";
	print OUT "\$TIME_SEND_MONEY_PLUS=$g_define->{timesendmoneyplus};\n";
	
	push(@dispmsg,"アイテム使用時間倍率 ".$g_define->{itemusetimerate}) if $g_define->{itemusetimerate}!=1;
	
	push(@dispmsg,"アイテム分類");
	$ary=GetDefineList("type");
	push(@dispmsg,"\t".$ary);
	print OUT "\@ITEMTYPE=qw($ary );\n";
	
	push(@dispmsg,"職業リスト");
	$ary=join(" ",map{/^job-([a-z]+)$/;($1,$g_define->{$_})}grep(/^job-[a-z]+$/,keys %$g_define));
	print OUT "%JOBTYPE=qw($ary );\n";
	push(@dispmsg,"\t".$ary);
	
	push(@dispmsg,"定義関数");
	foreach my $key (keys(%{$g_define->{function}}))
	{
		push(@dispmsg,"\t".$key);
		$key=~tr/a-z/A-Z/;
		print OUT "\$DEFINE_$key=1;\n";
	}
	print OUT "\$EXISTS_DEFINE_DATA=1;\n";
	
	my $sort=0;
	
	print OUT <<'CODE';
tie @ITEM,"AutoVarItem",[
{name=>'なし',price=>0,point=>0},
CODE
	my $prevno=0;
	foreach(0..$#out_item){$out_item[$_]->{sort}=$_;};
	foreach my $item (sort {$a->{no}<=>$b->{no}} @out_item)
	{
		push(@errormsg,"コード無\tITEM\t$item->{no}\t$item->{name}"),next if !$item->{code};
		push(@errormsg,"重複登録\tITEM\t".$item->{code}),next if $g_define_item{$item->{code}}++;
		push(@errormsg,"重複登録\tITEM-NO\t".$item->{no}),next if $g_define_itemno{$item->{no}}++;
		
		my $itemname=$item->{name};
		$itemname=~s/\\$//;
		
		push(@dispmsg,"ITEM\t$item->{no}\t$itemname");
		
		$g_useitemno[$item->{no}]=1;
		
		my $existimage=0;
		$existimage=1 if -e "$IMAGE_DIR/item-code-$item->{code}$IMAGE_EXT";
		$existimage=2 if -e "$IMAGE_DIR/item-no-$item->{no}$IMAGE_EXT";
		
		print OUT "{},\n" x ($item->{no}-$prevno-1);
		$prevno=$item->{no};
		
		my $s=join("\t",
		  (	
		  	$item->{no},
			$item->{sort},
			$item->{type},
			$item->{price},
			$item->{cost},
			$item->{pricebase},
			$item->{pricehalf},
			$item->{limit},
			$item->{wslimit},
			$item->{popular},
			$item->{plus},
			$item->{code},
			$item->{scale},
			$item->{name},
			$item->{info},
			$item->{point},
			$item->{param},
			$existimage,
			$item->{func},
			$item->{functurn},
			$item->{funcsale},
			$item->{funcbuy},
			$item->{flag},
		  )
		);
		print OUT "'$s',\n";
		
		if($item->{localfuncturn})
		{
			push(@dispmsg,"\tfuncturn $item->{functurn}");
			open(OUTSUB,">$ITEM_DIR/item-t/$item->{no}$FILE_EXT");
			print OUTSUB "package item;\nsub $item->{functurn} {eval(<<'_eval_code_');\n";
			print OUTSUB GetFuncItemNo($item->{localfuncturn},"ITEM funct $item->{code}");
			print OUTSUB "\n"."_eval_code_\n}\n1;\n";
		}
		if($item->{localfuncsale})
		{
			push(@dispmsg,"\tfuncsale $item->{funcsale}");
			open(OUTSUB,">$ITEM_DIR/item-s/$item->{no}$FILE_EXT");
			print OUTSUB "package item;\nsub $item->{funcsale} {eval(<<'_eval_code_');\n";
			print OUTSUB GetFuncItemNo($item->{localfuncsale},"ITEM funcs $item->{code}");
			print OUTSUB "\n"."_eval_code_\n}\n1;\n";
		}
		if($item->{localfuncbuy})
		{
			push(@dispmsg,"\tfuncbuy $item->{funcbuy}");
			open(OUTSUB,">$ITEM_DIR/item-b/$item->{no}$FILE_EXT");
			print OUTSUB "package item;\nsub $item->{funcbuy} {eval(<<'_eval_code_');\n";
			print OUTSUB GetFuncItemNo($item->{localfuncbuy},"ITEM funcb $item->{code}");
			print OUTSUB "\n"."_eval_code_\n}\n1;\n";
		}
		
		if(defined($out_use{$item->{code}}))
		{
			if($item->{localfunc})
			{
				push(@dispmsg,"\tfunc $item->{func}");
				open(OUTSUB,">$ITEM_DIR/use-s/$item->{code}$FILE_EXT");
				print OUTSUB "sub $item->{func} {eval(<<'_eval_code_');\n";
				print OUTSUB GetFuncItemNo($item->{localfunc},"ITEM func $item->{code}");
				print OUTSUB "\n"."_eval_code_\n}\n1;\n";
			}
			
			open(MAKEOUT,">$ITEM_DIR/use/$item->{code}$FILE_EXT");
			my $s="";
			$s.="package item;\0";
			$s.='$main\'DEFINE_FUNCUSE_SUB=1;\0' if $item->{localfunc};
			foreach my $use (@{$out_use{$item->{code}}})
			{
				my $log="\tUSE\t$use->{no}\t$use->{name}\t$use->{time}";
				$log.="\tlocal func"        if $use->{localfunc};
				$log.="\tlocal func before" if $use->{localfuncbefore};
				$log.="\tlocal func info"   if $use->{localfuncinfo};
				push(@dispmsg,$log);
				
				$s.="
					\$USE[$use->{no}]=
					{
						'code'	=>'$use->{code}',
						'no'	=>$use->{no},
						'itemno'=>'$use->{itemno}',
						'name'	=>'$use->{name}',
						'info'	=>'$use->{info}',
						'scale'	=>'$use->{scale}',
						'action'=>'$use->{action}',
						'money'	=>${\($use->{money}+0)},
						'time'	=>${\($use->{time}+0)},
				";
				$s.="'exptime'=>'${\($use->{exptime}+0)}'," if $use->{exptime};
				$s.="'exp'=>'$use->{exp}',"                 if $use->{exp};
				$s.="'arg'=>'$use->{arg}',"                 if $use->{arg};
				$s.="'argmessage'=>'$use->{argmessage}',"   if $use->{argmessage};
				$s.="'argselect' =>'$use->{argselect}',"    if $use->{argselect};
				$s.="'param1'=>'$use->{param1}',"           if $use->{param1};
				$s.="'param2'=>'$use->{param2}',"           if $use->{param2};
				$s.="'param3'=>'$use->{param3}',"           if $use->{param3};
				$s.="'param4'=>'$use->{param4}',"           if $use->{param4};
				$s.="'needexp'=>'$use->{needexp}',"         if $use->{needexp};
				$s.="'needjob'=>'$use->{needjob}',"         if $use->{needjob};
				$s.="'needpoint'=>'$use->{needpoint}',"     if $use->{needpoint};
				$s.="'needevent'=>'$use->{needevent}',"     if $use->{needevent};
				$s.="'needpop'=>'$use->{needpop}',"         if $use->{needpop};
				
				if(defined($use->{use}[0]))
				{
					$s.="'use'=>[";
					foreach (@{$use->{use}})
					{
						my @val=split(/\t/,$_);
						$s.="{'no'=>".GetItemNumber($val[1]).",'count'=>$val[0],'proba'=>$val[2]";
						$s.=",'message'=>'$val[3]'" if $val[3]ne'';
						$s.="},";
					}
					$s.="],";
				}
				
				$s.="'functionbefore'=>'$use->{funcbefore}'," if $use->{funcbefore};
				$s.="'functioninfo'=>'$use->{funcinfo}'," if $use->{funcinfo};
				
				$s.="'result'=>{";
				$s.="'function'=>'$use->{func}'," if $use->{func};
	
				if($use->{okmsg}.$use->{ngmsg} ne '')
				{
					$s.="'message'=>{";
					$s.="'resultok'=>'$use->{okmsg}'," if $use->{okmsg};
					$s.="'resultng'=>'$use->{ngmsg}'," if $use->{ngmsg};
					$s.="},";
				}
	
				if(defined($use->{get}[0]))
				{
					$s.="'create'=>[";
					foreach (@{$use->{get}})
					{
						my @val=split(/\t/,$_);
						$s.="{'no'=>".GetItemNumber($val[1]).",'count'=>$val[0],'proba'=>$val[2]";
						$s.=",'message'=>'$val[3]'" if $val[3]ne'';
						$s.="},";
					}
					$s.="],";
				}
				
				$s.="},";
				$s.="};\0";
				$s.="sub $use->{func} {eval(<<'_eval_code_');\0".GetFuncItemNo($use->{localfunc},"USE func $use->{code}:no".($use->{no}+1))."\0"."_eval_code_\0}\0" if $use->{localfunc};
				$s.="sub $use->{funcbefore} {eval(<<'_eval_code_');\0".GetFuncItemNo($use->{localfuncbefore},"USE funcb $use->{code}:no".($use->{no}+1))."\0"."_eval_code_\0}\0" if $use->{localfuncbefore};
				$s.="sub $use->{funcinfo} {eval(<<'_eval_code_');\0".GetFuncItemNo($use->{localfuncinfo},"USE funci $use->{code}:no".($use->{no}+1))."\0"."_eval_code_\0}\0" if $use->{localfuncinfo};
				
				my @jobworklist=sort{$a->[0] cmp $b->[0]}map{[split /\t/]}@{$use->{job}};
				my $lastjob="";
				foreach my $job (@jobworklist)
				{
					my @val=@$job;
					my($key,$ope,$val)=($val[1]=~/^([^\+\-\*\/\=]+)([\+\-\*\/\=])(\S+)$/);
					$ope.="=" if $ope=~/[\+\-\*]/;
					$val=GetNumber($val);
					my $jobcode=GetJobCode($val[0]);
					push(@errormsg,"未定義職業 $val[0]"),next if !$jobcode;
					
					my @keys=();
					push(@keys,qw(time exptime)) if $key eq 'times';
					@keys=($key) if !@keys;
					
					if($lastjob ne $jobcode)
					{
						#$s.="\0_eval_code_\0}\0" if $lastjob ne '';
						$s.="\0"."_eval_code_\0}\0" if $lastjob ne '';
						#$s.="sub _job_use_$use->{no}_${jobcode}_ {eval(<<'_eval_code_');\0my \$use=\$USE[$use->{no}];";
						$s.="sub _job_use_$use->{no}_${jobcode}_ {eval(<<'_eval_code_');\0my(\$i)=\@_;\0my \$use=\$USE[\$i];";
						$lastjob=$jobcode;
					}
					foreach(@keys)
					{
						my $keyuse="\$use->{$_}";
						$s.=$ope ne '/' ? "$keyuse$ope$val;" : "$keyuse=int($keyuse/$val);";
					}
				}
				$s.="\0"."_eval_code_\0}\0" if $lastjob ne '';
			}
			$s=~s/[\t\n]//g;
			$s=~s/\0/\n/g;
			
			print MAKEOUT $s."\n1;\n";
			close(MAKEOUT);
		}
	}
	
	print OUT "];\n";
	
	print OUT '$AutoVarItem::itemcount='.scalar(@out_item).";\n";
	print OUT '$MAX_ITEM='.$prevno,";\n";
	
	print OUT <<'CODE';

package AutoVarItem;

sub TIEARRAY { bless $_[1],$_[0];}

sub FETCH
{
	my $hash=$_[0]->[$_[1]];
	return $hash if ref $hash eq 'HASH';
	
	$hash={};
	(
		$hash->{no},
		$hash->{sort},
		$hash->{type},
		$hash->{price},
		$hash->{cost},
		$hash->{pricebase},
		$hash->{pricehalf},
		$hash->{limit},
		$hash->{wslimit},
		$hash->{popular},
		$hash->{plus},
		$hash->{code},
		$hash->{scale},
		$hash->{name},
		$hash->{info},
		$hash->{point},
		$hash->{param},
		$hash->{existimage},
		$hash->{func},
		$hash->{functurn},
		$hash->{funcsale},
		$hash->{funcbuy},
		$hash->{flag},
	)=split(/\t/,$_[0]->[$_[1]]);
	$_[0]->[$_[1]]=$hash;
	
	return $hash if --$itemcount;
	
	my $array=$_[0];
	untie @main::ITEM;
	@main::ITEM=@$array if !tied @main::ITEM;
	return $hash;
}
CODE
	print OUT 'sub FETCHSIZE { return '.($prevno+1)." }\n1;\n";

	close(OUT);
}

sub OutEventData
{
	open(EOUT,">$ITEM_DIR/event$FILE_EXT");
	
	if(@out_event==())
	{
		print EOUT "1;";
		close(EOUT);
		return
	}
	print EOUT <<"CODE";
foreach(
CODE
	foreach my $event (@out_event)
	{
		push(@errormsg,"コード無\tEVENT\t$event->{info}"),next if !$event->{code};
		push(@errormsg,"重複登録\tEVENT\t".$event->{code}),next if $g_define_event{$event->{code}};
		$g_define_event{$event->{code}}=1;
		
		push(@dispmsg,"EVENT\t$event->{info}");
		
		($event->{nowfunc},$event->{nowfuncparam})=($1,$2) if $event->{nowfunc}=~/^(.*)\((.*)\)$/;
		($event->{startfunc},$event->{startfuncparam})=($1,$2) if $event->{startfunc}=~/^(.*)\((.*)\)$/;
		($event->{endfunc},$event->{endfuncparam})=($1,$2) if $event->{endfunc}=~/^(.*)\((.*)\)$/;
		
		my $s=join("\t",
		  (
			$event->{code},
			$event->{group},
			$event->{startproba},
			$event->{startfunc},
			$event->{startfuncparam},
			$event->{endfunc},
			$event->{endfuncparam},
			$event->{basetime},
			$event->{plustime},
			$event->{startmsg},
			$event->{endmsg},
			$event->{nowfunc},
			$event->{nowfuncparam},
		  )
		);
		print EOUT "'$s',\n" if $event->{startproba}!=-1;
		
		if($event->{localfuncstart})
		{
			push(@dispmsg,"\tstartfunc\t$event->{startfunc}");
			open(EOUTSUB,">$ITEM_DIR/event-s/$event->{code}$FILE_EXT");
			print EOUTSUB "package event;\n";
			print EOUTSUB "sub $event->{startfunc} {\n";
			print EOUTSUB GetFuncItemNo($event->{localfuncstart},"EVENT startfunc $event->{code}");
			print EOUTSUB "\n}\n1;\n";
			close(EOUTSUB);
		}
		
		if($event->{localfuncend})
		{
			push(@dispmsg,"\tendfunc\t$event->{endfunc}");
			open(EOUTSUB,">$ITEM_DIR/event-e/$event->{code}$FILE_EXT");
			print EOUTSUB "package event;\n";
			print EOUTSUB "sub $event->{endfunc} {\n";
			print EOUTSUB GetFuncItemNo($event->{localfuncend},"EVENT endfunc $event->{code}");
			print EOUTSUB "\n}\n1;\n";
			close(EOUTSUB);
		}
		
		if($event->{localfuncnow})
		{
			push(@dispmsg,"\tcustom func");
			open(EOUTSUB,">$ITEM_DIR/event-n/$event->{code}$FILE_EXT");
			print EOUTSUB "package event;\n";
			print EOUTSUB "sub $event->{nowfunc} {\n";
			print EOUTSUB GetFuncItemNo($event->{localfuncnow},"EVENT func $event->{code}");
			print EOUTSUB "\n}\n1;\n";
		}
		
		open(EOUTSUB,">$ITEM_DIR/event/$event->{code}$FILE_EXT");
		
		print EOUTSUB "push(\@EVENTMSG,'$event->{info}');\n" if $event->{info};
		
		foreach my $param (@{$event->{param}})
		{
			my @val=split(/\t/,$param);
			$val[1] =~ /^([^\+\-\*\/\=]+)([\+\-\*\/\=])(\S+)$/;
			my($key,$ope,$val)=($1,$2,$3);
			if($ope =~ /[\+\-\*]/){$ope.="=";}
			
			$key=~s/^(\\|money)$/price/i;
			$key=~s/^base$/pricebase/i;
			$key=~s/^harf$/pricehalf/i; # ver.2002-01-01-a までとの互換性確保
			$key=~s/^half$/pricehalf/i;
			$key=~s/^pop$/popular/i;
			
			my $keyitem="\$ITEM[".GetItemNumber($val[0])."]->{$key}";
			if($ope ne '/')
			{
				# / 以外の場合
				print EOUTSUB "$keyitem$ope$val;\n";
			}
			else
			{
				# / の場合は int で丸める
				print EOUTSUB "$keyitem=int($keyitem/$val);\n";
			}
		}
		
		print EOUTSUB "1;\n";
		close(EOUTSUB);
	}
	print EOUT <<'CODE';
)
{
	my $hash={};
	(
		$hash->{code},
		$hash->{group},
		$hash->{startproba},
		$hash->{startfunc},
		$hash->{startfuncparam},
		$hash->{endfunc},
		$hash->{endfuncparam},
		$hash->{basetime},
		$hash->{plustime},
		$hash->{startmsg},
		$hash->{endmsg},
		$hash->{func},
		$hash->{funcparam},
	)=split(/\t/);
	$EVENT{$hash->{code}}=$hash;
}
CODE
	print EOUT "1;\n";
	close(EOUT);
}

sub GetFuncItemNo
{
	my($val,$type)=@_;
	
	$val=GetFuncValue($val,$type); # まず@@VALUEを処理する(@@ITEMNO"@@VALUE"BaseItemName""等の為に)
	
	$val=~s/$g_define->{cmdhead}ITEMNO\s*"(.+?)"\s*$g_define->{cmdfoot}/GetItemNumber($1)/ige;
	eval("sub { $val } ");
	push(@errormsg,"$type $@") if $@;
	return $val;
}

sub GetFuncValue
{
	my($val,$type)=@_;
	$val=~s/$g_define->{cmdhead}VALUE\s*"(.+?)"\s*$g_define->{cmdfoot}/GetDefineString($1)/ige;
	#eval("sub { $val } ");
	#push(@errormsg,"$type $@") if $@;
	return $val;
}

sub OutFunctionData
{
	foreach my $key (keys(%{$g_define->{function}}))
	{
		my $val=$g_define->{function}->{$key};
		$val=GetFuncItemNo($val);
		eval("sub { $val } ");
		push(@errormsg,"$key error $@"),return if $@;
		
		my $packagename="";
		$packagename='event' if $key eq 'funcevent';
		$packagename='item' if $key eq 'funcitem';
		$packagename='item' if $key eq 'functurn';
		$packagename='item' if $key eq 'funcsale';
		$packagename='item' if $key eq 'funcbuy';
		
		open(OUT,">$ITEM_DIR/$key$FILE_EXT");
		print OUT "package $packagename;\n" if $packagename ne '';
		$val=~s/\s*sub\s+(\w+)\s*/\nsub $1 /g;
		print OUT $val."\n1;\n";
		close(OUT);
		
		#push(@dispmsg,$val);
		
		$key=~tr/a-z/A-Z/;
		push(@dispmsg,$key);
		push(@dispmsg,map{"\t".$_}($val=~/\s*sub\s+(\w+)\s*/g));
	}
}

sub OutResultMessage
{
	if($errormsg[0])
	{
		print "●ERROR●<br>";
		foreach(@errormsg)
		{
			print $_."<br>";
		}
		print "<hr>";
	}
	
	print "利用可能\アイテムNo.<br>";
	foreach(1..$#g_useitemno)
	{
		if(!$g_useitemno[$_])
		{
			print "[$_] ";
		}
	}
	print "[".($#g_useitemno+1)."～]";
	print "<hr>";
	if($dispmsg[0])
	{
		print "RESULT<br>";
		foreach(@dispmsg)
		{
			s/\t/　/g;
			print $_."<br>";
		}
		print "<hr>";
	}
}

sub GetLocalFunction
{
	my($funcname,$ext)=@_;
	#$funcname=GetString($funcname);
	my $funcbuf="";
	
	if($funcname=~/^$g_define->{localfuncmark}(\(.+\))?$/i)
	{
		my $linestart=$linecount;
		$funcname=$g_define->{localfuncmark}.$ext;
		$funcname.=$1 if $1;
		while(1)
		{
			my $line=GetLine($NOW_FILEHANDLE);
			last if $line eq '' || $line=~/^\s*$g_define->{localfuncmark}\s*$/;
			$line=~s/^\s+//g;
			$line=~s/\s+$//g;
			$funcbuf.=$line."\n";
		}
		#eval("sub{$funcbuf}");
		#push(@errormsg,"$NOW_FILENAME ($linestart-$linecount) $@") if $@;
	}
	return ($funcname,$funcbuf);
}

sub OutDefineData
{
	open OUT,">$ITEM_DIR/define$FILE_EXT";
	
	print OUT "\%DEFINE_DATA=(\n";
	while(my($key,$val)=each %$g_define)
	{
		next if ref $val;
		
		$key=~s/\\$/\\\\/;
		$val=~s/\\$/\\\\/;
		print OUT "'$key'=>'$val',\n";
	}
	print OUT ");\n1;\n";
	
	close OUT;
}

