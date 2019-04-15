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
        BaseOperate.delete_meeting_record(self, Content.register_count)
        BaseOperate.quit(self)

    def test_step(self):
        u"""android—删除日程"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击小秘, 进入任务界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_workLayout)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "任务")

        logger.info("创建一个任务")
        BaseOperate.creat_mission(self, "mission_test")

        logger.info("判断是否任务创建成功")
        name_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_title)
        check_res1 = BaseOperate.check_text_in_list(self, name_list, "mission_test")
        self.assertTrue(check_res1)

        logger.info("点击删除任务")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "mission_test")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_btn)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "删除任务")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_btn_selectPositive)

        logger.info("判断是否删除创建成功")
        name_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_title)
        check_res1 = BaseOperate.check_text_in_list(self, name_list, "mission_test")
        self.assertFalse(check_res1)


 
     
