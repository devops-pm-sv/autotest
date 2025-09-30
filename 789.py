
# encoding: utf-8
# @Time    : 2020/12/4 15:33
# @Author  : zhoubo
# @dsc     :
import os
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
import colorlog


root_dir = os.getcwd()



# print(root_dir)


import os
# curPath = os.path.abspath(os.path.dirname(__file__))
# print(curPath)
# rootPath = curPath[:curPath.find("autotest\\")+len("autotest\\")]  # 获取myProject，也就是项目的根路径
# print(rootPath)
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
# formatter = colorlog.ColoredFormatter(
#     fmt='[%(asctime)s] ：%(levelname)-6s %(message)s ',
#     datefmt=DATE_FORMAT,
#     reset=True,
#     log_colors={
#         'DEBUG': 'cyan',
#         'INFO': 'green',
#         'WARNING': 'yellow',
#         'ERROR': 'red',
#         'CRITICAL': 'red,bg_white',
#     }
# )

# import logging
# import colorlog
# LOG_LEVEL = logging.DEBUG
# LOGFORMAT ="  %(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s"
# logging.root.setLevel(LOG_LEVEL)
# formatter = colorlog.ColoredFormatter(LOGFORMAT)
# stream = logging.StreamHandler()
# stream.setLevel(LOG_LEVEL)
# stream.setFormatter(formatter)
# log = logging.getLogger('pythonConfig')
# log.setLevel(LOG_LEVEL)
# log.addHandler(stream)
#
# log.debug("A quirky message only developers care about")
# log.info("Curious users might want to know this")
# log.warning("Something is wrong and any user should be informed")
# log.error("Serious stuff, this is red for a reason")
# log.critical("OH NO everything is on fire")



# logger = logging.getLogger()
# logger.setLevel('DEBUG')
# DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
# formatter = colorlog.ColoredFormatter(
#     fmt='[%(asctime)s] ：%(levelname)-6s %(message)s ',
#     datefmt=DATE_FORMAT,
#     reset=True,
#     log_colors={
#         'DEBUG': 'cyan',
#         'INFO': 'green',
#         'WARNING': 'yellow',
#         'ERROR': 'red',
#         'CRITICAL': 'red,bg_white'})
# out_console = logging.StreamHandler()
# out_console.setFormatter(formatter)
# out_console.setLevel('DEBUG')
# logger.addHandler(out_console)
# logger.info("5645")





def runoob(func):    # 两个局部变量：arg、z
    z = 1
    def inner(*arg,**kwargs):
        func(*arg,**kwargs)
        return locals()
    return inner



@runoob
def a(v,b):
    print(v,b)


s = a(1,5)

print(a)







