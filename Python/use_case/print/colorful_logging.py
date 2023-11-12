import logging


# ANSI转义序列
class CustomFormatter(logging.Formatter):
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

# 测试不同级别的日志
logger.debug("这是一个调试信息")
logger.info("这是默认颜色的INFO消息")
logger.info("这是绿色的INFO消息", info_color="green")
logger.info("这是黄色的INFO消息", info_color="yellow")
logger.warning("这是一个警告消息")
logger.error("这是一个错误消息")
logger.critical("这是一个严重错误消息")
