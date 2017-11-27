# coding=utf-8
class Login:
    # 变量赋值
    company = 'sun公司'

    # 登录
    @staticmethod
    def user_login(browser):
        # 登录密码
        browser.maximize_window()
        browser.get("http://172.16.40.240:8888/sitopeuv")
        browser.find_element_by_id('userName').clear()
        browser.find_element_by_id('userName').send_keys('15609109999')
        browser.find_element_by_id('userPwd').clear()
        browser.find_element_by_id('userPwd').send_keys('123456')
        # 登录
        browser.find_element_by_xpath('//input[@value="登录"]').click()
        # 等待