# coding=utf-8
import unittest
from selenium import webdriver
from time import sleep
from public import Login
from properties import EquipmentTypeData


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

    def test4_equipmentTypeBuild(self):
        """BS端增加角色"""
        # 系统管理
        sleep(3)
        self.browser.find_element_by_xpath('//div[@expander-title="资源管理"]').click()
        sleep(1)
        self.browser.find_element_by_link_text('设备类型管理').click()
        i = 0
        for data in EquipmentTypeData.equipment_type_list:
            """BS端增加设备类型"""
            # 资源管理
            # 新增
            sleep(2)
            self.browser.find_element_by_id('news').click()
            # 表单
            sleep(1)
            self.browser.find_element_by_id('name').send_keys(data)
            self.browser.find_element_by_xpath('//textarea[@ng-model="equipmentType.equipmentTypeRemark"]').send_keys(
                EquipmentTypeData.remark)
            # 确定
            self.browser.find_element_by_id('new-save').click()

            # 断言页面上新添加的元素是否和断言一致
            sleep(3)
            result = self.browser.find_elements_by_xpath('//td[@data-title-text="类型名称"]')[0].text
            print(result),
            print(data),
            sleep(1)
            self.assertEqual(result, data, msg="添加的设备类型与网页上显示的设备类型不同！")


if __name__ == '__main__':
    unittest.main()
