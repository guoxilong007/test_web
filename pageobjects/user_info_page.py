from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pagelocators.userinfopagelocators import UserInfoPageLocators
import time


"""
个人信息页面元素操作
"""

class UserInfoPage():

    def __init__(self, driver):
        self.driver = driver

    # 判断个人信息页面内的在读班级tap元素是否存在
    def is_reading_class_ele(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(UserInfoPageLocators.user_info_page_ele))
            return True
        except:
            return False

