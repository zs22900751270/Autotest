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
        u"""安卓-设置-修改密码页面-发送验证码"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击进入设置界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_shezhi)

        logger.info("点击修改密码界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_modify_pass)

        logger.info("点击发送验证码, 输入验证码，点击下一步")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_verify_code_btn)
        BaseOperate.sendTextById(self, PhoneControl.id_verify_code_edit, "123456")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_next_btn, t=0)
        self.assertTrue(BaseOperate.find_toast(self, "验证码输入错误"))
