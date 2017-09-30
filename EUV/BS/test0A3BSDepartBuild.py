# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep
import sys
from public import Login

reload(sys)
sys.setdefaultencoding('utf8')


class BSDepartBuild(unittest.TestCase):
    """BS端增加部门班组"""
    # 变量赋值
    depart = u'部门test'
    depart_remark = u'备注test'
    group = u'班组test'
    group_remark = u'备注test'

    def setUp(self):
        print("start"),
        self.browser = webdriver.Chrome()
        # self.browser = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
        sleep(3)
        Login.user_login(self.browser)
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
        self.browser.find_element_by_xpath('//textarea[@ng-model="dept.deptRemark"]').send_keys(
            BSDepartBuild.depart_remark)
        # 确定
        self.browser.find_element_by_xpath('//*[@id="footer"]/button[1]').click()
        # *******************************建立DOM树二级***********************************
        sleep(3)
        self.browser.find_element_by_xpath('//span[@title="%s"]' % BSDepartBuild.depart).click()
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
        self.browser.find_element_by_xpath('//textarea[@ng-model="dept.deptRemark"]').send_keys(
            BSDepartBuild.group_remark)
        # 确定
        self.browser.find_element_by_xpath('//*[@id="footer"]/button[1]').click()

        # 断言页面上新添加的元素是否和断言一致
        sleep(3)
        # 点击公司名称
        self.browser.find_element_by_xpath('//span[@title="%s"]' % Login.company).click()
        sleep(1)
        resultDepart = self.browser.find_elements_by_xpath('//td[@data-title-text="部门名称"]')[0].text
        sleep(1)
        self.browser.find_element_by_xpath('//span[@title="%s"]' % BSDepartBuild.depart).click()
        sleep(1)
        resultTeam = self.browser.find_elements_by_xpath('//td[@data-title-text="部门名称"]')[0].text
        print(resultDepart),
        print(resultTeam),
        sleep(1)
        self.assertEqual(resultDepart, BSDepartBuild.depart, msg="添加的部门名与网页上显示的部门名不同！")
        self.assertEqual(resultTeam, BSDepartBuild.group, msg="添加的班组名与网页上显示的班组名不同！")


if __name__ == '__main__':
    unittest.main()
