#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *

phoneNum = Content.register_count
password = Content.login_password


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
        u"""test step"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)
        BaseOperate.wait(self, 5)

        logger.info("登录APP")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("修改个人资料，修改住址")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_me_icon)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_address)
        DZ = "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111" \
             "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111" \
             "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
        BaseOperate.sendTextById(self,PhoneControl.id_infor_modify, DZ)
        inputdz = BaseOperate.get_text_by_id(self, PhoneControl.id_infor_modify)
        self.assertTrue(len(DZ) > 256)
        self.assertTrue(len(inputdz) <= 256)



    
