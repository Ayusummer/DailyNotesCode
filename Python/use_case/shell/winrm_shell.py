import winrm

# 连接到一个远程主机
session = winrm.Session("192.168.1.219", auth=("ARTWinSummer\Win10Pro", "Win10Pro"))
# 执行一个命令
result = session.run_cmd("Get-Process")
# 打印输出
print(result.std_out.decode())
# 执行一个脚本
result = session.run_ps("Get-Date")
# 打印输出
print(result.std_out.decode())
