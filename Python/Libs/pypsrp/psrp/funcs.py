from pypsrp.powershell import PowerShell, RunspacePool
import logging


# ANSI转义序列
class CustomFormatter(logging.Formatter):
    # 一些常用的颜色转义序列, 可在如下连接中查看: https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
    red = "\x1b[31m"
    bold_red = "\x1b[31;1m"
    green = "\x1b[32m"
    yellow = "\x1b[33m"
    blue = "\x1b[34m"
    magenta = "\x1b[35m"
    cyan = "\x1b[36m"
    white = "\x1b[37m"
    gray = "\x1b[90m"
    bright_red = "\x1b[91m"
    bright_green = "\x1b[92m"
    bright_yellow = "\x1b[93m"
    bright_blue = "\x1b[94m"
    bright_magenta = "\x1b[95m"
    bright_cyan = "\x1b[96m"
    bright_white = "\x1b[97m"
    reset = "\x1b[0m"
    format_str = "%(levelname)s: %(message)s (%(filename)s:%(lineno)d)"

    INFO_COLORS = {
        "default": blue,
        "green": green,
        "yellow": yellow,
        "blue": blue,
    }

    FORMATS = {
        logging.DEBUG: gray,
        logging.INFO: INFO_COLORS,  # 使用字典来处理不同的INFO颜色
        logging.WARNING: yellow,
        logging.ERROR: red,
        logging.CRITICAL: bold_red,
    }

    def format(self, record):
        color = self.FORMATS.get(record.levelno, self.gray)
        if isinstance(color, dict):
            # INFO级别的特殊处理
            info_color = getattr(record, "info_color", "default")
            color = color.get(info_color, self.gray)
        log_fmt = color + self.format_str + self.reset
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


# 自定义Logger类
class ColoredInfoLogger(logging.Logger):
    def info(self, msg, info_color="default", *args, **kwargs):
        # 添加info_color属性
        super().info(msg, extra={"info_color": info_color}, *args, **kwargs)


# 设置自定义的Logger
logging.setLoggerClass(ColoredInfoLogger)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# 创建控制台处理器并设置级别为DEBUG
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)


def sync_rps(runspace_pool: RunspacePool, script: str):
    """同步执行 Powershell script"""
    runspace = PowerShell(runspace_pool)
    runspace.add_script(script)
    logger.info(f"执行脚本：{script}")
    output = runspace.invoke()
    if runspace.had_errors:
        logger.error(f"执行脚本 {script} 时出错")
        if runspace.streams.error.__len__() > 0:
            for error in runspace.streams.error:
                logger.error(error.exception)
    else:
        if output:
            logger.info(f"OUTPUT: {output}")
        # 例如 Write-Host 的输出就会存在 information stream 中:
        if runspace.streams.information.__len__() > 0:
            for info in runspace.streams.information:
                logger.info(f"INFORMATION: {info.message_data}")
