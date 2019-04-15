#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *

no_register_count = Content.no_register_count
phoneNum = Content.register_count
password = Content.login_password
name = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaadddddddaaaaaasssssssssssssssssssssssssssssssssssssssssssssssss" \
       "ssajdksfhjakhflkadhskjaksnajncjaksdakjfdfffffffffffffffffffsssssss"


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        self.case_name = os.path.basename(__file__)
        self.driver = deviceDriver.mydriver(self)
        BaseOperate.installApp(self, Content.app_name)

    @classmethod
    def tearDown(self):
        BaseOperate.report_screen_shot(self, self.case_name)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)

    def test_step(self):
        u"""test step"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)
        BaseOperate.wait(self, 5)

        logger.info("登录app")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击应用中心")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_app_center_img)

        logger.info("判断搜索框限制50个字符")
        BaseOperate.sendTextById(self, PhoneControl.search_bar, name)
        get_result_input = BaseOperate.get_text_by_id(self, PhoneControl.search_bar)
        BaseOperate.wait(self, 1)
        self.assertTrue(len(name) >= 50)
        self.assertTrue(len(get_result_input) <= 50)



    
