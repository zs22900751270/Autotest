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
        # 输入账号
        BaseOperate.sendTextById(self, PhoneControl.login_count, phoneNum)
        # 输入密码
        BaseOperate.sendTextById(self, PhoneControl.login_password, password)
        # 点击登录
        BaseOperate.touch_id_by_index(self, PhoneControl.login_login_button)
        # 点击修改资料
        BaseOperate.touch_id_by_index(self, PhoneControl.id_me_icon)
        # 进入我的资料界面
        statue = BaseOperate.checkIfIdExist(self, PhoneControl.my_data_birthday)
        self.assertTrue(statue)



    
