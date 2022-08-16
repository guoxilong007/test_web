from selenium.webdriver.common.by import By



class StudentPageLocators():
    # 学习中心页面内学生的用户名元素
    student_name_ele = (By.XPATH, '//div[@class="name-wrap"]')
    status_student_centre = (By.CLASS_NAME, "matter-item-content")
    inform_student_centre = (By.CLASS_NAME, "matter-item-content")
    # 退出登录按钮元素
    ele_log_out = (By.XPATH, '//li[@class="el-dropdown-menu__item"]/following-sibling::li')
    # 个人信息按钮元素
    ele_user_info = (By.XPATH, '//li[@class="el-dropdown-menu__item"]/preceding-sibling::li')
    ele_login_batton = (By.XPATH, '//button[@type="button"]//span[text()="登录"]')
    # 个人信息页面内元素
    user_info_page_ele = (By.XPATH, '//div[@class="tab-header"]//div[@class="tab-item active"]')

class SchoolPopup():

    school_info_text = (By.XPATH, '//span[@class="el-dialog__title" and text()="信息填写"]')