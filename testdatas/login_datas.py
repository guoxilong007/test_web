import datetime
import time

"""
测试用例数据
"""

# 正常场景-登录成功
normal_login = {"student_id":"A190203161", "passwd":"long970224"}

# 异常场景-无效的学号（大于10位取11位，小于10位取9位，学号为空，存在特殊字符，错误的学号）
error_student_id = [
    {"student_id":"A1902031611", "passwd":"long970224", "check":"账户不存在"},
    {"student_id":"A19020316", "passwd":"long970224", "check":"账户不存在"},
    {"student_id":"", "passwd":"long970224", "check":"请输入用户名"},
    {"student_id":"A190203162", "passwd":"long970224", "check":"账户名或密码不正确"},
    {"student_id":"A190203@#¥", "passwd":"long970224", "check":"账户不存在"}
]


# 异常场景-无效的密码（错误的密码，密码为空）
error_passwd = [
    {"student_id":"A190203161", "passwd":"long9702241", "check":"账户名或密码不正确"},
    {"student_id":"A190203161", "passwd":"", "check":"请输入密码"}
]


# 忘记密码弹窗异常场景-（错误的验证码，验证码为空）
error_forget_code = [
    {"student_id":"A190203161", "code":"1111", "check":"验证码错误或过期，请点击刷新"},
    {"student_id":"A190203161", "code":"", "check":"请输入图片验证码"}
]


if __name__ == '__main__':
    test = time.time()
    print(type(test))
    print("{}".format(test))