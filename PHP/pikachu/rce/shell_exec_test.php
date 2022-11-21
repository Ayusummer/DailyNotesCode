<?php
//header("Content-type:text/html; charset=gbk");
$result='';

if(isset($_POST['submit']) && $_POST['ipaddress']!=null){
    $ip=$_POST['ipaddress'];
//     $check=explode('.', $ip);可以先拆分，然后校验数字以范围，第一位和第四位1-255，中间两位0-255
    if(stristr(php_uname('s'), 'windows')){
//         var_dump(php_uname('s'));
        $result.=shell_exec('ping '.$ip);//直接将变量拼接进来，没做处理
    }else {
        $result.=shell_exec('ping -c 4 '.$ip);
    }

}
?>

<div id="comm_main">
    <p class="comm_title">Here, please enter the target IP address!</p>
    <form method="post">
        <input class="ipadd" type="text" name="ipaddress" />
        <input class="sub" type="submit" name="submit" value="ping" />
    </form>

    <?php
    if($result){
        echo "<pre>{$result}</pre>";
    }
    ?>
</div>