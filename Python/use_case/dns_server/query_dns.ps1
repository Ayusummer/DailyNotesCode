$domain = "www.huawei.com"
$dns = "8.8.8.8"
Resolve-DnsName -Name $domain -Server $dns

# 
Resolve-DnsName -Name example.com -Server 8.8.8.8
Resolve-DnsName -Name yahoo.com -Server 127.0.0.1

# 参考材料记录: https://github.com/rthalley/dnspython/tree/master