import os
import datetime




# 获取到顶级目录
top_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

# 日志文件储存路径
log_path =os.path.join(top_path, "Outputs", "logfile", "{}".format(datetime.datetime.now())+".txt")

# 截图文件储存路径
screenshot_path = os.path.join(top_path, "Outputs", "screenshot")

# 测试报告文件保存路径
report_path = os.path.join(top_path, "Outputs", "report", "boxuegu_webtest.html")

# 测试用例目录路径
test_case_path = os.path.join(top_path, "Testcase")



if __name__ == '__main__':
    print(screenshot_path)
    print(report_path)