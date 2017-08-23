# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep


class BSCancelTest(unittest.TestCase):
    """BS端删除测试"""

    def setUp(self):
        print("test9 case start"),
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
        print("test9 case end")
        sleep(10)
        self.browser.quit()

    def test9_safeBagCancel(self):
        """BS端删除安全包"""
        # 安全包管理
        self.browser.find_element_by_xpath('/html/body/div/index-header/div/div[2]/div[1]/div/div[9]/div[1]/i').click()
        sleep(1)
        # 新建
        sleep(1)
        # 删除第一个item
        sleep(1)
        self.browser.find_element_by_xpath('/html/body/div/index-header/div/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[3]/button[3]').click()
        sleep(1)
