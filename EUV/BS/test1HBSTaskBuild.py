# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep
import sys
from public import Login
from test1FBSEquipmentBuild import BSEquipmentBuild
from test1CBSDepartBuild import BSDepartBuild

reload(sys)
sys.setdefaultencoding('utf8')


class BSTaskBuild(unittest.TestCase):
    """BS端增加任务"""
    # 变量赋值
    task = u'特检任务test'
    security_id = '//select[@ng-model="task.securityPackage.securityId"]/option[2]'
    model_id = '//select[@ng-model="currentEquipment.inspectionModelId"]/option[2]'

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

    def test8_BSTaskBuild(self):
        """BS端增加任务"""
        # 任务管理
        self.browser.find_element_by_xpath('//div[@expander-title="任务管理"]').click()
        sleep(1)
        # 新增
        sleep(2)
        self.browser.find_element_by_xpath('//p[@class="titletop"]/button').click()
        # 表单
        sleep(1)
        # 任务名称
        sleep(1)
        self.browser.find_element_by_xpath('//input[@ng-model="task.taskName"]').send_keys(BSTaskBuild.task)
        # 执行班组
        sleep(1)
        self.browser.find_element_by_xpath('//div[@selected-model="task.executorDeptList"]/div/div/button').click()
        sleep(1)
        self.browser.find_element_by_link_text(BSDepartBuild.group).click()
        # 选择安全包
        sleep(1)
        self.browser.find_element_by_xpath('//select[@ng-model="task.securityPackage.securityId"]').click()
        sleep(1)
        self.browser.find_element_by_xpath(BSTaskBuild.security_id).click()

        # 开始时间
        sleep(1)
        self.browser.find_element_by_id('startDateTime').click()
        sleep(1)
        self.browser.find_element_by_xpath('//td[@class="day ng-binding ng-scope current"]').click()
        sleep(1)
        self.browser.find_element_by_xpath('//span[text()="9:00 AM"]').click()
        sleep(1)
        self.browser.find_element_by_xpath('//span[text()="9:00 AM"]').click()

        # 结束时间
        sleep(1)
        self.browser.find_element_by_id('endDateTime').click()
        sleep(1)
        self.browser.find_element_by_xpath('//td[@class="day ng-binding ng-scope current"]').click()
        sleep(1)
        self.browser.find_element_by_xpath('//span[text()="9:00 PM"]').click()
        sleep(1)
        self.browser.find_element_by_xpath('//span[text()="9:00 PM"]').click()

        # 选择设备
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="tree-root"]/ol/li/ol/li[1]/ol/li[1]/div/input').click()
        sleep(1)
        self.browser.find_element_by_xpath('//span[@title="%s"]' % BSEquipmentBuild.transformer).click()
        # 选择模板
        sleep(1)
        self.browser.find_element_by_xpath('//select[@ng-model="currentEquipment.inspectionModelId"]').click()
        sleep(1)
        self.browser.find_element_by_xpath(BSTaskBuild.model_id).click()

        # 提交
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="footer"]/button[1]').click()

        # 断言页面上新添加的元素是否和断言一致
        sleep(3)
        resultTask = self.browser.find_elements_by_xpath('//td[@data-title-text="巡检任务名称"]')[0].text
        # 去除文件中含有的空格等符号
        resultTask = resultTask.strip()
        print(resultTask),
        sleep(1)
        self.assertEqual(resultTask, BSTaskBuild.task, msg="添加的任务模板与网页上显示的不同！")


if __name__ == '__main__':
    unittest.main()
