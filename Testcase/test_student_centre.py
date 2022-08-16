from pageobjects.login_page import LoginPage
from testdatas.login_datas import normal_login
import pytest


@pytest.mark.usefixtures("start_web")
class TestStudentCentre():


    # def setUp(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get(coment_testdata.online_login_url)
    #     self.driver.maximize_window()
    #     self.lg = LoginPage(self.driver)
    #     self.lg.login(normal_login["student_id"], normal_login["passwd"])
    #     # self.sc = StudyCenterPage(self.driver)
    #
    # def tearDown(self):
    #     self.driver.quit()


    def test_studentcentre_page(self, start_web):
        # 需要先登陆，才能操作学习中心页面
        start_web["loginpage"].login(normal_login["student_id"], normal_login["passwd"])
        # 调用学习中心页面的元素
        start_web["student_page"].student_centre_page()
        # 断言用例执行完成后，所处在最终页面的元素是否存在；
        # 需要注意的是：上面调用了封装在conftest内的页面元素时，断言还需要调用的就不能通过conftest，否则会出现重复调用导致报错，所以只能直接调用page方法
        assert LoginPage(start_web["driver"]).is_login_batton()
        # self.assertTrue(LoginPage(self.driver).is_login_batton())


if __name__ == '__main__':
    TestStudentCentre()