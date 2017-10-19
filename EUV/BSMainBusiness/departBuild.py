# coding=utf-8
import unittest
from selenium import webdriver
from time import sleep
from public import Login
import csv


class MainBusiness(unittest.TestCase):
    """BS主业务流程"""

    def setUp(self):
        print("start"),
        self.browser = webdriver.Chrome()
        # self.browser = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
        sleep(3)
        Login.user_login(self.browser)
        sleep(5)

    def tearDown(self):
        print("end"),
        sleep(10)
        self.browser.quit()

    def test3_departBuild(self):
        """BS端增加用户"""
        # 系统管理
        sleep(3)
        self.browser.find_element_by_xpath('//div[@expander-title="系统管理"]').click()
        sleep(1)
        self.browser.find_element_by_link_text('组织部门管理').click()

        user_file = open('depart_info.csv', 'r', encoding='UTF-8')
        user_list = csv.reader(user_file)

        i = 0
        for data in user_list:
            # 新增
            sleep(1)
            self.browser.find_element_by_xpath('//*[@id="box"]/div[2]/p/button').click()
            # 表单
            # 部门名称
            sleep(3)
            self.browser.find_element_by_xpath('//input[@ng-model="dept.deptName"]').send_keys(data[0])
            # 部门类型
            self.browser.find_element_by_xpath('//select[@ng-model="dept.deptType"]').click()
            sleep(1)
            self.browser.find_element_by_xpath('//option[@label="%s"]' % data[1]).click()
            # 备注
            self.browser.find_element_by_xpath('//textarea[@ng-model="dept.deptRemark"]').send_keys(data[2])
            # 确定
            self.browser.find_element_by_xpath('//*[@id="footer"]/button[1]').click()

            # 断言页面上新添加的元素是否和断言一致
            sleep(3)
            result = self.browser.find_elements_by_xpath('//td[@data-title-text="部门名称"]')[i].text
            i = i + 1
            print(result),
            print(type(result)),
            print(data[0]),
            print(type(data[0])),
            sleep(1)
            self.assertEqual(result, data[0], msg="添加的角色名与网页上显示的角色名不同！")

        user_file.close()

        # ——————————————————————————————————选择巡检组人员————————————————————————————————————————————————————————————————
        # 分配人员
        sleep(1)
        self.browser.find_elements_by_xpath('//button[@title="人员"]')[0].click()
        sleep(1)
        self.browser.find_element_by_xpath('//button[text()="分配人员"]').click()
        sleep(1)
        self.browser.find_elements_by_xpath('//input[@ng-model="user.isDeptUser"]')[2].click()
        sleep(1)
        self.browser.find_elements_by_xpath('//input[@ng-model="user.isDeptUser"]')[3].click()
        sleep(1)
        self.browser.find_element_by_xpath('//input[@value="提交"]').click()
        # 指定负责人
        sleep(3)
        self.browser.find_element_by_xpath('//button[text()="指定负责人"]').click()
        sleep(1)
        self.browser.find_elements_by_xpath('//input[@ng-model="user.isAdmin"]')[1].click()
        sleep(1)
        self.browser.find_element_by_xpath('//button[text()="确定"]').click()

        # 浏览器返回
        sleep(1)
        self.browser.back()

        # ——————————————————————————————————选择检修组人员————————————————————————————————————————————————————————————————
        # 分配人员
        sleep(1)
        self.browser.find_elements_by_xpath('//button[@title="人员"]')[1].click()
        sleep(1)
        self.browser.find_element_by_xpath('//button[text()="分配人员"]').click()
        sleep(1)
        self.browser.find_elements_by_xpath('//input[@ng-model="user.isDeptUser"]')[0].click()
        sleep(1)
        self.browser.find_elements_by_xpath('//input[@ng-model="user.isDeptUser"]')[1].click()
        sleep(1)
        self.browser.find_element_by_xpath('//input[@value="提交"]').click()
        # 指定负责人
        sleep(3)
        self.browser.find_element_by_xpath('//button[text()="指定负责人"]').click()
        sleep(1)
        self.browser.find_elements_by_xpath('//input[@ng-model="user.isAdmin"]')[1].click()
        sleep(1)
        self.browser.find_element_by_xpath('//button[text()="确定"]').click()

        # 浏览器返回
        sleep(1)
        self.browser.back()


if __name__ == '__main__':
    unittest.main()
