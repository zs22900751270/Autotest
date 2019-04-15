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
        # 输入账号
        BaseOperate.sendTextById(self, "com.hqd.app_manager:id/login_tel_num", no_register_count)
        # 输入密码
        BaseOperate.sendTextById(self, "com.hqd.app_manager:id/login_password_num", password)
        # 点击登陆
        BaseOperate.touch_id_by_index(self, "com.hqd.app_manager:id/next_btn", t=0)
        # 判断是否弹出提示
        get_toast_result = BaseOperate.find_toast(self, "用户不存在，请先注册")
        self.assertTrue(get_toast_result)



    
