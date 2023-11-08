from pypsrp.shell import Process, SignalCode, WinRS
from pypsrp.wsman import WSMan

wsman = WSMan("192.168.1.219", username="user", password="password", ssl=False)

with WinRS(wsman) as shell:
    process = Process(shell, "whoami.exe", ["/all"])
    process.invoke()
    process.signal(SignalCode.CTRL_C)

print("RC: %d" % process.rc)

# the stdout and stderr streams come back as bytes, this decodes them with the 437 codepage (default on my Windows host)
print("STDOUT:\n%s" % process.stdout.decode("437"))
print("STDERR:\n%s" % process.stderr.decode("437"))
