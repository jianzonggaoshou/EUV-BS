# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep
import sys
from public import Login


reload(sys)
sys.setdefaultencoding('utf8')


class BSUserBuild(unittest.TestCase):
    """BS端增加用户"""
    # 变量赋值
    username = u'testuser'
    true_name = u'许臻'
    password = '123456'
    confirm_password = '123456'
    telephone = '15609100803'
    office_phone = '029-123456'
    user_role = '巡检组长'

    def setUp(self):
        print("start"),
        self.browser = webdriver.Chrome()
        # self.browser = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
        sleep(3)
        Login.user_login(self.browser)
        sleep(5)

    def tearDown(self):
        print("end"),
        sleep(10)
        self.browser.quit()

    def test1_BSUserBuild(self):
        """BS端增加用户"""
        # 滚动翻页
        js = "window.scrollTo(0, 500)"
        self.browser.execute_script(js)
        sleep(3)
        # 系统管理
        self.browser.find_element_by_xpath('//div[@expander-title="系统管理"]').click()
        sleep(1)
        self.browser.find_element_by_link_text('用户管理').click()
        # 滚动翻页
        js = "window.scrollTo(0, 0)"
        self.browser.execute_script(js)
        # 新增
        sleep(1)
        self.browser.find_element_by_id('button2').click()
        # 表单
        self.browser.find_element_by_xpath('//input[@placeholder="请输入用户名"]').send_keys(BSUserBuild.username)
        self.browser.find_element_by_xpath('//input[@placeholder="请输入真实姓名"]').send_keys(BSUserBuild.true_name)
        self.browser.find_element_by_xpath('//input[@placeholder="请输入密码"]').send_keys(BSUserBuild.password)
        self.browser.find_element_by_xpath('//input[@placeholder="请输入确认密码"]').send_keys(BSUserBuild.confirm_password)
        self.browser.find_elements_by_id('tel')[0].send_keys(BSUserBuild.telephone)
        self.browser.find_elements_by_id('tel')[1].send_keys(BSUserBuild.office_phone)

        self.browser.find_element_by_xpath('//button[@ng-class="settings.buttonClasses"]').click()
        self.browser.find_element_by_link_text(BSUserBuild.user_role).click()
        self.browser.find_element_by_xpath('//button[@ng-class="settings.buttonClasses"]').click()
        self.browser.find_element_by_id('new-save').click()

        # 断言页面上新添加的元素是否和断言一致
        sleep(3)
        result = self.browser.find_elements_by_xpath('//td[@data-title-text="用户名"]')[0].text
        print(result),
        sleep(1)
        self.assertEqual(result, BSUserBuild.username, msg="添加的用户名与网页上显示的用户名不同！")


if __name__ == '__main__':
    unittest.main()
