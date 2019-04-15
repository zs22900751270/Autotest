#!/usr/bin/env python
# _*_coding:utf-8_*_


from AppTest.Common import *
revised_name = "newname1234zs"
revised_name_1 = "zhangsen1234zs"


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControl.web_url)

    @classmethod
    def tearDown(self):
        Common.report_screen_shot(self, self.case_name)
        Common.quit(self)

    def test_step(self):
        u"""手机号和密码和服务端一致"""
        logger.info("web端登录")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("判断是否登陆成功")
        get_login_result = Common.check_if_class_name_exist(self, ClassName.user_info)
        self.assertTrue(get_login_result)

        logger.info("进行前后台对比")
        get_info = Ldap.ldap_cn_list(self, "user", "ou=users", "cn=%s" % Content.register_count)
        result = str(get_info[0])
        self.assertTrue(Content.register_count in result)
        self.assertTrue(Content.login_password in result)



     
