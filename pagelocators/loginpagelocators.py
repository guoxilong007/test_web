from selenium.webdriver.common.by import By


# 将元素定位方式、页面元素与页面元素操作代码分离，形成参数化
class LoginPageLocators():

    # 学号输入框
    student_id_ele = (By.XPATH, '//input[@placeholder="请输入登录账号" and @class="el-input__inner"]')
    # 密码输入框
    password_ele = (By.XPATH, '//input[@placeholder="请输入密码" and @type="password"]')
    # 登录按钮输入框
    login_batton_ele = (By.XPATH, '//button[@type="button"]//span[text()="登录"]')
    # 记住密码输入框
    ele_remember_passwd = (By.XPATH, '//label[@for="checkbox"]//span[text()="记住密码"]')
    # 提示悬浮窗元素
    msg_ele = (By.XPATH, '//p[@class="el-message__content"]')


class ForgetThePasswd():

    # 忘记密码元素
    batton_forget_password = (By.XPATH, '//button[@type="button"]//span[text()="忘记密码？"]')
    # 忘记密码页面内元素
    student_id_forget_password = (By.XPATH, '//input[@name="studentNumber" and @placeholder="请输入学号"]')
    # 输入验证码元素
    ele_auth_code = (By.XPATH, '//input[@name="verify" and @placeholder="请输入验证码"]')
    # 获取验证码按钮元素
    ele_code_batton = (By.XPATH, '//button[@type ="button"]//span[text()="获取验证码"]')
    # 下一步按钮元素
    ele_next_step = (By.XPATH, '//button[@type ="button"]//span[text()="下一步"]')
