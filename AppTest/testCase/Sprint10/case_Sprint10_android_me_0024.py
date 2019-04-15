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
        u"""安卓-设置-修改密码页面-输入新密码和确认新密码不一致"""
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
        BaseOperate.touch_id_by_index(self, PhoneControl.id_next_btn, t=0)

        logger.info("查看是否进入输入新密码界面")
        tit_text = BaseOperate.get_text_by_id(self, PhoneControl.id_toolbar_title_tv)
        self.assertEqual(tit_text, "设置密码")

        logger.info("查看该界面是否存在所有选项")
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_toolbar_left_btn))
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_password_tel_num))
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_password_verify_code_edit))
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_password_next_btn))

        logger.info("输入不合规则的新密码")
        BaseOperate.sendTextById(self, PhoneControl.id_password_tel_num, "qwe123")
        BaseOperate.sendTextById(self, PhoneControl.id_password_verify_code_edit, "123qwe")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_password_next_btn, t=0)

        logger.info("点击是否出现错误提示)")
        self.assertTrue(BaseOperate.find_toast(self, "请输入正确信息"))
        tip_text = BaseOperate.get_text_by_id(self, PhoneControl.id_password_warning_tv)
        self.assertEqual(tip_text, "两次输入密码不一致")

