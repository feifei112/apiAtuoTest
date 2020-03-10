# 自媒体域名地址
import logging.handlers
import time
# import os



MP_BASE_URL = "http://ttapi.research.itcast.cn"
# 自媒体请求头
MP_HEADER = {"Content-Type": "application/json"}

# 后台系统域名地址
MIS_BASE_URL = "http://ttapi.research.itcast.cn"
# 后台系统请求头
MIS_HEADER = {"Content-Type": "application/json"}

# 后台系统域名地址
APP_BASE_URL = "http://ttapi.research.itcast.cn"
# 后台系统请求头
APP_HEADER = {"Content-Type": "application/json"}




# 日志配置
def basic_loger():
    # 创建日志器
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # 创建处理器
    # 1.输出到控制台
    ls = logging.StreamHandler()
    # 2.按天切割日志文件
    lht = logging.handlers.TimedRotatingFileHandler(
        filename=  "./log/test.log{}".format(time.strftime("%Y%m%d%H%M%S")), when="midnight", interval=1,
        backupCount=2)
    # 创建格式化器
    formatter = logging.Formatter(
        fmt="%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    # 给处理器设置格式化器
    ls.setFormatter(formatter)
    lht.setFormatter(formatter)
    # 将处理器添加到日志器
    logger.addHandler(ls)
    logger.addHandler(lht)


