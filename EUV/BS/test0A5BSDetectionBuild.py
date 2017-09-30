# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep
import sys
from public import Login


reload(sys)
sys.setdefaultencoding('utf8')


class BSDetectionBuild(unittest.TestCase):
    """BS端增加检测项"""
    # 变量赋值
    qualitative = u'检测项定性test'
    quantify = u'检测项定量test'
    pic = u'检测项拍照test'
    equipment_model = u'设备test模板'
    remark = u'备注test'

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

    def test5_BSDetectionBuild(self):
        """BS端增加检测项"""
        # *******************创建设备***********************
        # 资源管理
        # ********************巡检项管理新增******************
        # 滚动翻页
        js = "window.scrollTo(0, 500)"
        self.browser.execute_script(js)
        sleep(3)
        # 资源管理
        sleep(1)
        self.browser.find_element_by_xpath('//div[@expander-title="资源管理"]').click()
        sleep(2)
        self.browser.find_element_by_link_text('检测项管理').click()
        # 滚动翻页
        js = "window.scrollTo(0, 0)"
        self.browser.execute_script(js)
        sleep(3)
        # 新增
        sleep(1)
        self.browser.find_element_by_xpath('//button[@ng-click="preaddInspectionItem()"]').click()
        # 表单
        # ***********************定性*************************
        sleep(2)
        self.browser.find_element_by_xpath('//input[@ng-model="inspectionItem.inspectionName"]').send_keys(
            BSDetectionBuild.qualitative)
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
        self.browser.find_element_by_xpath('//button[@ng-click="preaddInspectionItem()"]').click()
        sleep(1)
        self.browser.find_element_by_xpath('//input[@ng-model="inspectionItem.inspectionName"]').send_keys(
            BSDetectionBuild.quantify)
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="elect"]/input[2]').click()
        self.browser.find_element_by_xpath('//input[@ng-model="inspectionItem.quantityUnit"]').send_keys('kV')
        self.browser.find_element_by_xpath('//input[@ng-model="inspectionItem.quantityUplimit"]').send_keys('10')
        self.browser.find_element_by_xpath('//input[@ng-model="inspectionItem.quantityLowlimit"]').send_keys('1')
        # 保存
        sleep(1)
        self.browser.find_element_by_id('all-sava1').click()

        # ********************拍照******************
        # 新增
        sleep(1)
        self.browser.find_element_by_xpath('//button[@ng-click="preaddInspectionItem()"]').click()
        sleep(2)
        self.browser.find_element_by_xpath('//input[@ng-model="inspectionItem.inspectionName"]').send_keys(
            BSDetectionBuild.pic)
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="elect"]/input[3]').click()
        # 保存
        sleep(1)
        self.browser.find_element_by_id('all-sava1').click()

        # 断言页面上新添加的元素是否和断言一致
        sleep(3)
        resultPic = self.browser.find_elements_by_xpath('//td[@data-title-text="巡检项名称"]')[0].text
        print(resultPic),
        resultQualitative = self.browser.find_elements_by_xpath('//td[@data-title-text="巡检项名称"]')[1].text
        print(resultQualitative),
        resultQuantify = self.browser.find_elements_by_xpath('//td[@data-title-text="巡检项名称"]')[2].text
        print(resultQuantify),
        sleep(1)
        self.assertEqual(resultPic, BSDetectionBuild.pic, msg="添加的检测项拍照与网页上显示的不同！")
        self.assertEqual(resultQualitative, BSDetectionBuild.quantify, msg="添加的检测项定量与网页上显示的不同！")
        self.assertEqual(resultQuantify, BSDetectionBuild.qualitative, msg="添加的检测项定性与网页上显示的不同！")

        # ********************模板管理新增******************
        sleep(1)
        self.browser.find_element_by_xpath('//span[@ng-click="getInspectionModelList()"]').click()
        # self.browser.find_element_by_xpath(
        # '/html/body/div/index-header/div/div[2]/div[2]/nav5-content/div[1]/span[2]').click()
        # 新增
        sleep(1)
        self.browser.find_element_by_id('sten-new').click()
        # 表单
        self.browser.find_element_by_id('name').send_keys(BSDetectionBuild.equipment_model)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav5-content/div[4]/div/form/div[2]/textarea').send_keys(
            BSDetectionBuild.remark)
        # 确定
        self.browser.find_element_by_id('sten-save').click()

        # 配置
        sleep(2)
        self.browser.find_element_by_id('sten-amend').click()
        # 选择检测项
        sleep(1)
        self.browser.find_element_by_xpath('//div[@class="checkBox"]/div[1]/input').click()
        sleep(1)
        self.browser.find_element_by_xpath('//div[@class="checkBox"]/div[2]/input').click()
        sleep(1)
        self.browser.find_element_by_xpath('//div[@class="checkBox"]/div[3]/input').click()
        # 确定
        sleep(2)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav5-content/div[5]/div/p[2]/button[1]').click()

        # 断言页面上新添加的元素是否和断言一致
        sleep(3)
        result = self.browser.find_elements_by_xpath('//td[@data-title-text="模板名称"]')[0].text
        print(result),
        sleep(1)
        self.assertEqual(result, BSDetectionBuild.equipment_model, msg="添加的检测项设备模板与网页上显示的不同！")


if __name__ == '__main__':
    unittest.main()
