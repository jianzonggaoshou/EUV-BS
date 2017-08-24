# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep


class BSEquipmentTypeBuild(unittest.TestCase):
    """BS端增加设备类型"""
    # 变量赋值
    a = 'test'
    equipment_type = u'设备类型' + a

    def setUp(self):
        print("test4 case start"),
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
        print("test4 case end")
        sleep(10)
        self.browser.quit()

    def test4_BSEquipmentTypeBuild(self):
        """BS端增加设备类型"""
        # 滚动翻页
        js = "window.scrollTo(0, 500)"
        self.browser.execute_script(js)
        sleep(3)
        # 资源管理
        sleep(1)
        self.browser.find_element_by_xpath('/html/body/div/index-header/div/div[2]/div[1]/div/div[12]/div[1]/i').click()
        sleep(1)
        self.browser.find_element_by_link_text('设备类型管理').click()
        # 滚动翻页
        js = "window.scrollTo(0, 0)"
        self.browser.execute_script(js)
        sleep(3)
        # 新增
        sleep(2)
        self.browser.find_element_by_id('news').click()
        # 表单
        sleep(1)
        self.browser.find_element_by_id('name').send_keys(BSEquipmentTypeBuild.equipment_type)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div[2]/div/form/div[2]/textarea').send_keys(u'设备类型test')
        # 确定
        self.browser.find_element_by_id('new-save').click()
