# 将 basic_sample.py 转换为使用低级API的写法示例:
from pypsrp.powershell import PowerShell, RunspacePool
from pypsrp.wsman import WSMan

SERVER = "192.168.1.219"
USERNAME = "ARTWinSummer\Win10Pro"
PASSWORD = "Win10Pro"
wsman = WSMan(SERVER, username=USERNAME, password=PASSWORD, ssl=False)

with RunspacePool(wsman) as pool:
    ps = PowerShell(pool)
    ps.add_script("New-Item -Path C:\\temp\\folder -ItemType Directory -Verbose")
    output = ps.invoke()

print("HAD ERRORS: %s" % ps.had_errors)
print("OUTPUT:\n%s" % "\n".join([str(s) for s in output]))
print("ERROR:\n%s" % "\n".join([str(s) for s in ps.streams.error]))
print("DEBUG:\n%s" % "\n".join([str(s) for s in ps.streams.debug]))
print("VERBOSE:\n%s" % "\n".join([str(s) for s in ps.streams.verbose]))
