# 通过如下例子详细解释下 pypsrp 在执行以下脚本时会做什么:
from pypsrp.powershell import PowerShell, RunspacePool
from pypsrp.wsman import WSMan
from config import SERVER, USERNAME, PASSWORD


wsman = WSMan(
    server=SERVER,
    username=USERNAME,
    password=PASSWORD,
    cert_validation=False,
    ssl=False,  # 不将 ssl 设置为 False 会报错: Max retries exceeded with url: /wsman (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x000001A367C8C4F0>: Failed to establish a new connection: [WinError 10061] 由于目标计算机积极拒绝，无法连接。'))
)

with RunspacePool(wsman) as pool:
    ps = PowerShell(pool)
    ps.add_cmdlet("Get-PSDrive").add_parameter("Name", "C")
    ps.invoke()
    # we will print the first object returned back to us
    print(ps.output[0])
