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
        u"""手机端安卓-游客模式应用评论验证"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)
        app_name = BaseOperate.get_frist_app_name(self)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_app_center_img)
        BaseOperate.sendTextById(self, PhoneControl.search_bar, app_name)
        BaseOperate.touch_search_by_id(self, PhoneControl.search_bar)

        logger.info("点击评论")
        BaseOperate.touch_text_by_id(self, app_name, PhoneControl.id_business_app_name)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "评论")
        text = BaseOperate.get_text_by_id(self, PhoneControl.open_server)
        self.assertEqual(text, "开通应用")


