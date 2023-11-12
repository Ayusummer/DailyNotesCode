from pathlib import Path
import toml
from pypsrp.powershell import PowerShell, RunspacePool
from pypsrp.wsman import WSMan
from funcs import sync_rps, logger

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

# 测试不同级别的日志
logger.debug("这是一个调试信息")
logger.info("这是默认颜色的INFO消息")
logger.info("这是绿色的INFO消息", info_color="green")
logger.info("这是黄色的INFO消息", info_color="yellow")
logger.warning("这是一个警告消息")
logger.error("这是一个错误消息")
logger.critical("这是一个严重错误消息")


# 基本用例测试
sync_rps(pool, "whoami")
# 执行两例 Write-Host
sync_rps(pool, "Write-Host Ayusummer;Write-Host 233;")
# 报错测试
sync_rps(pool, "whoami1")


# 结束
pool.close()
wsman.close()
