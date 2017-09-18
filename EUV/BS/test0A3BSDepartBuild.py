# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep
import sys

reload(sys)
sys.setdefaultencoding('utf8')


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
        self.browser.find_element_by_xpath('//div[@expander-title="系统管理"]').click()
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
        self.browser.find_element_by_xpath('//input[@ng-model="dept.deptName"]').send_keys(BSDepartBuild.depart)
        # 部门类型
        self.browser.find_element_by_xpath('//select[@ng-model="dept.deptType"]').click()
        sleep(1)
        self.browser.find_element_by_xpath('//option[@label="巡检组"]').click()
        # 备注
        self.browser.find_element_by_xpath('//textarea[@ng-model="dept.deptRemark"]').send_keys(u'备注test')
        # 确定
        self.browser.find_element_by_xpath('//*[@id="footer"]/button[1]').click()
        # *******************************建立DOM树二级***********************************
        sleep(3)
        self.browser.find_element_by_xpath('//span[@title="部门test"]').click()
        # 新增
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="box"]/div[2]/p/button').click()
        # 表单
        # 部门名称
        sleep(3)
        self.browser.find_element_by_xpath('//input[@ng-model="dept.deptName"]').send_keys(BSDepartBuild.group)
        # 部门类型
        self.browser.find_element_by_xpath('//select[@ng-model="dept.deptType"]').click()
        sleep(1)
        self.browser.find_element_by_xpath('//option[@label="巡检组"]').click()
        # 备注
        self.browser.find_element_by_xpath('//textarea[@ng-model="dept.deptRemark"]').send_keys(u'备注test')
        # 确定
        self.browser.find_element_by_xpath('//*[@id="footer"]/button[1]').click()

        # 断言页面上新添加的元素是否和断言一致
        sleep(3)
        #点击公司名称
        self.browser.find_element_by_xpath('//span[@title="自动化测试脚本"]').click()
        sleep(1)
        resultDepart = self.browser.find_elements_by_xpath('//td[@data-title-text="部门名称"]')[0].text
        sleep(1)
        self.browser.find_element_by_xpath('//span[@title="部门test"]').click()
        sleep(1)
        resultTeam = self.browser.find_elements_by_xpath('//td[@data-title-text="部门名称"]')[0].text
        print(resultDepart),
        print(resultTeam),
        sleep(1)
        self.assertEqual(resultDepart, u'部门test', msg="添加的部门名与网页上显示的部门名不同！")
        self.assertEqual(resultTeam, u'班组test', msg="添加的班组名与网页上显示的班组名不同！")


if __name__ == '__main__':
    unittest.main()
