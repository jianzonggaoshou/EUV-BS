# coding=utf-8
import unittest
from selenium import webdriver
from time import sleep
from public import Login
import csv


class MainBusiness(unittest.TestCase):
    """BS主业务流程"""

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

    def test2_userBuild(self):
        """BS端增加用户"""
        # 系统管理
        sleep(3)
        self.browser.find_element_by_xpath('//div[@expander-title="系统管理"]').click()
        sleep(1)
        self.browser.find_element_by_link_text('用户管理').click()

        user_file = open('user_info.csv', 'r', encoding='UTF-8')
        user_list = csv.reader(user_file)

        for data in user_list:

            # 新增
            sleep(1)
            self.browser.find_element_by_id('button2').click()
            # 表单
            self.browser.find_element_by_xpath('//input[@placeholder="请输入用户名"]').send_keys(data[0])
            self.browser.find_element_by_xpath('//input[@placeholder="请输入真实姓名"]').send_keys(data[1])
            self.browser.find_element_by_xpath('//input[@placeholder="请输入密码"]').send_keys(data[2])
            self.browser.find_element_by_xpath('//input[@placeholder="请输入确认密码"]').send_keys(data[3])
            self.browser.find_elements_by_id('tel')[0].send_keys(data[4])
            self.browser.find_elements_by_id('tel')[1].send_keys(data[5])
            self.browser.find_element_by_xpath('//button[@ng-class="settings.buttonClasses"]').click()
            self.browser.find_element_by_link_text(data[6]).click()
            self.browser.find_element_by_xpath('//button[@ng-class="settings.buttonClasses"]').click()
            self.browser.find_element_by_id('new-save').click()

            # 断言页面上新添加的元素是否和断言一致
            sleep(3)
            result = self.browser.find_elements_by_xpath('//td[@data-title-text="用户名"]')[0].text
            print(result),
            print(type(result)),
            print(data[0]),
            print(type(data[0])),
            sleep(1)
            self.assertEqual(result, data[0], msg="添加的角色名与网页上显示的角色名不同！")

        user_file.close()


if __name__ == '__main__':
    unittest.main()
