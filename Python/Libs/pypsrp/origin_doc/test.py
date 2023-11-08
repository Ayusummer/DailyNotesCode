# 通过 PSRP 层运行一些代码的示例
from pypsrp.client import Client
from config import SERVER, USERNAME, PASSWORD

client = Client(
    server=SERVER,
    username=USERNAME,
    password=PASSWORD,
    ssl=False,
)

output, streams, had_errors = client.execute_ps(r"cd C:/")

print("HAD ERRORS: %s" % had_errors)
print("OUTPUT:\n%s" % output)
print("ERROR:\n%s" % "\n".join([str(s) for s in streams.error]))
print("DEBUG:\n%s" % "\n".join([str(s) for s in streams.debug]))
print("VERBOSE:\n%s" % "\n".join([str(s) for s in streams.verbose]))

output, streams, had_errors = client.execute_ps(r"dir")
print("HAD ERRORS: %s" % had_errors)
print("OUTPUT:\n%s" % output)
print("ERROR:\n%s" % "\n".join([str(s) for s in streams.error]))
print("DEBUG:\n%s" % "\n".join([str(s) for s in streams.debug]))
print("VERBOSE:\n%s" % "\n".join([str(s) for s in streams.verbose]))
