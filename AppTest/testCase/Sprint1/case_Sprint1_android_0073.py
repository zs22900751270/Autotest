#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
# import warnings
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
        # 在手机号码框输入英文
        BaseOperate.touch_id_by_index(self, "com.hqd.app_manager:id/tel_num")
        BaseOperate.input_text_by_cmd(self, "zhangsen")
        # 不能输入
        reslut_input_num = BaseOperate.get_text_by_id(self, "com.hqd.app_manager:id/tel_num")
        # 判断是否可以输入
        last_reslut = True
        if reslut_input_num == "请输入手机号码":
            pass
        else:
            last_reslut = False
        self.assertTrue(last_reslut)



    
