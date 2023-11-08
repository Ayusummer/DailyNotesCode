from pypsrp.client import Client

client = Client(
    "192.168.1.219", username="ARTWinSummer\Win10Pro", password="Win10Pro", ssl=False
)

# stdout, stderr, rc = client.execute_cmd("whoami.exe /all")
stdout, stderr, rc = client.execute_cmd(
    "whoami.exe /all", encoding="GBK"  # encoding 默认是 437(en-US), 需要改成 GBK 才能正常显示中文
)

print("RC: %d" % rc)
print("STDOUT:\n%s" % stdout)
print("STDERR:\n%s" % stderr)
