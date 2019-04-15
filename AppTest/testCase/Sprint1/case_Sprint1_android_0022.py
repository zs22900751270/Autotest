#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *

phoneNum = Content.register_count
password = Content.login_password


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
        u"""具体地址"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录app")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("进入我的资料界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_me_icon)

        logger.info("修改地址")
        DZ = "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111" \
             "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111" \
             "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
        BaseOperate.touch_id_by_index(self, PhoneControl.id_address)
        BaseOperate.sendTextById(self, PhoneControl.id_infor_modify, DZ)

        logger.info("查看是否弹出提示")
        self.assertTrue(BaseOperate.find_toast(self, "地址不能超过256字符"))



    
