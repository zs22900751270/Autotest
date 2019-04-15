#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *

phoneNum = Content.register_count
password = Content.login_password
nickname = "zhagnsenzhangsen1"


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

        logger.info("登录app")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("进入我的资料界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_me_icon)

        logger.info("点击昵称")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_nick_name)

        logger.info("判断昵称的输入偿长度")
        BaseOperate.sendTextById(self, PhoneControl.id_infor_modify, nickname)
        get_toast = BaseOperate.find_toast(self, "昵称长度不能超过16字符")
        self.assertTrue(get_toast)



    
