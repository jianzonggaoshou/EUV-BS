# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep


class BSTaskBuild(unittest.TestCase):
    """BS端增加任务"""
    # 变量赋值
    a = 'test'
    task = u'特检任务' + a

    def setUp(self):
        print("test8 case start"),
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
        print("test8 case end")
        sleep(10)
        self.browser.quit()

    def test8_BSTaskBuild(self):
        """BS端增加任务"""
        # 任务管理
        self.browser.find_element_by_xpath('/html/body/div/index-header/div/div[2]/div[1]/div/div[7]/div[1]/i').click()
        sleep(1)
        # 新增
        sleep(2)
        self.browser.find_element_by_xpath('/html/body/div/index-header/div/div[2]/div[2]/div[1]/p/button').click()
        # 表单
        sleep(1)
        # 任务名称
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div[2]/div/div[1]/input').send_keys(
            BSTaskBuild.task)
        # 执行班组
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/div/button').click()
        sleep(1)
        self.browser.find_element_by_link_text('运行一班').click()
        # 选择安全包
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/select').click()
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/select/option[2]').click()

        # 开始时间
        sleep(1)
        self.browser.find_element_by_id('startDateTime').click()
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div[2]/div/div[3]/div[1]/div/ul/div/table/tbody/tr[1]/td[3]').click()
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div[2]/div/div[3]/div[1]/div/ul/div/table/tbody/tr/td/span[2]').click()
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div[2]/div/div[3]/div[1]/div/ul/div/table/tbody/tr/td/span[1]').click()

        # 结束时间
        sleep(1)
        self.browser.find_element_by_id('endDateTime').click()
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/ul/div/table/tbody/tr[1]/td[3]').click()
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/ul/div/table/tbody/tr/td/span[2]').click()
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/ul/div/table/tbody/tr/td/span[1]').click()

        # 选择设备
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="tree-root"]/ol/li/ol/li[1]/ol/li[1]/div/input').click()
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="tree-root"]/ol/li/ol/li[1]/ol/li[1]/div/span').click()
        # 选择模板
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div[2]/div/div[4]/div[2]/span/select').click()
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div[2]/div/div[4]/div[2]/span/select/option[2]').click()

        # 提交
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div[2]/div/div[5]/button[1]').click()
