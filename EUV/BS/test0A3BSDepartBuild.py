# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep


class BSDepartBuild(unittest.TestCase):
    """BS端增加部门班组"""
    # 变量赋值
    a = 'test'
    depart = u'部门' + a
    group = u'班组' + a

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
        print("end")
        sleep(10)
        self.browser.quit()

    def test3_BSDepartBuild(self):
        """BS端增加部门班组"""
        # 滚动翻页
        js = "window.scrollTo(0, 500)"
        self.browser.execute_script(js)
        sleep(3)
        # 系统管理
        self.browser.find_element_by_xpath('/html/body/div/index-header/div/div[2]/div[1]/div/div[11]/div[1]/i').click()
        sleep(1)
        self.browser.find_element_by_link_text('组织部门管理').click()
        # 滚动翻页
        js = "window.scrollTo(0, 0)"
        self.browser.execute_script(js)
        sleep(3)
        # 新增
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="box"]/div[2]/p/button').click()
        # 表单
        # 部门名称
        sleep(3)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav2-content/div[2]/div/form/div[1]/input').send_keys(
            BSDepartBuild.depart)
        # 部门类型
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav2-content/div[2]/div/form/div[2]/select').click()
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav2-content/div[2]/div/form/div[2]/select/option[2]').click()
        # 备注
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav2-content/div[2]/div/form/div[3]/textarea').send_keys(
            u'备注test')
        # 确定
        self.browser.find_element_by_xpath('//*[@id="footer"]/button[1]').click()
        # *******************************建立DOM树二级***********************************
        sleep(3)
        self.browser.find_element_by_xpath('//*[@id="box"]/div[1]/div/ol/li/ol/li[2]/div/span').click()
        # 新增
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="box"]/div[2]/p/button').click()
        # 表单
        # 部门名称
        sleep(3)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav2-content/div[2]/div/form/div[1]/input').send_keys(
            BSDepartBuild.group)
        # 部门类型
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav2-content/div[2]/div/form/div[2]/select').click()
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav2-content/div[2]/div/form/div[2]/select/option[2]').click()
        # 备注
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav2-content/div[2]/div/form/div[3]/textarea').send_keys(
            u'备注test')
        # 确定
        self.browser.find_element_by_xpath('//*[@id="footer"]/button[1]').click()

        # 断言页面上新添加的元素是否和断言一致
        sleep(3)
        resultDepart = self.browser.find_element_by_xpath(
            '//*[@id="box"]/div[1]/div/ol/li/ol/li[2]/div/span').text
        resultTeam = self.browser.find_element_by_xpath('//*[@id="box"]/div[1]/div/ol/li/ol/li[2]/ol/li/div/span').text
        print(resultDepart),
        print(resultTeam),
        sleep(1)
        self.assertEqual(resultDepart, u'部门test', msg="添加的部门名与网页上显示的部门名不同！")
        self.assertEqual(resultTeam, u'班组test', msg="添加的班组名与网页上显示的班组名不同！")