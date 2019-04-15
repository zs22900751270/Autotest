#!/usr/bin/env python
# _*_coding:utf-8_*_


from AppTest.Common import *


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControl.web_url)

    @classmethod
    def tearDown(self):
        logger.info("通过命令修改密码")
        Common.report_screen_shot(self, self.case_name)
        BaseOperate.modify_password_by_phone(self, Content.register_count, Content.login_password)
        Common.quit(self)

    def test_step(self):
        u"""修改密码成功"""
        Common.touch_text_by_class_name(self, ClassName.ivu_col_span_5, "忘记密码", "div")
        Common.wait(self, 10)
        handles = Common.get_window_handle(self)
        Common.switch_window_handle(self, handles[1])
        logger.info("输入手机号")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入手机号",
                                                       "19802990115")

        logger.info("点击获取验证码,判断是否出现错误提示")
        Common.touch_by_id(self, ID.getUpdatePwdCodeBtn)
        identify_code = Common.get_identifying_code(self, Content.register_count)
        logger.info("输入错误的验证码，点击确定，查看错误提示")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入验证码",
                                                       identify_code)
        Common.touch_by_id(self, ID.checkUpdatePwdcodeBtn)

        logger.info("输入符合要求的密码,修改成功后等待10s，返回登录界面")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入密码", "qwe123")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "确认密码", "qwe123")
        Common.touch_by_id(self, ID.updatePasswordBtn)
        Common.wait(self, 10)
        self.assertTrue(Common.check_if_id_exist(self, ID.handleSubmitBtn))

        logger.info("使用新密码登录")
        Common.login_web_client(self, Content.register_count, "qwe123")

        logger.info("判断是否登录成功")
        self.assertTrue(Common.check_if_class_name_exist(self, ClassName.user_info))



     
