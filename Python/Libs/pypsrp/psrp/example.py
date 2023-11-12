from pathlib import Path
import toml
from pypsrp.powershell import PowerShell, RunspacePool
from pypsrp.wsman import WSMan
from funcs import sync_rps, CustomFormatter, ColoredInfoLogger
import logging

CONFIG_PATH = Path(__file__).parent / "config.toml"
CONFIG = toml.load(CONFIG_PATH)
SERVER = CONFIG["SERVER"]
USERNAME = CONFIG["USERNAME"]
PASSWORD = CONFIG["PASSWORD"]

# 设置自定义的Logger
logging.setLoggerClass(ColoredInfoLogger)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# 创建控制台处理器并设置级别为DEBUG
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)

wsman = WSMan(
    server=SERVER,
    username=USERNAME,
    password=PASSWORD,
    ssl=False,
)
pool = RunspacePool(wsman)
pool.open()

# shell = PowerShell(pool)
# shell.add_script("$a=1")
# shell.add_script("$b=2")
# shell.add_script("$a+$b")
# output = shell.invoke()
# print(output)
# print(f"shell streams: {shell.streams}")

# shell2 = PowerShell(pool)
# shell2.add_script("$a+$b")
# output = shell2.invoke()
# print(output)

# shell3 = PowerShell(pool)
# shell3.add_script("$a+1")
# output = shell3.invoke()
# print(output)


# 基本用例测试
shell_test_basic = PowerShell(pool)
sync_rps(shell_test_basic, "whoami")
# 执行两例 Write-Host
shell_test_twice_write_host = PowerShell(pool)
sync_rps(shell_test_twice_write_host, "Write-Host Ayusummer;Write-Host 233;")
# 报错测试
shell_test_error = PowerShell(pool)
sync_rps(shell_test_error, "whoami1")


# 结束
pool.close()
wsman.close()
