#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
no_register_count = Content.no_register_count
phoneNum = Content.register_count
password = Content.login_password


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        self.driver = deviceDriver.mydriver(self)
        BaseOperate.installApp(self, Content.app_name)

    @classmethod
    def tearDown(self):
        BaseOperate.report_screen_shot(self, self.case_name)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)

    def test_step(self):
        u"""test step"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)
        BaseOperate.wait(self, 5)
        # 点击我的
        BaseOperate.touch_id_by_index(self, PhoneControl.me)
        # 点击登录或注册
        BaseOperate.touch_id_by_index(self, PhoneControl.login_or_register)
        # 点击注册
        BaseOperate.touch_id_by_index(self, PhoneControl.register_button)
        # 输入超过11位的手机号码
        BaseOperate.sendTextById(self, "com.hqd.app_manager:id/tel_num", "19802990115123")
        # 判断是否可以输入超过11位
        get_text_result = BaseOperate.get_text_by_id(self, "com.hqd.app_manager:id/tel_num")
        self.assertTrue(len(get_text_result) == 11)

        # 输入少于11位的电话号码
        BaseOperate.sendTextById(self, "com.hqd.app_manager:id/tel_num", "1980299011")
        # 判断是否可以输入超过11位
        get_text_result1 = BaseOperate.get_text_by_id(self, "com.hqd.app_manager:id/tel_num")
        get_text_result2 = BaseOperate.get_text_by_id(self, "com.hqd.app_manager:id/warning_tv")
        self.assertTrue(len(get_text_result1) < 11)
        self.assertTrue(get_text_result2 == "请输入11位电话号码")

        # 输入不是电话号码的11位数字
        BaseOperate.sendTextById(self, "com.hqd.app_manager:id/tel_num", "12345678912")
        # 判断是否可以输入超过11位
        get_text_result3 = BaseOperate.get_text_by_id(self, "com.hqd.app_manager:id/tel_num")
        get_text_result4 = BaseOperate.get_text_by_id(self, "com.hqd.app_manager:id/warning_tv")
        self.assertTrue(len(get_text_result3) == 11)
        self.assertTrue(get_text_result4 == "请填入正确的手机号")



    
