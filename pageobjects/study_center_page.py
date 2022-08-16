import time
from pagelocators.studentpageloactors import StudentPageLocators as stu
from pagelocators.studentpageloactors import SchoolPopup
from common.basepage import BasePage
from common.weblog import WebLog



"""
学习中心的页面操作
"""
class StudyCenterPage(BasePage):

    # 判断学习中心页面内是否有学生的用户名元素存在，如果有则返回true，没有则返回false
    def is_student_name(self):
        doc = "学习中心页面"
        # student_name_ele = '//div[@class="name"]'
        try:
            self.wait_eleVisible(stu.student_name_ele, doc=doc)
            return True
        except:
            return False

    # 学习中心页面元素操作
    def student_centre_page(self):
        doc = "学习中心页面"
        WebLog().info(doc)
        # 显示等待学习中心内页面的操作元素
        self.wait_eleVisible(stu.student_name_ele, doc=doc)
        # 点击学籍信息icon
        # 此处使用的elements方法，elements方法没有封装在basepage内，所以在使用elements方法的地方try一下并定位失败后截图
        try:
            WebLog().info("点击成功")
            self.driver.find_elements(*stu.status_student_centre)[0].click()
        except:
            WebLog().error("点击失败{}".format(stu.status_student_centre))
            self.save_screenshor(doc)
        # self.eles_click(*stu.status_student_centre, doc=0)
        time.sleep(1)
        # 点击通知icon
        try:
            WebLog().info("点击成功")
            self.driver.find_elements(*stu.inform_student_centre)[1].click()
        except:
            WebLog().error("点击失败{}".format(stu.inform_student_centre))
            self.save_screenshor(doc)
        # self.eles_click(*stu.inform_student_centre, doc=1)
        time.sleep(1)
        self.driver.refresh()
        self.wait_eleVisible(stu.student_name_ele, doc=doc)
        # 点击登录用户的头像
        self.click_element(stu.student_name_ele, doc)
        # 显示等待个人信息按钮元素是否显示
        self.wait_eleVisible(stu.ele_user_info, doc=doc)
        # 点击个人信息按钮
        self.click_element(stu.ele_user_info, doc)
        # 等待个人中心页面元素出现
        self.wait_eleVisible(stu.user_info_page_ele, doc=doc)
        time.sleep(1)
        # 页面返回到上一级
        self.driver.back()
        # 页面返回至上一页后，需要显示等待学习中心页面元素
        self.wait_eleVisible(stu.student_name_ele, doc=doc)
        # 点击登录用户的头像
        self.click_element(stu.student_name_ele, doc)
        self.wait_eleVisible(stu.ele_log_out, doc=doc)
        # 点击退出账号按钮
        self.click_element(stu.ele_log_out, doc)
        self.wait_eleVisible(stu.ele_login_batton, doc=doc)

    def school_roll_popup(self):
        doc = "学籍页面"
        # 显示等待学习中心内页面的操作元素
        self.wait_eleVisible(stu.student_name_ele, doc=doc)
        # 点击学籍信息icon
        try:
            WebLog().info("点击成功")
            self.driver.find_elements(*stu.status_student_centre)[0].click()
        except:
            WebLog().error("点击失败{}".format(stu.status_student_centre))
            self.save_screenshor(doc)
        # self.eles_click(*stu.status_student_centre, doc=0)
        time.sleep(1)
        # 等待学籍信息弹窗元素
        self.wait_eleVisible(SchoolPopup.school_info_text, doc=doc)
        #

