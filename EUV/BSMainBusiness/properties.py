# coding=utf-8

class RoleData:
    # 新增角色内容
    role_list = [u'巡检组长', u'巡检组员', u'检修组长', u'检修组员']
    remark = u'备注test'


class EquipmentTypeData:
    # 新增角色内容
    equipment_type_list = [u'开关柜7',u'开关柜8',u'开关柜9']
    remark = u'备注test'


class DetectionData:
    # 变量赋值
    qualitative = u'检测项定性test'
    quantify = u'检测项定量test'
    pic = u'检测项拍照test'
    equipment_model = u'设备test模板'
    remark = u'备注test'


class EquipmentData:
    # 变量赋值
    room = u'1#配电室'
    room_type = '//*[@id="roomType"]/option[3]'
    room_remark = u'备注test'


class SafeBagData:
    # 变量赋值
    safe_bag = u'安全包test1'
    remark = u'备注test'
