from pypsrp.client import Client
from config import SERVER, USERNAME, PASSWORD

client = Client(server=SERVER, username=USERNAME, password=PASSWORD, ssl=False)

# stdout, stderr, rc = client.execute_cmd("whoami.exe /all")
stdout, stderr, rc = client.execute_cmd(
    "whoami.exe /all", encoding="GBK"  # encoding 默认是 437(en-US), 需要改成 GBK 才能正常显示中文
)

print("RC: %d" % rc)
print("STDOUT:\n%s" % stdout)
print("STDERR:\n%s" % stderr)
