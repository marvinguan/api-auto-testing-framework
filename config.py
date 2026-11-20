import logging.handlers
import os
# print(os.path.dirname(os.path.abspath(__file__)))
# 当前目录路径
BASE_DIR = os.path.dirname(__file__)

# 当前项目地址
BASE_URL = "http://localhost:3001"
# 使用日志的高级用法对于logging模块自带的root日志器进行配置的函数
def basic_log_config():
    # 1.创建日志器
    logger = logging.getLogger()
    # 2.设置日志级别
    # 5级别:DEBUG调试级别 INFO信息级别 WARNING警告级别 ERROR错误级别 CRITICAL致命错误
    logger.setLevel(level=logging.INFO)
    # 确保 log 文件夹存在，不存在就自动建一个
    log_dir = os.path.join(BASE_DIR, "log")
    os.makedirs(log_dir, exist_ok=True)
    log_file_path = os.path.join(log_dir, "api_test.log")
    # 3.创建处理器-输出到日志文件
    lht = logging.handlers.TimedRotatingFileHandler(log_file_path, when='midnight',
                                                    interval=1, backupCount=2, encoding="utf8")
    # 4.创建处理器-输出到控制台
    ls = logging.StreamHandler()
    # 5.创建格式化器
    fomatter = logging.Formatter(fmt="%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    # 6.给处理器添加格式化器
    lht.setFormatter(fomatter)
    ls.setFormatter(fomatter)
    # 7.给日至期添加处理器
    logger.addHandler(lht)
    logger.addHandler(ls)


basic_log_config()
