# 多种颜色的 INFO 支持
import logging


class ColoredInfoLogger(logging.Logger):
    INFO_COLORS = {
        "default": "\x1b[34;21m",  # 蓝色
        "green": "\x1b[32;21m",  # 绿色
        "yellow": "\x1b[33;21m",  # 黄色
    }
    RESET = "\x1b[0m"

    def info(self, msg, color="default", *args, **kwargs):
        if color in self.INFO_COLORS:
            msg = f"{self.INFO_COLORS[color]}{msg}{self.RESET}"
        super().info(msg, *args, **kwargs)


# 设置自定义的Logger
logging.setLoggerClass(ColoredInfoLogger)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# 创建控制台处理器并设置级别为DEBUG
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 设置格式化器
formatter = logging.Formatter("%(levelname)s: %(message)s")
ch.setFormatter(formatter)

# 将处理器添加到logger
logger.addHandler(ch)

# 测试不同颜色的INFO消息
logger.info("这是默认颜色的INFO消息")
logger.info("这是绿色的INFO消息", color="green")
logger.info("这是黄色的INFO消息", color="yellow")
logger.debug("这是DEBUG消息")
logger.warning("这是WARNING消息")
logger.error("这是ERROR消息")
logger.critical("这是CRITICAL消息")
