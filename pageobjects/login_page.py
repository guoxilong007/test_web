from pagelocators import loginpagelocators as lpl
import time
from common.basepage import BasePage
from common.weblog import WebLog

"""
需要操作的登录页面元素
"""

class LoginPage(BasePage):

    # 继承BasePage后这个页面内的初始化方法可以去掉
    # # 初始化浏览器，防止用一个页面类就打开一个浏览器
    # def __init__(self, driver):
    #     self.driver = driver

    # 登录步骤;将用户名和密码参数化
    # remember_batton默认为勾选，等于False则不勾选忘记密码按钮，等于True时，则勾选忘记密码按钮
    def login(self, student_id, password, remember_batton=True):
        doc = "登录页面-登录模块"
        WebLog().info(doc)
        # 隐式等待:登录页面内的学号输入框元素；doc需要指明参数，否则会报错，错误为valueerror
        self.wait_eleVisible(lpl.LoginPageLocators().student_id_ele, doc=doc)
        # 操作输入学号的元素；操作元素时可以传入在该方法内定位的doc即可
        # 传入定位方式和定位元素时不需要加*号，因为basepage内find_element将元祖数据处理过了
        self.input_text(student_id, lpl.LoginPageLocators().student_id_ele, doc)
        # 操作输入密码的元素
        self.input_text(password, lpl.LoginPageLocators().password_ele, doc)
        # 判断是否点击记住密码；默认是不选中记住密码
        if remember_batton == False:
            self.click_element(lpl.LoginPageLocators().ele_remember_passwd, doc)
        elif remember_batton == True:
            pass
        # 操作点击登录按钮元素
        self.click_element(lpl.LoginPageLocators().login_batton_ele, doc)
        time.sleep(1)

    # 忘记密码模块
    def forget_password(self, student_id, auth_code):
        doc = "登录页面-忘记密码模块"
        # 等待页面内的忘记密码按钮的元素
        self.wait_eleVisible(lpl.ForgetThePasswd().batton_forget_password, doc=doc)
        # 忘记密码入口
        self.click_element(lpl.ForgetThePasswd().batton_forget_password, doc)
        # 等待忘记密码页面元素展示
        self.wait_eleVisible(lpl.ForgetThePasswd().student_id_forget_password, doc=doc)
        # 操作输入学号元素
        self.input_text(student_id, lpl.ForgetThePasswd().student_id_forget_password, doc)
        # 操作请输入验证码元素
        self.input_text(auth_code, lpl.ForgetThePasswd().ele_auth_code, doc)
        # 操作点击获取验证码元素
        self.click_element(lpl.ForgetThePasswd.ele_code_batton, doc)
        # 操作点击下一步元素
        self.click_element(lpl.ForgetThePasswd.ele_next_step, doc)

    # 判断页面是否跳转，页面没有跳转可以获取到登录按钮就返回true，如果跳转则获取不到登录按钮就返回false
    def is_login_batton(self):
        doc = "登录页面-登录模块"
        try:
            self.wait_eleVisible(lpl.LoginPageLocators().login_batton_ele, doc=doc)
            return True
        except:
            return False

    # 获取到悬浮窗内的文本
    def error_msg(self):
        doc = "登录页面-登录模块"
        self.wait_eleVisible(lpl.LoginPageLocators().msg_ele, doc=doc)
        return self.get_ele_text(lpl.LoginPageLocators.msg_ele, doc)



