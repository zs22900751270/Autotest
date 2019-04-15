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
        u"""正确的手机号码输入"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        BaseOperate.touch_id_by_index(self, PhoneControl.me)
        BaseOperate.touch_id_by_index(self, PhoneControl.login_or_register)
        BaseOperate.touch_id_by_index(self, PhoneControl.register_button)

        logger.info("输入手机号码")
        BaseOperate.sendTextById(self, PhoneControl.register_phone_num, Content.no_register_count)

        logger.info("删除输入的手机号码")
        BaseOperate.clear_text_by_id(self, PhoneControl.register_phone_num)

        logger.info("判断手机号删除正常")
        text = BaseOperate.get_text_by_id(self, PhoneControl.register_phone_num)
        self.assertEqual(text, "请输入手机号码")

        logger.info("重新输入手机号码, 并点击发送验证码")
        BaseOperate.sendTextById(self, PhoneControl.register_phone_num, Content.no_register_count)
        BaseOperate.touch_id_by_index(self, PhoneControl.register_verify_button)

        logger.info("判断是否可以获取到验证码")
        id_c = BaseOperate.get_identifying_code(self, Content.no_register_count)
        self.assertIsNotNone(id_c)



