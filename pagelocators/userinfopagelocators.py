from selenium.webdriver.common.by import By


# 个人信息页面内的元素
class UserInfoPageLocators:


    # 在读班级元素
    user_info_page_ele = (By.XPATH, '//div[@class="tab-header"]//div[@class="tab-item active"]')