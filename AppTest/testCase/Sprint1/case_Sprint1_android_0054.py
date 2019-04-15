#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *

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
        # 点击忘记密码
        BaseOperate.touch_id_by_index(self, PhoneControl.login_forget_password)
        # 输入手机号码
        BaseOperate.sendTextById(self, PhoneControl.forget_count, phoneNum)
        # 点击获取验证码
        BaseOperate.touch_id_by_index(self, PhoneControl.forget_verify_button)
        # 通过后台获取验证码
        BaseOperate.wait(self, 5)
        identcode = BaseOperate.get_identifying_code(self, phoneNum)
        # 输入验证码
        BaseOperate.sendTextById(self, PhoneControl.forget_verify_input, identcode)
        # 点击下一步
        BaseOperate.touch_id_by_index(self, PhoneControl.forget_next_button)
        # 输入新密码
        BaseOperate.sendTextById(self, PhoneControl.forget_input_password, "qqqq1111")
        # 重复输入密码（两次输入不同密码）
        BaseOperate.sendTextById(self, PhoneControl.forget_input_password_again, "1111qqqq")
        starus = BaseOperate.get_text_by_id(self, PhoneControl.id_password_warning_tv)
        self.assertTrue(starus == "两次输入密码不一致")



    
