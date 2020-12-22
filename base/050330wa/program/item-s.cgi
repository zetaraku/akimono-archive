# アイテム使用処理 2005/01/06 由來

$NOMENU=1;
$Q{er}='stock';
Lock();
DataRead();
CheckUserPass();

$Q{cnt}=int($Q{cnt2} ? $Q{cnt2} : $Q{cnt1});
$Q{cnt}=0 if $Q{cnt}<=0;
$itemno=$Q{item};
$no=$Q{no};
$target=$Q{tg};
$message=$Q{msg};
$select=$Q{select};
CheckItemNo($itemno);
OutError('標的が見つかりません') if $target && !defined($id2idx{$target});

$itemcode=GetPath($ITEM_DIR,"use",$ITEM[$itemno]->{code});
OutError('使えません') if $itemcode eq '' || !(-e $itemcode);

$ITEM=$ITEM[$itemno];
@item::DT=@DT;
$item::DT=$DT;
@item::ITEM=@ITEM;
$item::ITEM=$ITEM;
RequireFile('inc-item.cgi');
require $itemcode;

$USE=GetUseItem($no);
OutError('使えません') if !$USE || !$USE->{useok};
$item::USE=$USE;

	if($USE->{arg}=~/message(\d*)/)
	{
		my $limit=$1||80;
		require $JCODE_FILE;
		$message=EscapeHTML(jcode::sjis($message,$CHAR_SHIFT_JIS&&'sjis'));
		OutError('入力文字数が多すぎます (<>&"は4～6文字に換算されます)') if length $message>$limit;
	}
	my %select_hash;
	if($USE->{arg}=~/select/)
	{
		my @fld=split(/;/,$USE->{argselect});
		shift(@fld) if @fld%2==1;
		%select_hash=@fld;
		while(@fld)
		{
			last if shift @fld eq $select;
			shift @fld;
		}
		OutError('選択肢が不正です') if !@fld;
	}
	$USE->{arg}={};
	$USE->{arg}->{target}=$target;
	$USE->{arg}->{targetidx}=$id2idx{$target};
	$USE->{arg}->{count}=$Q{cnt};
	$USE->{arg}->{message}=$message;
	$USE->{arg}->{select}=$select;
	$USE->{arg}->{select_hash}=\%select_hash;
	UseItem($USE,$Q{cnt});

RequireFile('inc-html-ownerinfo.cgi');

my $count=$USE->{result}->{count};

$disp.="<BIG>●結果</BIG><br><br>";

if(!$count)
{
	$disp.="実行できませんでした";
}
else
{

	$disp.=$USE->{result}->{function_return}."<BR>" if $USE->{result}->{function_return};
	$disp.=$USE->{result}->{count}.$USE->{scale}."<BR>";
	$disp.="費用:".GetMoneyString($USE->{money}*$USE->{result}->{count})."<BR>" if $USE->{money}*$USE->{result}->{count};
	$disp.="時間:".GetTime2HMS(GetItemUseTime($USE)*$count)."<BR><BR>";
	
	foreach my $MESSAGE (@{$USE->{result}->{addmsg}})
		{$disp.=$MESSAGE."<BR>" if $MESSAGE;}
	
	if($USE->{result}->{additem}[0])
	{
		my $result=$USE->{result}->{message}->{resultok};
		$disp.=$result."<BR>" if $result;
		
		foreach my $MESSAGE (@{$USE->{result}->{trashmsg}})
			{$disp.=$MESSAGE."<BR>" if $MESSAGE;}
		
		$disp.="入手:";
		foreach my $ADDITEM (@{$USE->{result}->{additem}})
		{
			my $no=$ADDITEM->[0];
			$disp.=$ITEM[$no]->{name};
			$disp.=" +".$ADDITEM->[1]." (残".$DT->{item}[$no-1].") ";
		}
		$disp.="<BR>";
	}
	else
	{
		my $result=$USE->{result}->{message}->{resultng};
		$disp.=$result."<BR>" if $result;
	}
	
	foreach my $MESSAGE (@{$USE->{result}->{usemsg}})
	{
		$disp.=$MESSAGE."<BR>" if $MESSAGE;
	}
	
	if($USE->{result}->{useitem}[0])
	{
		$disp.="消費:";
		foreach my $USEITEM (@{$USE->{result}->{useitem}})
		{
			my $no=$USEITEM->[0];
			$disp.=$ITEM[$no]->{name};
			$disp.=" -".$USEITEM->[1]." (残".$DT->{item}[$no-1].") ";
		}
		$disp.="<BR>";
	}
}
	RenewLog();
	DataWrite();
	DataCommitOrAbort();
	UnLock();

OutSkin();
1;
