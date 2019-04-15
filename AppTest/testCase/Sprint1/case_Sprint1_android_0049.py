#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *

phoneNum = Content.register_count
password = Content.login_password
realname = "asdfadzhaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
           "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasssssssssssssssssssssssssssssssss"


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
        u"""输入超长的昵称"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)
        BaseOperate.wait(self, 5)

        logger.info("登录APP")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("进入个人资料界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_me_icon)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_true_name)
        BaseOperate.sendTextById(self, PhoneControl.me_data_mail_input, realname)

        logger.info("判断设置结果")
        statue = BaseOperate.find_toast(self, "真实姓名最大长度40字符")
        self.assertTrue(statue)



    
