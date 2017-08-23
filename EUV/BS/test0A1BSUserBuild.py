# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep


class BSAddTest(unittest.TestCase):
    """BS端增加测试"""
    # 变量赋值
    a = 'test'
    username = u'test' + a

    def setUp(self):
        print("test case1 start"),
        self.browser = webdriver.Chrome()
        # self.browser = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
        self.browser.maximize_window()
        self.browser.get("http://172.16.40.5:8888/sitopeuv")
        # self.browser.get("http://114.215.94.141:8060/sitopeuv")
        # self.browser.get("http://localhost:8080/sitopeuv/")
        sleep(3)
        # 登录密码
        self.browser.find_element_by_id('userName').clear()
        self.browser.find_element_by_id('userName').send_keys('biandongfeng')
        self.browser.find_element_by_id('userPwd').clear()
        self.browser.find_element_by_id('userPwd').send_keys('12345678')
        # 登录
        self.browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/p[3]/input').click()
        # 等待
        sleep(5)

    def tearDown(self):
        print("test1 case end")
        sleep(10)
        self.browser.quit()

    def test1_BSUserBuild(self):
        """BS端增加用户"""
        # 滚动翻页
        js = "window.scrollTo(0, 500)"
        self.browser.execute_script(js)
        sleep(3)
        # 系统管理
        self.browser.find_element_by_xpath('/html/body/div/index-header/div/div[2]/div[1]/div/div[11]/div[1]/i').click()
        sleep(1)
        self.browser.find_element_by_link_text('用户管理').click()
        # 滚动翻页
        js = "window.scrollTo(0, 0)"
        self.browser.execute_script(js)
        # 新增
        sleep(1)
        self.browser.find_element_by_id('button2').click()
        # 表单
        self.browser.find_elements_by_xpath('//*[@id="name"]')[0].send_keys(BSAddTest.username)
        self.browser.find_elements_by_xpath('//*[@id="name"]')[1].send_keys(u'许臻')
        self.browser.find_elements_by_xpath('//*[@id="name"]')[2].send_keys('123456')
        self.browser.find_elements_by_xpath('//*[@id="name"]')[3].send_keys('123456')
        self.browser.find_elements_by_id('tel')[0].send_keys('15609100803')
        self.browser.find_elements_by_id('tel')[1].send_keys('029-123456')

        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div[2]/div/form/div[7]/span/div/div/button').click()
        self.browser.find_element_by_link_text('企业管理员').click()
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div[2]/div/form/div[7]/span/div/div/button').click()
        self.browser.find_element_by_id('new-save').click()
