# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep
import sys
from public import Login
from test0A6BSEquipmentBuild import BSEquipmentBuild
from test0A3BSDepartBuild import BSDepartBuild

reload(sys)
sys.setdefaultencoding('utf8')


class BSPlanBuild(unittest.TestCase):
    """BS端增加计划"""
    # 变量赋值
    plan = u'日计划测试test1'
    plan_period_type = '//select[@ng-model="plan.planPeriodType"]/option[2]'
    plan_start_timeInDay_hour = '//select[@ng-model="plan.planStartTimeInDay1"]/option[10]'
    plan_start_timeInDay_minute = '//select[@ng-model="plan.planStartTimeInDay2"]/option[2]'
    plan_start_timeInDay_second = '//select[@ng-model="plan.planStartTimeInDay3"]/option[2]'
    plan_end_timeInDay_hour = '//select[@ng-model="plan.planEndTimeInDay1"]/option[19]'
    plan_end_timeInDay_minute = '//select[@ng-model="plan.planEndTimeInDay2"]/option[2]'
    plan_end_timeInDay_second = '//select[@ng-model="plan.planEndTimeInDay3"]/option[2]'
    security_package = '//select[@ng-model="plan.securityPackage.securityId"]/option[2]'
    plan_description = u'日计划测试test'

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

    def test7_BSPlanBuild(self):
        """BS端增加计划"""
        # 计划管理
        self.browser.find_element_by_xpath('//div[@expander-title="计划管理"]').click()
        sleep(1)
        # 新增
        sleep(2)
        self.browser.find_element_by_xpath('//p[@class="titletop"]/button').click()
        # 表单
        sleep(1)
        # 计划名称
        sleep(1)
        self.browser.find_element_by_xpath('//input[@ng-model="plan.planName"]').send_keys(BSPlanBuild.plan)
        # 周期类型
        sleep(1)
        self.browser.find_element_by_xpath('//select[@ng-model="plan.planPeriodType"]').click()
        sleep(1)
        self.browser.find_element_by_xpath(BSPlanBuild.plan_period_type).click()
        # 开始时间
        # 时
        sleep(1)
        self.browser.find_element_by_xpath('//select[@ng-model="plan.planStartTimeInDay1"]').click()
        sleep(1)
        self.browser.find_element_by_xpath(BSPlanBuild.plan_start_timeInDay_hour).click()
        # 分
        sleep(1)
        self.browser.find_element_by_xpath('//select[@ng-model="plan.planStartTimeInDay2"]').click()
        sleep(1)
        self.browser.find_element_by_xpath(BSPlanBuild.plan_start_timeInDay_minute).click()
        # 秒
        sleep(1)
        self.browser.find_element_by_xpath('//select[@ng-model="plan.planStartTimeInDay3"]').click()
        sleep(1)
        self.browser.find_element_by_xpath(BSPlanBuild.plan_start_timeInDay_second).click()

        # 结束时间
        # 时
        sleep(1)
        self.browser.find_element_by_xpath('//select[@ng-model="plan.planEndTimeInDay1"]').click()
        sleep(1)
        self.browser.find_element_by_xpath(BSPlanBuild.plan_end_timeInDay_hour).click()
        # 分
        sleep(1)
        self.browser.find_element_by_xpath('//select[@ng-model="plan.planEndTimeInDay2"]').click()
        sleep(1)
        self.browser.find_element_by_xpath(BSPlanBuild.plan_end_timeInDay_minute).click()
        # 秒
        sleep(1)
        self.browser.find_element_by_xpath('//select[@ng-model="plan.planEndTimeInDay3"]').click()
        sleep(1)
        self.browser.find_element_by_xpath(BSPlanBuild.plan_end_timeInDay_second).click()

        # 选择班组
        sleep(1)
        self.browser.find_element_by_xpath('//div[@selected-model="plan.executorDeptList"]/div/div/button').click()

        sleep(1)
        self.browser.find_element_by_link_text(BSDepartBuild.group).click()
        sleep(1)
        self.browser.find_element_by_xpath('//div[@selected-model="plan.executorDeptList"]/div/div/button').click()
        # 是否激活
        sleep(1)
        self.browser.find_element_by_xpath('//input[@ng-model="plan.isActivated"]').click()

        # 选择安全包
        sleep(1)
        self.browser.find_element_by_xpath('//select[@ng-model="plan.securityPackage.securityId"]').click()
        sleep(1)
        self.browser.find_element_by_xpath(BSPlanBuild.security_package).click()

        # 计划描述
        sleep(1)
        self.browser.find_element_by_xpath('//textarea[@ng-model="plan.planDescription"]').send_keys(
            BSPlanBuild.plan_description)

        # 选择设备
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="tree-root"]/ol/li/ol/li[1]/ol/li[1]/div/input').click()
        sleep(1)
        self.browser.find_element_by_xpath('//span[@title="%s"]' % BSEquipmentBuild.transformer).click()

        # 选择模板
        sleep(1)
        self.browser.find_element_by_xpath('//select[@ng-model="currentEquipment.inspectionModelId"]').click()
        sleep(1)
        self.browser.find_element_by_xpath('//select[@ng-model="currentEquipment.inspectionModelId"]/option[2]').click()

        # 滚动翻页
        js = "window.scrollTo(0, 500)"
        self.browser.execute_script(js)
        sleep(3)

        # 提交
        self.browser.find_element_by_xpath('//*[@id="footer"]/button[1]').click()

        # 断言页面上新添加的元素是否和断言一致
        sleep(3)
        resultPlan = self.browser.find_elements_by_xpath('//td[@data-title-text="巡检计划名称"]')[0].text
        # 去除文件中含有的空格等符号
        resultPlan = resultPlan.strip()
        print(resultPlan),
        sleep(1)
        self.assertEqual(resultPlan, BSPlanBuild.plan, msg="添加的日计划模板与网页上显示的不同！")


if __name__ == '__main__':
    unittest.main()
