#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *


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
        u"""安卓-邮箱菜单位置"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("查看我的界面中选项是否完整")
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_shenpi))
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_my_msg))
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_guanyuwomen))
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_update))
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_feedback))
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_shezhi))

