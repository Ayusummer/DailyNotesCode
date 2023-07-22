<!-- 显示当前目录下的文件以及超链接 -->
<?php
// 获取当前目录下的文件
$files = scandir("./");
// 遍历文件
foreach ($files as $file) {
    // 判断是否为文件
    if (is_file($file)) {
        // 输出文件名
        echo $file . "<br>";
        // 输出超链接
        echo "<a href='./" . $file . "'>" . $file . "</a><br>";
    }
}
?>
