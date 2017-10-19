# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep
from public import Login
from properties import SafeBagData
import csv


# noinspection SpellCheckingInspection
class MainBusinessBuild(unittest.TestCase):
    """BS端增加安全包"""

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

    def test9_BSSafeBagBuild(self):
        """BS端增加安全包"""
        # 安全包管理
        self.browser.find_element_by_xpath('//div[@expander-title="作业包管理"]').click()
        sleep(1)

        safeBag_file = open('safeBag_info.csv', 'r', encoding='UTF-8')
        safeBag_list = csv.reader(safeBag_file)

        for x in range(9, 10):

            # 页列表
            sleep(1)
            self.browser.find_elements_by_xpath('//button[@title="页列表"]')[x].click()
        # ------------------------------------------------------------------------------------------------------------------
            for data in safeBag_list:
                # 新建
                sleep(1)
                self.browser.find_element_by_xpath('//p[@class="titletop"]/button').click()

                # 页名
                sleep(1)
                self.browser.find_element_by_xpath('//input[@ng-model="page.pageName"]').send_keys(data[0])

                # 页码
                sleep(1)
                self.browser.find_element_by_xpath('//input[@ng-model="page.pageSequence"]').send_keys(data[1])

                sleep(1)
                self.browser.switch_to.frame('ueditor_0')
                sleep(1)
                self.browser.find_element_by_tag_name('body').send_keys(data[2])

                # 跳出框架
                sleep(1)
                self.browser.switch_to.parent_frame()
                # 提交
                sleep(1)
                self.browser.find_element_by_xpath('//*[@id="footer"]/button[1]').click()

            sleep(1)
            self.browser.back()

        safeBag_file.close()


if __name__ == '__main__':
    unittest.main()
