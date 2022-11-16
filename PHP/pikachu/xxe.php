<?php
//查看当前LIBXML的版本
//print_r(LIBXML_VERSION);

$html='';
//考虑到目前很多版本里面libxml的版本都>=2.9.0了,所以这里添加 了LIBXML_NOENT 参数开启了外部实体解析
if(isset($_POST['submit']) and $_POST['xml'] != null){


    $xml =$_POST['xml'];
//    $xml = $test;
    $data = @simplexml_load_string($xml,'SimpleXMLElement',LIBXML_NOENT);
    if($data){
        $html.="<pre>{$data}</pre>";
    }else{
        $html.="接收到的数据 $data, 类型为 ".gettype($data);
        $html.="<p>XML声明、DTD文档类型定义、文档元素这些都搞懂了吗?</p>";
    }
}

?>

<form method="post">
    <p>这是一个接收xml数据的api:</p>
    <label>
        <input type="text" name="xml" />
    </label>
    <input type="submit" name="submit" value="提交">
</form>

<?php echo $html;?>