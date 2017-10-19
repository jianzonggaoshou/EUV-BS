# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep
from public import Login
from properties import EquipmentData
import csv


class MainBusinessBuild(unittest.TestCase):
    """BS端增加台账"""

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

    def test6_EquipmentBuild(self):
        """BS端增加台账"""
        # *******************新增配电室***********************
        sleep(3)
        # 资源管理
        sleep(1)
        self.browser.find_element_by_xpath('//div[@expander-title="资源管理"]').click()
        sleep(1)
        self.browser.find_element_by_link_text('台账管理').click()

        equipment1_file = open('equipment1_info.csv', 'r', encoding='UTF-8')
        equipment1_list = csv.reader(equipment1_file)

        # 新增配电室
        sleep(3)
        self.browser.find_element_by_id('newRoom').click()
        sleep(1)
        self.browser.find_element_by_id('roomName').send_keys(EquipmentData.room)
        self.browser.find_element_by_id('roomType').click()
        sleep(1)
        self.browser.find_element_by_xpath(EquipmentData.room_type).click()
        self.browser.find_element_by_id('roomRemark').send_keys(EquipmentData.room_remark)
        # 确定
        self.browser.find_element_by_id('newR-save').click()

        # 断言页面上新添加的元素是否和断言一致
        sleep(1)
        resultRoom = self.browser.find_elements_by_xpath('//td[@data-title-text="配电室名称"]')[0].text
        print(resultRoom),
        sleep(1)
        self.assertEqual(resultRoom, EquipmentData.room, msg="添加的配电室与网页上显示的不同！")

        # *******************新增设备***********************
        # 选择配电室
        sleep(1)
        self.browser.find_element_by_xpath('//span[@title="%s"]' % EquipmentData.room).click()

        # --------------------------------------------------------------------------------------------------------------
        for data in equipment1_list:
            sleep(2)
            self.browser.find_element_by_id('newEquipment').click()
            # 表单
            # 设备名称
            sleep(1)
            self.browser.find_element_by_id('equipmentName').send_keys(data[0])
            # 设备类型
            sleep(1)
            self.browser.find_element_by_id('equipmentTypeId').click()
            sleep(1)
            self.browser.find_element_by_xpath(data[1]).click()
            # 电压等级
            sleep(1)
            self.browser.find_element_by_id('voltageLevel').click()
            sleep(1)
            self.browser.find_element_by_xpath(data[2]).click()
            # 设备位号
            sleep(1)
            self.browser.find_element_by_id('itemNumber').send_keys(data[3])
            # 设备编号
            sleep(1)
            self.browser.find_element_by_id('equipmentSn').send_keys(data[4])
            # 出厂编号
            sleep(1)
            self.browser.find_element_by_id('equipmentFsn').send_keys(data[5])
            # 生产厂商
            sleep(1)
            self.browser.find_element_by_id('manufacturer').send_keys(data[6])
            # 供应厂商
            sleep(1)
            self.browser.find_element_by_id('supplier').send_keys(data[7])
            # 运行状态
            sleep(1)
            self.browser.find_element_by_id('workingState').click()
            sleep(1)
            self.browser.find_element_by_xpath(data[8]).click()
            # 设备状态
            sleep(1)
            self.browser.find_element_by_id('equipmentState').click()
            sleep(1)
            self.browser.find_element_by_xpath(data[9]).click()
            # --------------------------------------------------------------------------------------------------------------
            # 生产时间
            sleep(1)
            self.browser.find_element_by_id('manufactureTime').click()
            sleep(1)
            self.browser.find_element_by_xpath('//td[@class="day ng-binding ng-scope current"]').click()
            # 安装时间
            sleep(1)
            self.browser.find_element_by_id('installTimeTime').click()
            sleep(1)
            self.browser.find_element_by_xpath('//td[@class="day ng-binding ng-scope current"]').click()
            # 运行时间
            sleep(1)
            self.browser.find_element_by_id('startTimeTime').click()
            sleep(1)
            self.browser.find_element_by_xpath('//td[@class="day ng-binding ng-scope current"]').click()
            # --------------------------------------------------------------------------------------------------------------
            # 备注
            sleep(1)
            self.browser.find_element_by_id('equipmentRemark').send_keys(data[10])
            # 确定
            sleep(1)
            self.browser.find_element_by_id('newE-save').click()

            # 断言页面上新添加的元素是否和断言一致
            sleep(1)
            resultTransformer = self.browser.find_elements_by_xpath('//td[@data-title-text="设备名称"]')[0].text
            print(resultTransformer)
            sleep(1)
            self.assertEqual(resultTransformer, data[0], msg="添加的设备与网页上显示的不同！")

        equipment1_file.close()


if __name__ == '__main__':
    unittest.main()
