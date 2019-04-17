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

        logger.info("登录app,进入修改邮箱界面")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_me_icon)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_mail)

        logger.info("输入格式错误的邮箱")
        DZ = "huiyanni@163@163.com"
        BaseOperate.sendTextById(self, PhoneControl.id_infor_modify, DZ)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv, t=0)
        statue = BaseOperate.find_toast(self, "请输入正确的邮箱地址")
        self.assertTrue(statue)

