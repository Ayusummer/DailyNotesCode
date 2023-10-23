# 替换为您要计算 MD5 的文件路径
$filePath = "E:\DownloadFile\xiaomi.eu_multi_RUBENS_V14.0.4.0.TLNCNXM_v14-13-fastboot.zip" 

# 使用 Get-FileHash 计算 MD5 哈希
$md5Hash = Get-FileHash -Path $filePath -Algorithm MD5

# 输出 MD5 哈希值
$md5Hash.Hash
