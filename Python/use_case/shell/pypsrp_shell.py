from pypsrp.client import Client

# 连接到一个远程主机
client = Client("server", username="user", password="password")
# 执行一个命令
output, streams, had_errors = client.execute_cmd("Get-Process")
# 打印输出
print(output)
# 执行一个脚本
output, streams, had_errors = client.execute_ps("Get-Date")
# 打印输出
print(output)


