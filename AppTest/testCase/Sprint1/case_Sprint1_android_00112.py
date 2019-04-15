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
        # 点击我的
        BaseOperate.touch_id_by_index(self, PhoneControl.me)
        # 点击登录或注册
        BaseOperate.touch_id_by_index(self, PhoneControl.login_or_register)
        # 点击注册
        BaseOperate.touch_id_by_index(self, PhoneControl.register_button)
        # 输入手机号码
        BaseOperate.sendTextById(self, PhoneControl.id_tel_num, no_register_count)
        # 点击获取验证码
        BaseOperate.touch_id_by_index(self, PhoneControl.id_verify_code_btn)
        # 输入错误的验证码
        BaseOperate.sendTextById(self, PhoneControl.id_verify_code_edit, "123456")
        # 点击下一步
        BaseOperate.touch_id_by_index(self, PhoneControl.id_next_btn, t=0)
        self.assertTrue(BaseOperate.find_toast(self, "验证码输入错误"))



    
