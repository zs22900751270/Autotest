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
        BaseOperate.modify_mail_address_by_user(self, Content.register_count, Content.register_mail_address)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)

    def test_step(self):
        u"""登录状态保持成功"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录app")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("进入我的资料界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.me)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_me_icon)

        logger.info("修改资料")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_mail)
        BaseOperate.sendTextById(self, PhoneControl.id_infor_modify, Content.register_mail_address)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)

        logger.info("从后台获取信息，与前台进行比较")
        realname = BaseOperate.get_mail_address_by_user(self, Content.register_count)
        self.assertEqual(realname, Content.register_mail_address)


