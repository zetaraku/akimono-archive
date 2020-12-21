# 旧版SOLD OUTからのデータ変換 2004/01/20 由來

GetQuery();

Lock();
DataReadOld();
CheckUserPass(1);
ConvertData();
ConvertPass() if !$Q{nopass};
OldLog("0");
OldLog("1");
OldLog("2");
DataWrite();
DataCommitOrAbort();
UnLock();
$disp.="正常に変換できました。";

OutSkin();
exit;

sub ConvertData
{
	$DTlasttime=$NOW_TIME;
	$DTTaxrate=0;
	$DTState="0:0:0:0:5001:0:5001:0:0:2000:0";
	undef %STATE;
	my @buf=split(/:/,$DTState); my $i=0;
	foreach (@STATEnamelist) { $STATE->{$_}=$buf[$i];$i++;}
	foreach my $DT (@DT)
	{
	$DT->{dignity}=0;
	$DT->{ticket}="";
	$DT->{taxmode}="";
	$DT->{guild}="";
	$DT->{lastlogin}=$NOW_TIME;
	$DT->{money}+=$DT->{trush};
	$DT->{trush}=0;
	$DT->{icon}=int(rand($ICON_NUMBER))+1;
	delete $DT->{user};
	}
}

sub ConvertPass
{
	foreach my $DT (@DT)
	{
	$DT->{pass}=crypt($DT->{pass},GetSalt());
	}
}

sub OldLog
{
	my($f)=@_;
	$disp.=$f;
	open(IN,GetPath("log-s$f")) or return;
	my @data=<IN>;
	close(IN);
	undef @MESSAGE;
	foreach my $i(0..$#data)
		{
		my($tm,$mode,$id,$to,$message,$no)=split(',',$data[$i]);
		$MESSAGE[$i]="$tm\t$mode\t$id\t$message\n";
		}
	OpenAndCheck(GetPath($TEMP_DIR,"log$f"));
	print OUT @MESSAGE;
	close(IN);
}

sub DataReadOld
{
	my $datafile=GetPath("data");
	OutError("実行できません") unless -e $datafile;
	open(IN,$datafile);
	read(IN,my $buf,-s $datafile);
	close(IN);
	my @DATA=split(/\n/,$buf);
	
	OutError("no data") if !@DATA;
	
	my $idx=0;
	my $maxdata=@DATA;
	
	$DTlasttime=$DATA[$idx++];
	($DTpeople,$DTnextid,$DTblockip,$DTTaxrate,$DTState)=split(/,/,$DATA[$idx++]);
	@DTwholestore=split(/,/,$DATA[$idx++],$MAX_ITEM);
	%DTevent=split(/,/,$DATA[$idx++]);
	undef %STATE;
	my @buf=split(/:/,$DTState); my $i=0;
	foreach (@STATEnamelist) { $STATE->{$_}=$buf[$i];$i++;}
	foreach(keys(%DTevent)){require(GetPath($ITEM_DIR,"event",$_));}
	
	tie($DTtown,"AutoVar",[\$DTtown,$DATA[$idx++],"HASH",","]) if $DATA[$idx] ne '//';
	
	while($DATA[$idx++] ne '//'){}
	
	undef @DT;
	undef %id2idx;
	undef %name2idx;
	undef %name2pass;
	
	my @list;
	my $cnt=0;
	my $id;
	my $name;
	
	while($idx<$maxdata)
	{
		my %DT;
		$DT[$cnt]=\%DT;
		
		@DT{@DTindexnamelist}=split(/,/,$DATA[$idx++]);
		$DT{point}=GetDTPoint(\%DT);
		$DT{status}=1;
		
		$id=$DT{id};
		$name=$DT{name};
		
		$id2idx{$id}=$name2idx{$name}=$cnt;
		$name2pass{$name}=$DT{pass};
		
		$DTnextid=$id+1 if $DTnextid<=$id;
		
		if($MAX_ITEM)
		{
			@list=split(/:/,$DATA[$idx],7);
			@DT{qw(showcase price)}=map{[split(/,/,$_)]}@list[0,1];
			tie $DT{item},"AutoVar",[\$DT{item},$list[2],"ARRAY",","];
			@DT{qw(itemyesterday itemtoday exp)}=map{{split(/,/,$_)}}@list[3,4,5];
			$list[6] ? tie($DT{user},"AutoVar",[\$DT{user},$list[6],"HASH",'[\t,]']) : ($DT{user}={});
		}
		$idx++;
		$cnt++;
	}
	$DTusercount=$cnt;
}
