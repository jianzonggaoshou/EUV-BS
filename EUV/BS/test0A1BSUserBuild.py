# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class BSUserBuild(unittest.TestCase):
    """BS端增加用户"""
    # 变量赋值
    a = 'test'
    username = u'用户' + a

    def setUp(self):
        print("start"),
        self.browser = webdriver.Chrome()
        # self.browser = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
        self.browser.maximize_window()
        self.browser.get("http://172.16.40.240:8888/sitopeuv")
        sleep(3)
        # 登录密码
        self.browser.find_element_by_id('userName').clear()
        self.browser.find_element_by_id('userName').send_keys('zhenzhen')
        self.browser.find_element_by_id('userPwd').clear()
        self.browser.find_element_by_id('userPwd').send_keys('123456')
        # 登录
        self.browser.find_element_by_xpath('//input[@value="登录"]').click()
        # 等待
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
        self.browser.find_element_by_xpath('//input[@placeholder="请输入真实姓名"]').send_keys(u'许臻')
        self.browser.find_element_by_xpath('//input[@placeholder="请输入密码"]').send_keys('123456')
        self.browser.find_element_by_xpath('//input[@placeholder="请输入确认密码"]').send_keys('123456')
        self.browser.find_elements_by_id('tel')[0].send_keys('15609100803')
        self.browser.find_elements_by_id('tel')[1].send_keys('029-123456')

        self.browser.find_element_by_xpath('//button[@ng-class="settings.buttonClasses"]').click()
        self.browser.find_element_by_link_text('巡检组长').click()
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div[2]/div/form/div[7]/span/div/div/button').click()
        self.browser.find_element_by_id('new-save').click()

        # 断言页面上新添加的元素是否和断言一致
        sleep(3)
        result = self.browser.find_elements_by_xpath('//td[@data-title-text="用户名"]')[0].text
        print(result),
        sleep(1)
        self.assertEqual(result, u'用户test', msg="添加的用户名与网页上显示的用户名不同！")


if __name__ == '__main__':
    unittest.main()
