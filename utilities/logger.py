import inspect
import logging
from logging.handlers import RotatingFileHandler
"""
->from logging.handlers import RotatingFileHandler:

Log Rotation (Optional): If your framework is running large test suites or generating logs frequently,
implement log rotation. This will keep log files manageable and avoid excessive disk usage.
"""
class LogMaker:
    @staticmethod
    def custom_logger(name=__name__, log_level=logging.INFO):
        logger_name = inspect.stack()[1][3]  # Gets the calling function name
        logger = logging.getLogger(logger_name)
        logger.setLevel(log_level)
        if not logger.handlers:
            file_handler = logging.FileHandler("D:\\PytestPython\\NopCommerceAutomation\\Logs\log.txt")
            formatter = logging.Formatter(
                "%(asctime)s:%(module)s:%(funcName)s:%(levelname)s:%(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        return logger
# class LogMaker:
#     @staticmethod
#     def custom_logger(name=__name__,log_level=logging.INFO):
#         logger_name = inspect.stack()[1][3]
#         logging.basicConfig(filename="D:\\PytestPython\\NopCommerceAutomation\\Logs\log.txt",
#                             format="%(asctime)s:%(module)s:%(classname)s:%(funcName)s:%(levelname)s:%(message)s",
#                             datefmt="%Y-%m-%d %H:%M:%S",force=True)
#
#         logger = logging.getLogger(logger_name)
#         logger.setLevel(log_level)
#         return logger

"""handler= RotatingFileHandler(filename="D:\\PytestPython\\NopCommerceAutomation\\Logs\log.txt",
                                     maxBytes=5000000, backupCount=100)"""



