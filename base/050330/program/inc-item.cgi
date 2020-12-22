# アイテム関数 2005/01/06 由來

package item; #変更不可

######################################################################
# ★アイテム用下請関数：ログ書きこみ
# usage: WriteLog(重要度,対象店舗ID,メッセージ)
#           重要度     0==一般 1==重要
#           対象店舗ID 0==全店舗宛 店舗ID==プライベート
#           メッセージ ログメッセージ
# return: 0 固定
######################################################################
sub WriteLog
{
	main::PushLog($_[0],$_[1],$_[2]);
	return 0;
}

######################################################################
# ★デバッグ用ログ書きこみ
# usage: DebugLog(メッセージ)
#           メッセージ ログメッセージ
# return: 0 固定
######################################################################
sub DebugLog
{
	my($msg)=@_;
	main::WriteErrorLog($msg,$main::LOG_DEBUG_FILE) if $main::DEBUG_LOG_ENABLE;
	return 0;
}

######################################################################
# ★アイテム用下請関数：アイテム消費
# usage: UseItem(アイテム番号,消費個数,メッセージ)
#           アイテム番号 1~
#           消費個数     1~
#           メッセージ   表示メッセージ
# return: 0 固定
######################################################################
sub UseItem
{
	my($itemno,$count,$msg)=@_;

	$count=UseItemSub($itemno,$count,$DT);
	push(@{$USE->{result}->{useitem}},[$itemno,$count]);
	push(@{$USE->{result}->{usemsg}},$msg);
	return 0;
}
sub UseItemSub
{
	my($itemno,$count,$DT)=@_;
	
	$count=$DT->{item}[$itemno-1] if $DT->{item}[$itemno-1]<$count;
	$DT->{item}[$itemno-1]-=$count;
	
	return $count;
}

######################################################################
# ★アイテム用下請関数：アイテム取得
# usage: AddItem(アイテム番号,取得個数,メッセージ)
#           アイテム番号 1~
#           取得個数     1~
#           メッセージ   表示メッセージ
# return: 0 固定
######################################################################
sub AddItem
{
	my($itemno,$count,$msg)=@_;

	$count=AddItemSub($itemno,$count,$DT);
	push(@{$USE->{result}->{additem}},[$itemno,$count]);
	push(@{$USE->{result}->{addmsg}},$msg);
	return 0;
}
sub AddItemSub
{
	my($itemno,$count,$DT)=@_;
	
	$count=$main::ITEM[$itemno]->{limit}-$DT->{item}[$itemno-1] if $main::ITEM[$itemno]->{limit}<$DT->{item}[$itemno-1]+$count;
	$DT->{item}[$itemno-1]+=$count;
	
	return $count;
}

sub GetUserData
{
	return &main::GetUserData;
}

sub GetMoneyString
{
	return &main::GetMoneyString;
}

require "$main::ITEM_DIR/funcitem.cgi" if $main::DEFINE_FUNCITEM;
1;
