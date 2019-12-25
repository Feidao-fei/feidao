import colorlog
import logging


class CustomLogging:
    SYSINFO = 9
    SUCCESS = 8
    ERROR = 7
    WARNING = 6


logging.addLevelName(CustomLogging.SYSINFO, "*")
logging.addLevelName(CustomLogging.SUCCESS, "+")
logging.addLevelName(CustomLogging.ERROR, "-")
logging.addLevelName(CustomLogging.WARNING, "!")

fmt = "%(log_color)s[%(asctime)s] %(log_color)s [%(levelname)s] %(log_color)s%(message)s"
datefmt = '%H:%M:%S'
LOGGER = logging.getLogger("feidaoLog")

formatter = colorlog.ColoredFormatter(
    fmt=fmt,
    datefmt=datefmt,
    reset=True,
    log_colors={
        "*": "yellow",
        "+": "red",
        "-": "cyan",
        "!": "green"
    },
    style='%'

)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
LOGGER.addHandler(handler)
LOGGER.setLevel(CustomLogging.WARNING)


class MyLogger:
    @staticmethod
    def success(msg):
        return LOGGER.log(CustomLogging.SUCCESS, msg)

    @staticmethod
    def info(msg):
        return LOGGER.log(CustomLogging.SYSINFO, msg)

    @staticmethod
    def warning(msg):
        return LOGGER.log(CustomLogging.WARNING, msg)

    @staticmethod
    def error(msg):
        return LOGGER.log(CustomLogging.ERROR, msg)

if __name__ == '__main__':
    log = MyLogger()
    log.success('aaa')