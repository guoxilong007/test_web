# 实现异常处理、打印日志、失败截图
# 所有页面公共的部分，不是基于业务部分
import time
from datetime import datetime

from common.weblog import WebLog
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common import getpath



class BasePage:

    # 封装driver对象
    def __init__(self, driver):
        self.driver = driver

    # 等待元素可见
    def wait_eleVisible(self, locator, waittime=30, poll_frequency=0.5, doc=""):
        """
        :param locator:定位方式和定位元素；元组形式（定位方式，定位元素）
        :param timeout: 等待元素最长时长
        :param poll_frequency: 查找元素的时间间隔
        :param doc:模块名称、页面名称、操作名称
        :return:
        """
        WebLog().info("等待元素 {0} 可见".format(locator))
        try:
            # 开始等待的时间，datetime.now()获取到当前时间，second函数为精确到秒
            start = datetime.now().second
            WebDriverWait(self.driver, waittime, poll_frequency).until(EC.visibility_of_element_located(locator))
            # 结束等待的时间
            end = datetime.now().second
            # 求一个差值，写在日志当中，等待了多久;
            # seconds函数为精确到秒
            wait_time = (end - start)
            WebLog().info("开始等待的时间为：{0}，结束等待的时间为：{1}，共等待时长为：{2}".format(start, end, wait_time))
        except:
            WebLog().error("等待元素失败！！！")
            # 截图
            self.save_screenshor(doc)
            raise

    # 等待元素存在
    def wait_elePresence(self):
        pass

    # 查找元素
    def get_element(self, locator, doc=""):
        """
        :param locator: 定位方式和定位元素；元组形式（定位方式，定位元素）
        :param doc: 模块名称、页面名称、操作名称
        :return:
        """
        WebLog().info("所属模块：{0}查到元素：{1}".format(doc, locator))
        try:
            # 要ruturn下，否则点击和输入等操作无法调用到查找元素的方法
            # *locator将元祖内的参数拆开，并且顺序赋值，元祖内的参数为(定位方式,元素)
            return self.driver.find_element(*locator)
        except:
            WebLog().error("查到元素失败！！！")
            # 截图
            self.save_screenshor(doc)
            raise

    # 输入文本
    def input_text(self, text, locator, doc=""):
        WebLog().info("{0} 在{1}元素内，输入的的内容是：{2}".format(doc, locator, text))
        ele = self.get_element(locator)
        try:
            ele.send_keys(text)
        except:
            WebLog().error("输入的是：{}".format(text))
            self.save_screenshor(doc)
            raise

    # 点击操作
    def click_element(self, locator, doc=""):
        WebLog().info("{0} 点击的元素是：{1}".format(doc, locator))
        ele = self.get_element(locator)
        try:
            ele.click()
        except:
            WebLog().error("点击失败")
            self.save_screenshor(doc)
            raise

    # 获取元素的文本内容
    def get_ele_text(self, locator, doc=""):
        WebLog().info("{0} 需要获取文本的元素是：{1}".format(doc, locator))
        ele = self.get_element(locator)
        try:
            # 返回的是文本，所以要returu下
            return ele.text
        except:
            WebLog().error("获取文本失败！！！")
            self.save_screenshor(doc)
            raise

    # 获取元素的属性名
    def get_element_attribute(self, attr, locator, doc=""):
        WebLog().info("{0} 需要获取属性名的元素是：{1}".format(doc, locator))
        ele = self.get_element(locator)
        try:
            return ele.get_attribute(attr)
        except:
            WebLog().error("获取元素的属性名失败！")
            self.save_screenshor(doc)
            raise

    # alert处理
    def alert_action(self):
        pass

    # iframe切换
    def switch_iframe(self):
        pass

    # 上传操作
    def upload_file(self):
        pass

    # 截图操作
    def save_screenshor(self, doc):
        # 图片名称：模块名称、页面名称、操作名称、截图的时间.png
        # screenshot_file将截图文件保存到制定的目录中
        # time.strftime()函数用于格式化时间，返回以可读字符串表示的当地时间，格式参数由format决定；
        # time.localtime([sec])作用格式化时间戳为本地时间，如果sec参数未输入，则以当前时间为转换参数
        screenshot_file = getpath.screenshot_path + "/{0}_{1}.png".format(doc, time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
        try:
            self.driver.save_screenshot(screenshot_file)
            WebLog().info("截图成功，保存路径为：{0}".format(screenshot_file))
        except:
            WebLog().error("截图失败！！！")

    # def elements_get(self, locator, doc=""):
    #     WebLog().info("在{0} 查找元素：{1}".format(doc, locator))
    #     try:
    #         # elements方法需要传入下标
    #         return self.driver.find_elements(*locator)
    #     except:
    #         WebLog().error("查到元素失败：{}".format(locator))
    #         self.save_screenshor(doc)
    #
    # def eles_click(self, locator, doc=""):
    #     WebLog().info("在{0} 查找元素：{1}".format(doc, locator))
    #     eles_0 = self.elements_get(locator)[0]
    #     eles_1 = self.elements_get(locator)[1]
    #     try:
    #         if doc == "0":
    #             return eles_0.clilk()
    #         elif doc == "1":
    #             return eles_1.click()
    #     except:
    #         WebLog().error("点击元素失败：{}".format(locator))
    #         self.save_screenshor(doc)
    #
    # def eles_send_keys(self, text, locator, doc=""):
    #     WebLog().info("在{0} 查找元素：{1}".format(doc, locator))
    #     eles = self.elements_get(locator)
    #     try:
    #         return eles.send_keys(text)
    #     except:
    #         WebLog().error("输入元素失败：{}".format(locator))
    #         self.save_screenshor(doc)


