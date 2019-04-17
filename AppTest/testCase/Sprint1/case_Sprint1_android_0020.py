#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *

phoneNum = Content.register_count
password = Content.login_password


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
        u"""必选项已填"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)
        logger.info("登录app")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("进入修改资料界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.me)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_me_icon)

        logger.info("设置真实姓名为空")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_mail)
        BaseOperate.sendTextById(self, PhoneControl.id_infor_modify, Content.register_mail_address)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)
        result = BaseOperate.checkIfIdExist(self, PhoneControl.id_mail)
        self.assertTrue(result)


