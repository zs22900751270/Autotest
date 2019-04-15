#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *

phoneNum = Content.register_count
password = Content.login_password
DZ = "huiyanni@.com."


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        warnings.filterwarnings("ignore")
        self.case_name = os.path.basename(__file__)
        self.driver = deviceDriver.mydriver(self)
        BaseOperate.installApp(self, Content.app_name)

    @classmethod
    def tearDown(self):
        BaseOperate.report_screen_shot(self, self.case_name)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)

    def test_step(self):
        u"""和点之间没有字符"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)
        logger.info("登录APP")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("进入我的资料界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_me_icon)

        logger.info("点击修改邮箱")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_mail)

        logger.info("输入不正确格式的邮箱")
        BaseOperate.sendTextById(self, PhoneControl.me_data_mail_input, DZ)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv, t=0)
        self.assertTrue(BaseOperate.find_toast(self, "请输入正确的邮箱地址"))



    
