# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep


class BSDetectionCancel(unittest.TestCase):
    """BS端删除检测项"""

    def setUp(self):
        print("start"),
        self.browser = webdriver.Chrome()
        # self.browser = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
        self.browser.maximize_window()
        self.browser.get("http://172.16.40.240:8888/sitopeuv")
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
        print("end"),
        sleep(10)
        self.browser.quit()

    def test4_BSDetectionCancel(self):
        """BS端删除检测项"""
        # *******************创建设备***********************
        # 资源管理
        # ********************巡检项管理新增******************
        # 滚动翻页
        js = "window.scrollTo(0, 500)"
        self.browser.execute_script(js)
        sleep(3)
        sleep(1)
        self.browser.find_element_by_xpath('/html/body/div/index-header/div/div[2]/div[1]/div/div[12]/div[1]/i').click()
        # 资源管理
        sleep(2)
        self.browser.find_element_by_link_text('检测项管理').click()
        # 滚动翻页
        js = "window.scrollTo(0, 0)"
        self.browser.execute_script(js)
        sleep(3)
        # 删除默认第一个巡检项
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav5-content/div[1]/div[1]/div/div/div/table/tbody/tr[1]/td[3]/button[2]').click()
        # 确认弹出框
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div[1]/index-header/div/div[2]/div[2]/nav5-content/div[6]/div/div/div[3]/button[1]').click()
        # 点选模板管理
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav5-content/div[1]/span[2]').click()
        # 删除第一个模板item
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav5-content/div[1]/div[2]/table/tbody/tr/td[3]/button[2]').click()
        # 确认弹出框
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div[1]/index-header/div/div[2]/div[2]/nav5-content/div[7]/div/div/div[3]/button[1]').click()


if __name__ == '__main__':
    unittest.main()
