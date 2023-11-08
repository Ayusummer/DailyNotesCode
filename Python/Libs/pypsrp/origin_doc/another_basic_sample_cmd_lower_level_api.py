from pypsrp.shell import Process, SignalCode, WinRS
from pypsrp.wsman import WSMan
from config import SERVER, USERNAME, PASSWORD


wsman = WSMan(
    server=SERVER,
    username=USERNAME,
    password=PASSWORD,
    ssl=False,
)

with WinRS(wsman) as shell:
    process = Process(shell, "whoami.exe", ["/all"])
    process.invoke()
    process.signal(SignalCode.CTRL_C)

print("RC: %d" % process.rc)

# the stdout and stderr streams come back as bytes, this decodes them with GBK(用于中文)
print("STDOUT:\n%s" % process.stdout.decode("GBK"))
print("STDERR:\n%s" % process.stderr.decode("GBK"))
