import logging
from common.getpath import log_path


class WebLog():

    def web_log(self, msg, level):
        # 创建日志名称
        log_name = logging.getLogger("boxuegu")
        # 设置手机log级别
        log_name.setLevel(level)
        # 制定日志的输出格式
        log_format = logging.Formatter("%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s")
        # 日志输出到控制台
        sh = logging.StreamHandler()
        # 输出到控制台的日志级别
        sh.setLevel(level)
        # 日志输出到制定的日志文件内
        fh = logging.FileHandler(log_path, encoding="utf-8")
        # 输出到日志文件内的日志级别
        fh.setLevel(level)
        # 制定的输出格式传入到setformat内
        sh.setFormatter(log_format)
        fh.setFormatter(log_format)
        # 创建日志和输出日志两者对接
        log_name.addHandler(sh)
        log_name.addHandler(fh)

        # 判断level属于那个等级级别，根据级别来调用日志级别的方法
        if level == "DEBUG":
            log_name.debug(msg)
        elif level == "INFO":
            log_name.info(msg)
        elif level == "ERROR":
            log_name.error(msg)
        elif level == "WARNIMG":
            log_name.warning(msg)
        elif level == "CRITICAL":
            log_name.critical(msg)

    def debug(self, msg):
        self.web_log(msg, "DEBUG")

    def info(self, msg):
        self.web_log(msg, "INFO")

    def error(self, msg):
        self.web_log(msg, "ERROR")

    def warning(self, msg):
        self.web_log(msg, "WARNING")

    def critical(self, msg):
        self.web_log(msg, "CRITICAL")


if __name__ == '__main__':
    WebLog().error(212121)
