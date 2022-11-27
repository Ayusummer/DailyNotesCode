<?php
$html='';
if(isset($_POST['submit']) && $_POST['txt'] != null){
    if(@!eval($_POST['txt'])){
        $html.="<p>你喜欢的字符还挺奇怪的!</p>";

    }

}

?>

<div id="comm_main">
    <p class="comm_title">Here, 请提交一个你喜欢的字符串:</p>
    <form method="post">
        <input class="ipadd" type="text" name="txt" />
        <input class="sub" type="submit" name="submit" value="提交" />
    </form>
</div>


<?php
    echo $html;
    //    显示 /etc/passwd
    echo file_get_contents('test');
    ?>
