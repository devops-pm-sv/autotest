# encoding: utf-8
# @Time    : 2020/12/3 15:57
# @Author  : zhoubo
# @dsc     :
import logging
import time
import inspect
import functools
import traceback
import os
import sys
import colorlog

now_time = time.strftime('%Y%m%d%H%M%S')
LOGFILE = f"E:/PyProject/autotest/log/LogFile/{now_time}.log"



class LogSet(object):
    @staticmethod
    def _log(level, msg="") -> None:
        """
        日志配置
        :param log_idx: 日志等级
        :param msg: 日志信息
        :return:
        """
        logger = logging.getLogger()
        logger.setLevel('DEBUG')
        # file_path = sys._getframe(1).f_code.co_filename
        # BASIC_FORMAT = f"[%(asctime)s] [{file_path :<{30}}]：%(levelname)-6s %(message)s "
        BASIC_FORMAT = f"[%(asctime)s] %(levelname)-5s ：%(message)s "
        DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
        LOGFORMAT = f"%(log_color)s[%(asctime)s] %(log_color)s%(levelname)-5s ：%(log_color)s%(message)s"

        formatter = colorlog.ColoredFormatter(fmt=LOGFORMAT, log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white'},datefmt=DATE_FORMAT)
        file_format = logging.Formatter(BASIC_FORMAT, DATE_FORMAT)

        # 输出到控制台的handler
        out_console = logging.StreamHandler()
        out_console.setFormatter(formatter)
        out_console.setLevel('DEBUG')

        # 输出到文件的handler
        out_file = logging.FileHandler(LOGFILE, encoding="utf-8")
        out_file.setFormatter(file_format)
        out_file.setLevel('DEBUG')

        # 添加handler
        logger.addHandler(out_console)
        logger.addHandler(out_file)
        if level=="debug":
            logger.debug(msg)
        if level=="info":
            logger.info(msg)
        if level=="error":
            logger.error(msg)
        if level=="critical":
            logger.critical(msg)
        if level=="warning":
            logger.warning(msg)
        logger.removeHandler(out_console)
        logger.removeHandler(out_file)

    @staticmethod
    def error(msg):
        LogSet._log(level="error",msg=msg)

    @staticmethod
    def debug(msg):
        LogSet._log(level="debug",msg=msg)

    @staticmethod
    def info(msg):
        LogSet._log(level="info",msg=msg)

    @staticmethod
    def critical(msg):
        LogSet._log(level="critical",msg=msg)

    @staticmethod
    def warning(msg):
        LogSet._log(level="warning",msg=msg)

    @staticmethod
    def decorator_for_func(orig_func):
        """
                函数装饰器，获取函数执行日志
        :param orig_func: 待装饰函数
        """
        # if not str(orig_func.__name__).startswith("test"):
        #     return
        @functools.wraps(orig_func)
        def decorator(*args, **kwargs):
            # 获取形参
            parse = locals()
            LogSet.info(msg=f"""函数  [ {orig_func.__name__}{inspect.signature(orig_func)} | MODULE:{orig_func.__module__}]  Running...""")
            # 封装实参
            arg = parse["args"][1:] if len(parse["args"])>1 else ""
            karg = parse["kwargs"]
            value = {"args":arg,"kwargs":karg}

            if arg or karg:
                LogSet.debug(msg=f"{orig_func.__name__} 函数实参：{value}")
            try:
                result = orig_func(*args, **kwargs)
                LogSet.info(msg=f"函数  [ {orig_func.__name__}{inspect.signature(orig_func)} ]  Successful!")
                return result
            except Exception as e:
                LogSet.error(msg=f"函数  [ {orig_func.__name__}{inspect.signature(orig_func)} ]  Fail!")
                raise
        return decorator

    @staticmethod
    def get_log(cls):
        """
            装饰类下的方法
        :param cls:
        :return:
        """
        for name, method in inspect.getmembers(cls):
            if (not inspect.ismethod(method) and not inspect.isfunction(method)) or inspect.isbuiltin(method): # or not name.startswith("test")
                continue
            setattr(cls, name, LogSet.decorator_for_func(method))
        return cls

# @LogSet.get_log
# class Test0():
#     def est2(self):
#         print(9999)


if __name__ == '__main__':
    pass
    import os

    # curPath = os.path.abspath(os.path.dirname(__file__))
    # print(curPath)
    # rootPath = curPath[:curPath.find("autotest\\") + len("autotest\\")]  # 获取myProject，也就是项目的根路径
    # print(rootPath)
    # Test0().est2()














