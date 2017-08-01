# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep


class SafeBagBuild(unittest.TestCase):
    def setUp(self):
        print("RoleBuild case start"),
        self.browser = webdriver.Chrome()
        # self.browser = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
        self.browser.maximize_window()
        # self.browser.get("http://localhost:8080/sitopeuv/")
        self.browser.get("http://192.168.8.88:8888/sitopeuv/")
        # self.browser.get("http://192.168.8.250:8088/sitopeuv/")
        sleep(3)
        # 登录密码
        self.browser.find_element_by_id('userName').send_keys('biandongfeng')
        self.browser.find_element_by_id('userPwd').send_keys('12345678')
        # 登录
        self.browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/p[3]/input').click()
        # 等待
        sleep(5)

    def tearDown(self):
        print("RoleBuild case end")
        sleep(10)
        self.browser.quit()

    def test_safeBagBuild(self):
        # 安全包管理
        self.browser.find_element_by_xpath('/html/body/div/index-header/div[1]/div[1]/div/div[8]/div[1]/i').click()
        sleep(1)
        # 新建
        sleep(1)
        # 删除第一个item
        sleep(1)
        self.browser.find_element_by_xpath('/html/body/div/index-header/div[2]/div[1]/table/tbody/tr[1]/td[3]/button[3]').click()
        sleep(1)


if __name__ == "__main__":
    unittest.main()
