import pytest
from selenium import webdriver
from testdatas import coment_testdata as ct
from pageobjects.login_page import LoginPage
from pageobjects.study_center_page import StudyCenterPage
from testdatas import login_datas


"""
fixture
数据准备和数据清理；类似与setup和teardown
需要将fixture封装起来，然后测试用例类直接调用即可，避免了代码冗余
"""
driver = None


# 类的fixture方法
@pytest.fixture(scope="function")
def start_web():
    # 其他的函数也需要用上driver，所以需要声明以下全局变量
    # 前置条件
    global driver
    driver = webdriver.Chrome()
    driver.get(ct.online_login_url)
    driver.maximize_window()
    student_page = StudyCenterPage(driver)
    lg = LoginPage(driver)
    yield {"driver":driver, "loginpage":lg, "student_page":student_page}    # yield 代表分割线，也代表返回值
    # 后置条件
    driver.refresh()
    driver.quit()


# 函数的fixture方法，每个用例执行完后刷新一次web页面
# @pytest.fixture(scope="function")
# def refresh_web():
#     global driver
#     yield
#     driver.refresh()
