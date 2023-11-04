import winrm

# 连接到一个远程主机
session = winrm.Session("server", auth=("user", "password"))
# 执行一个命令
result = session.run_cmd("Get-Process")
# 打印输出
print(result.std_out.decode())
# 执行一个脚本
result = session.run_ps("Get-Date")
# 打印输出
print(result.std_out.decode())
