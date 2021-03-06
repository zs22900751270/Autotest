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
        u"""分组名不能以空格开头或结尾"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录APP，进入主界面")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("进入服务")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_homeLayout)

        logger.info("进入可视化界面")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "可视化")
        Common.wait(self, 5)

        logger.info("判断是否进入可视化界面")
        title = BaseOperate.get_text_by_id(self, PhoneControl.id_toolbar_title_tv)
        self.assertEqual(title, "数据可视化")

