# ANSI转义序列示例
RED = "\033[31m"  # 红色文本
GREEN = "\033[32m"  # 绿色文本
YELLOW = "\033[33m"  # 黄色文本
BLUE = "\033[34m"  # 蓝色文本
PINK = "\033[35m"  # 粉红色文本
RESET = "\033[0m"  # 重置颜色

# 导入 windows-index  yaml 文档
print(YELLOW + "正在导入 windows-index.yaml 文档, 文档比较大，可能需要一些时间......" + RESET)
print(GREEN + "windows-index.yaml 文档导入完成" + RESET)

##########
import logging


# ANSI转义序列
class CustomFormatter(logging.Formatter):
    grey = "\x1b[38;21m"
    blue = "\x1b[34;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    green = "\x1b[32;21m"  # 新增绿色
    reset = "\x1b[0m"
    format_s = "%(levelname)s: %(message)s (%(filename)s:%(lineno)d)"  # 更改变量名

    COLORS = {
        "INFO": {"default": blue, "green": green, "yellow": yellow},
        "WARNING": yellow,
        "ERROR": red,
        "CRITICAL": bold_red,
        "DEBUG": grey,
    }

    def format(self, record):
        color = self.COLORS.get(record.levelno, self.grey)  # 默认颜色为灰色
        if isinstance(color, dict):
            color = color.get(getattr(record, "color", "default"), self.grey)
        log_fmt = color + self.format_s + self.reset
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


# 设置日志格式
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)

# 测试不同级别的日志
logger.debug("这是一个调试信息")
logger.info("这是一个信息提示")  # 默认蓝色
logger.info("这是一个绿色的信息提示", extra={"color": "green"})
logger.info("这是一个黄色的信息提示", extra={"color": "yellow"})
logger.warning("这是一个警告消息")
logger.error("这是一个错误消息")
logger.critical("这是一个严重错误消息")
