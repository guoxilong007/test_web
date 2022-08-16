from pageobjects.study_center_page import StudyCenterPage
from testdatas import login_datas
from pageobjects.login_page import LoginPage
import pytest

"""
登录页面测试用例
"""


@pytest.mark.usefixtures("start_web")
class TestLogin():

    # 异常场景---错误的密码
    # pytest参数化写法，直接调用列表数据，且参数名称要与测试用例内的参数名称保持一致
    @pytest.mark.parametrize("passwd_data", login_datas.error_passwd)
    @pytest.mark.smoke
    def test_003_passwd_error(self, start_web, passwd_data):
        # 步骤 1、输入用户名；2、输入错误的密码；3、点击登录
        start_web["loginpage"].login(passwd_data["student_id"], passwd_data["passwd"])
        # 断言 弹出账户名和密码不正确的提示，定位页面内内中部的限时消息提示，需要在sources内进行暂停操作后就可成功定位到该元素
        assert LoginPage(start_web["driver"]).error_msg(), passwd_data["check"]

    # 异常场景---无效的学号（大于10位取11位，小于10位取9位，学号为空，存在特殊字符），使用ddt实现
    # 创建testdatas的py文件包，将测试数据存到testdatas内，在引用测试数据文件包
    @pytest.mark.parametrize("student_id_data", login_datas.error_student_id)
    def test_002_student_id_error(self, start_web, student_id_data):
        # 步骤 1、输入无效的用户名；2、输入密码；3、点击登录
        start_web["loginpage"].login(student_id_data["student_id"], student_id_data["passwd"])
        # 断言 弹出账户不存在的提示
        assert LoginPage(start_web["driver"]).error_msg(), student_id_data["check"]

    # 忘记密码
    @pytest.mark.parametrize("error_code_data", login_datas.error_forget_code)
    def test_001_forget_passwd(self, start_web, error_code_data):
        start_web["loginpage"].login(error_code_data["student_id"], error_code_data["code"])
        # 断言 弹出账户不存在的提示
        assert LoginPage(start_web["driver"]).error_msg(), error_code_data["check"]

    # 正常场景---登录成功
    def test_004_login_success(self, start_web):  #引用driver和登录页面元素时，需要在测试用例函数内传入定义的fixture的函数名称
        # 步骤 1、输入用户名；2、输入错误的密码；3、点击登录
        # start_web["loginpage"]根据返回值进行调用
        start_web["loginpage"].login(login_datas.normal_login["student_id"], login_datas.normal_login["passwd"])
        # 断言 在学习中心页面是否能找到 （您好，郭希龙）学员名字 这个元素
        # start_web["driver"]根据返回值进行调用
        assert StudyCenterPage(start_web["driver"]).is_student_name()

    # @pytest.mark.dome()
    # def test_dome(self):
    #     print("我是dome")
    #     assert False

if __name__ == '__main__':
    pytest.main(['-v', 'test_login.py'])

