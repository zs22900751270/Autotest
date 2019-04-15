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
        # 在不输入手机号码与验证码时点击下一步
        BaseOperate.touch_id_by_index(self, PhoneControl.forget_next_button, t=0)
        # 判断是否出现提示
        status = BaseOperate.find_toast(self, "请输入正确手机号")
        self.assertTrue(status)



    
