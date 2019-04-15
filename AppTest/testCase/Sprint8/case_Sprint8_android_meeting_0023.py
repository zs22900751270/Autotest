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
        u"""android—创建会议界面发送按钮正常可用"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击小秘, 进入会议界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_workLayout)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "会议")

        logger.info("点击创建会议")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_rfab)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_rfab__content_label_list_label_tv, 2)
        BaseOperate.sendTextById(self, PhoneControl.id_theme, "meeting_theme")
        BaseOperate.sendTextById(self, PhoneControl.id_content, "meeting_content")
        BaseOperate.hide_keyboard(self)
        BaseOperate.sendTextById(self, PhoneControl.id_locate, "meeting_area")
        BaseOperate.hide_keyboard(self)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_take_in_layout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_contact)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_contact_layout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)

        logger.info("点击取消")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_left_btn)

        logger.info("判断会议是否创建成功")
        title_name = BaseOperate.get_text_list_by_id(self, PhoneControl.id_title)
        check_res111 = BaseOperate.check_text_in_list(self, title_name, "meeting_theme")
        self.assertFalse(check_res111)


 
     
