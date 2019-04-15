#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
title = "new_fl"


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
        u"""通知管理页面点击所有分类下方显示所有分类"""
        logger.info("打开App")
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("APP端登录")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击消息通知")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_serviceLayout)

        logger.info("获取分类名称")
        name_list = BaseOperate.get_text_by_class_name(self, PhoneControl.class_name_TextView)
        self.assertTrue(BaseOperate.check_text_in_list(self, name_list, "通知消息"))
        self.assertTrue(BaseOperate.check_text_in_list(self, name_list, "系统消息"))
        self.assertTrue(BaseOperate.check_text_in_list(self, name_list, "系统公告"))



    
