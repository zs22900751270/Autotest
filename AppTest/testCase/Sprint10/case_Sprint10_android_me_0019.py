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
        u"""安卓-设置-修改密码页面-倒计时内输入正确密码"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击进入设置界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_shezhi)

        logger.info("点击修改密码界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_modify_pass)

        logger.info("点击发送验证码, 输入验证码，点击下一步")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_verify_code_btn)
        iden_code = BaseOperate.get_identifying_code(self, Content.register_count)
        BaseOperate.sendTextById(self, PhoneControl.id_verify_code_edit, iden_code)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_next_btn)

        logger.info("是否进入设置密码界面")
        text_tit = BaseOperate.get_text_by_id(self, PhoneControl.id_toolbar_title_tv)
        self.assertEqual(text_tit, "设置密码")
