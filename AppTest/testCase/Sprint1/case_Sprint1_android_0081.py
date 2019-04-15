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
        u"""输入错误的密码(输入不一致)"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录APP")
        BaseOperate.touch_id_by_index(self, PhoneControl.me)
        BaseOperate.touch_id_by_index(self, PhoneControl.login_or_register)
        BaseOperate.sendTextById(self, PhoneControl.login_count, Content.register_count)
        BaseOperate.sendTextById(self, PhoneControl.login_password, Content.login_password+"2")
        BaseOperate.touch_id_by_index(self, PhoneControl.login_login_button, t=0)

        logger.info("判断是否有提示")
        reslut = BaseOperate.find_toast(self, "手机号或密码输入错误")
        self.assertTrue(reslut)



    
