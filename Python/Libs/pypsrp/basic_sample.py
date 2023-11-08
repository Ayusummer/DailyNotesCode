# 通过 PSRP 层运行一些代码的示例
from pypsrp.client import Client

SERVER = "192.168.1.219"
USERNAME = "ARTWinSummer\Win10Pro"
PASSWORD = "Win10Pro"
client = Client(SERVER, username=USERNAME, password=PASSWORD, ssl=False)

script = r"New-Item -Path C:\temp\folder -ItemType Directory -Verbose"
output, streams, had_errors = client.execute_ps(script)

print("HAD ERRORS: %s" % had_errors)
print("OUTPUT:\n%s" % output)
print("ERROR:\n%s" % "\n".join([str(s) for s in streams.error]))
print("DEBUG:\n%s" % "\n".join([str(s) for s in streams.debug]))
print("VERBOSE:\n%s" % "\n".join([str(s) for s in streams.verbose]))
