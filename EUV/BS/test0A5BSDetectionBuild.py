# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep


class BSAddTest(unittest.TestCase):
    """BS端增加测试"""
    # 变量赋值
    a = 'test'
    equipment_type = u'设备类型' + a

    def setUp(self):
        print("test5 case start"),
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
        print("test5 case end")
        sleep(10)
        self.browser.quit()

    def test5_BSDetectionBuild(self):
        """BS端增加检测项"""
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
        # 新增
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav5-content/div[1]/div[1]/div/div/div/p/button').click()
        # 表单
        # ***********************定性*************************
        sleep(2)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav5-content/div[2]/div/p[2]/input').send_keys(u'检测项定性test')
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="one"]/span').click()
        self.browser.find_element_by_xpath('//*[@id="one"]/span').click()
        self.browser.find_element_by_xpath('//*[@id="one"]/span').click()
        # 输入
        self.browser.find_element_by_xpath('//*[@id="one"]/p[1]/input').clear()
        self.browser.find_element_by_xpath('//*[@id="one"]/p[1]/input').send_keys(u'是')
        self.browser.find_element_by_xpath('//*[@id="one"]/p[2]/input').clear()
        self.browser.find_element_by_xpath('//*[@id="one"]/p[2]/input').send_keys(u'否')
        self.browser.find_element_by_xpath('//*[@id="one"]/p[3]/input').clear()
        self.browser.find_element_by_xpath('//*[@id="one"]/p[3]/input').send_keys(u'是否')
        # 保存
        sleep(1)
        self.browser.find_element_by_id('all-sava1').click()
        # ***********************定量*************************
        # 新增
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav5-content/div[1]/div[1]/div/div/div/p/button').click()
        sleep(2)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav5-content/div[2]/div/p[2]/input').send_keys(u'检测项定量test')
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="elect"]/input[2]').click()
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav5-content/div[2]/div/div[2]/p[1]/input').send_keys(
            'kV')  # ********************巡检项管理新增******************
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav5-content/div[2]/div/div[2]/p[2]/input').send_keys(
            '1')  # ********************巡检项管理新增******************
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav5-content/div[2]/div/div[2]/p[3]/input').send_keys('10')
        # 保存
        sleep(1)
        self.browser.find_element_by_id('all-sava1').click()

        # ********************拍照******************
        # 新增
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav5-content/div[1]/div[1]/div/div/div/p/button').click()
        sleep(2)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav5-content/div[2]/div/p[2]/input').send_keys(u'检测项拍照test')
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="elect"]/input[3]').click()
        # 保存
        sleep(1)
        self.browser.find_element_by_id('all-sava1').click()

        # ********************模板管理新增******************
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav5-content/div[1]/span[2]').click()
        # 新增
        sleep(1)
        self.browser.find_element_by_id('sten-new').click()
        # 表单
        self.browser.find_element_by_id('name').send_keys(u'设备test模板')
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav5-content/div[4]/div/form/div[2]/textarea').send_keys(
            u'test')
        # 确定
        self.browser.find_element_by_id('sten-save').click()

        # 配置
        sleep(2)
        self.browser.find_element_by_id('sten-amend').click()
        # 选择检测项
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav5-content/div[5]/div/div[1]/input').click()
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav5-content/div[5]/div/div[2]/input').click()
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav5-content/div[5]/div/div[3]/input').click()
        # 确定
        sleep(2)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav5-content/div[5]/div/p[4]/button[1]').click()