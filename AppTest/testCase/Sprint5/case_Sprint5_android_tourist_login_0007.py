#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
title = "new_fl"


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
        u"""通知管理页面点击所有分类下方显示所有分类"""
        logger.info("打开App")
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)
        BaseOperate.wait(self, 5)

        logger.info("点击登录")
        BaseOperate.touch_id_by_index(self, PhoneControl.me)
        BaseOperate.touch_id_by_index(self, PhoneControl.login_or_register)
        BaseOperate.wait(self, 3)

        logger.info("点击忘记密码, 进行密码修改")
        BaseOperate.touch_id_by_index(self, PhoneControl.login_forget_password)
        BaseOperate.sendTextById(self, PhoneControl.forget_count, Content.register_count)
        BaseOperate.touch_id_by_index(self, PhoneControl.forget_verify_button)
        BaseOperate.wait(self, 5)
        idenf = BaseOperate.get_identifying_code(self, Content.register_count)
        BaseOperate.sendTextById(self, PhoneControl.forget_verify_input, idenf)
        BaseOperate.touch_id_by_index(self, PhoneControl.forget_next_button)
        BaseOperate.sendTextById(self, PhoneControl.forget_input_password, "qwe123")
        BaseOperate.sendTextById(self, PhoneControl.forget_input_password_again, "qwe123")
        BaseOperate.touch_id_by_index(self, PhoneControl.forget_input_password_next_button)
        result = BaseOperate.checkIfIdExist(self, PhoneControl.login_login_button)
        self.assertTrue(result)

        BaseOperate.touch_id_by_index(self, PhoneControl.login_forget_password)
        BaseOperate.sendTextById(self, PhoneControl.forget_count, Content.register_count)
        BaseOperate.touch_id_by_index(self, PhoneControl.forget_verify_button)
        BaseOperate.wait(self, 5)
        identcode = BaseOperate.get_identifying_code(self, Content.register_count)
        BaseOperate.sendTextById(self, PhoneControl.forget_verify_input, identcode)
        BaseOperate.touch_id_by_index(self, PhoneControl.forget_next_button)
        BaseOperate.sendTextById(self, PhoneControl.forget_input_password, Content.login_password)
        BaseOperate.sendTextById(self, PhoneControl.forget_input_password_again, Content.login_password)
        BaseOperate.touch_id_by_index(self, PhoneControl.forget_input_password_next_button)
        result = BaseOperate.checkIfIdExist(self, PhoneControl.login_login_button)
        self.assertTrue(result)



    
