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
        u"""安卓-我的消息点击验证"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击进入设置界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_shezhi)

        logger.info("查看是否进入设置界面")
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_modify_pass))
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_modify_phone))
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_finger_toggle_layout))
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_clear_cache))
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_log_out))


