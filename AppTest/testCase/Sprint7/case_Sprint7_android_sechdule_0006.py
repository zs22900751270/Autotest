#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *


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
        BaseOperate.delete_schedule_record(self, Content.register_count)
        BaseOperate.quit(self)

    def test_step(self):
        u"""安卓-新建日程日程内容验证"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录app")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)
        logger.info("点击小秘, 进入任务界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_workLayout)

        logger.info("创建日程")
        BaseOperate.creat_schedule(self, "11111111")
        BaseOperate.creat_schedule(self, "qweqewrwer")
        BaseOperate.creat_schedule(self, "!@###@@@@")

        logger.info("进入小秘-日程界面")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "日程")
        BaseOperate.swipe(self, "up")

        logger.info("判断是否创建成功")
        content_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_content)
        res1 = BaseOperate.check_text_in_list(self, content_list, "11111111")
        res2 = BaseOperate.check_text_in_list(self, content_list, "qweqewrwer")
        res3 = BaseOperate.check_text_in_list(self, content_list, "!@###@@@@")
        self.assertTrue(res1)
        self.assertTrue(res2)
        self.assertTrue(res3)


 
    
