from pathlib import Path
import toml
from pypsrp.powershell import PowerShell, RunspacePool
from pypsrp.wsman import WSMan

CONFIG_PATH = Path(__file__).parent / "config.toml"
CONFIG = toml.load(CONFIG_PATH)
SERVER = CONFIG["SERVER"]
USERNAME = CONFIG["USERNAME"]
PASSWORD = CONFIG["PASSWORD"]

wsman = WSMan(
    server=SERVER,
    username=USERNAME,
    password=PASSWORD,
    ssl=False,
)
pool = RunspacePool(wsman)
pool.open()
shell = PowerShell(pool)
shell.add_script("$a=1")
shell.add_script("$b=2")
shell.add_script("$a+$b")
output = shell.invoke()
print(output)
print(f"shell streams: {shell.streams}")

shell2 = PowerShell(pool)
shell2.add_script("$a+$b")
output = shell2.invoke()
print(output)

shell3 = PowerShell(pool)
shell3.add_script("$a+1")
output = shell3.invoke()
print(output)

# 结束
pool.close()
