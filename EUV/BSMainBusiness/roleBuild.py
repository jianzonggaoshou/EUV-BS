# coding=utf-8
import unittest
from selenium import webdriver
from time import sleep
from public import Login
from properties import RoleData


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

    def test1_roleBuild(self):
        """BS端增加角色"""
        # 系统管理
        sleep(3)
        self.browser.find_element_by_xpath('//div[@expander-title="系统管理"]').click()
        sleep(1)
        self.browser.find_element_by_link_text('角色权限').click()
        i = 0
        for data in RoleData.role_list:
            # 新增
            sleep(2)
            self.browser.find_element_by_id('buttonToAdd').click()
            # 表单
            sleep(1)
            self.browser.find_element_by_id('name').send_keys(data)
            self.browser.find_element_by_xpath('//textarea[@ng-model="addRole.roleRemark"]').send_keys(RoleData.remark)
            # 确定
            self.browser.find_element_by_id('new-save').click()
            # 增加权限
            sleep(3)
            self.browser.find_elements_by_id("roleAuth")[i].click()
            i = i + 1
            # 点击全选按钮
            sleep(1)
            self.browser.find_element_by_xpath('//*[text()="全选"]').click()
            # 确定
            sleep(1)
            self.browser.find_element_by_id('jur-save').click()

        # 断言页面上新添加的元素是否和断言一致
        for times in range(0, 4):
            sleep(3)
            result = self.browser.find_elements_by_xpath('//td[@data-title-text="角色名称"]')[times].text
            print(result),
            sleep(1)
            self.assertEqual(result, RoleData.role_list[times], msg="添加的角色名与网页上显示的角色名不同！")


if __name__ == '__main__':
    unittest.main()
