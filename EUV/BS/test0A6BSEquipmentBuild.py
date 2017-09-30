# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep
import sys
from public import Login

reload(sys)
sys.setdefaultencoding('utf8')


class BSEquipmentBuild(unittest.TestCase):
    """BS端增加台账"""
    # 变量赋值
    room = u'配电室test'
    room_remark = u'备注test'
    transformer = u'变压器test'
    equipment_type = '//*[@id="equipmentTypeId"]/option[2]'
    room_id = '//*[@id="roomId"]/option[2]'
    equipmentSn = u'设备编号number1'
    equipmentFsn = u'出厂编号number1'
    manufacturer = u'生产厂商number1'
    supplier = u'供应厂商number1'
    working_state = '//*[@id="workingState"]/option[10]'
    equipment_state = '//*[@id="equipmentState"]/option[2]'
    transformer_remark = u'备注test'

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

    def test6_BSEquipmentBuild(self):
        """BS端增加台账"""
        # *******************新增配电室***********************
        # 滚动翻页
        js = "window.scrollTo(0, 500)"
        self.browser.execute_script(js)
        sleep(3)
        # 资源管理
        sleep(1)
        self.browser.find_element_by_xpath('//div[@expander-title="资源管理"]').click()
        sleep(1)
        self.browser.find_element_by_link_text('台账管理').click()
        # 滚动翻页
        js = "window.scrollTo(0, 0)"
        self.browser.execute_script(js)
        sleep(3)
        # 新增配电室
        sleep(2)
        self.browser.find_element_by_id('newRoom').click()
        sleep(1)
        self.browser.find_element_by_id('roomName').send_keys(BSEquipmentBuild.room)
        self.browser.find_element_by_id('roomType').click()
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="roomType"]/option[2]').click()
        self.browser.find_element_by_id('roomRemark').send_keys(BSEquipmentBuild.room_remark)
        # 确定
        self.browser.find_element_by_id('newR-save').click()

        # *******************新增设备***********************
        sleep(2)
        self.browser.find_element_by_id('newEquipment').click()
        # 表单
        # 设备名称
        sleep(1)
        self.browser.find_element_by_id('equipmentName').send_keys(BSEquipmentBuild.transformer)
        # 设备类型
        sleep(1)
        self.browser.find_element_by_id('equipmentTypeId').click()
        sleep(1)
        self.browser.find_element_by_xpath(BSEquipmentBuild.equipment_type).click()
        # 配电室
        sleep(1)
        self.browser.find_element_by_id('roomId').click()
        sleep(1)
        self.browser.find_element_by_xpath(BSEquipmentBuild.room_id).click()
        # 设备编号
        sleep(1)
        self.browser.find_element_by_id('equipmentSn').send_keys(BSEquipmentBuild.equipmentSn)
        # 出厂编号
        sleep(1)
        self.browser.find_element_by_id('equipmentFsn').send_keys(BSEquipmentBuild.equipmentFsn)
        # 生产厂商
        sleep(1)
        self.browser.find_element_by_id('manufacturer').send_keys(BSEquipmentBuild.manufacturer)
        # 供应厂商
        sleep(1)
        self.browser.find_element_by_id('supplier').send_keys(BSEquipmentBuild.supplier)
        # 运行状态
        sleep(1)
        self.browser.find_element_by_id('workingState').click()
        sleep(1)
        self.browser.find_element_by_xpath(BSEquipmentBuild.working_state).click()
        # 设备状态
        sleep(1)
        self.browser.find_element_by_id('equipmentState').click()
        sleep(1)
        self.browser.find_element_by_xpath(BSEquipmentBuild.equipment_state).click()
        # 备注
        sleep(1)
        self.browser.find_element_by_id('equipmentRemark').send_keys(BSEquipmentBuild.transformer_remark)
        # 确定
        sleep(1)
        self.browser.find_element_by_id('newE-save').click()

        # 断言页面上新添加的元素是否和断言一致
        # 点击公司
        sleep(3)
        self.browser.find_element_by_xpath('//span[@title="%s"]' % Login.company).click()
        sleep(1)
        resultRoom = self.browser.find_elements_by_xpath('//td[@data-title-text="配电室名称"]')[0].text
        print(resultRoom),
        sleep(1)
        self.browser.find_element_by_xpath('//span[@title="%s"]' % BSEquipmentBuild.room).click()
        resultTransformer = self.browser.find_elements_by_xpath('//td[@data-title-text="设备名称"]')[0].text
        print(resultTransformer)
        sleep(1)
        self.assertEqual(resultRoom, BSEquipmentBuild.room, msg="添加的配电室与网页上显示的不同！")
        self.assertEqual(resultTransformer, BSEquipmentBuild.transformer, msg="添加的设备与网页上显示的不同！")


if __name__ == '__main__':
    unittest.main()
