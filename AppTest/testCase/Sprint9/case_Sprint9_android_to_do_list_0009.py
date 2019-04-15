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
        BaseOperate.delete_meeting_record(self, Content.register_count)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)

    def test_step(self):
        u"""android—已开始的事件从待办列表消失"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击小秘, 进入待办")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_workLayout)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "会议")

        logger.info("创建多个会议")
        BaseOperate.creat_meeting(self, "meeting_test1", "content", "area")

        logger.info("修改会议时间")
        s_time, e_time = BaseOperate.get_start_and_end_time(self, "minute", 10)
        BaseOperate.modify_meeting_time(self, s_time, e_time, "meeting_test1", Content.register_count)

        logger.info("判断是否创建成功,是否按照开始时间排序")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "待办")
        theme_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_theme)
        self.assertEqual(theme_list[0], "meeting_test1")

        logger.info("点击右上角“...”")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "meeting_test1")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_btn)

        logger.info("点击取消会议")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "取消会议")

        logger.info("输入取消会议的原因, 点击确定")
        BaseOperate.sendTextById(self, PhoneControl.id_input, "cancel_reason")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)

        logger.info("判断是否从待办中取消")
        BaseOperate.go_back(self)
        theme_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_theme)
        self.assertFalse(BaseOperate.check_text_in_list(self, theme_list, "meeting_test1"))


 
     
