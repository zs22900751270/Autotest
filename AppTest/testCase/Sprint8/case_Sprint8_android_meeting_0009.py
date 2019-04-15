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
        u"""查看签到人个人资料"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击小秘, 进入任务界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_workLayout)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "会议")

        logger.info("创建一个会议")
        BaseOperate.creat_meeting(self, "meeting_test", "content", "area")
        logger.info("判断会议是否创建成功")
        title_name = BaseOperate.get_text_by_id(self, PhoneControl.id_title)
        self.assertEqual(title_name, "meeting_test")

        logger.info("进入会议详情界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_title)

        logger.info("判断是否进入会议详情")
        text_con = BaseOperate.get_text_by_id(self, PhoneControl.id_toolbar_title_tv)
        self.assertEqual(text_con, "会议详情")

        logger.info("点击进入会议签到界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_sign_in_layout)

        logger.info("判断是否进入签到详情界面")
        text_con = BaseOperate.get_text_by_id(self, PhoneControl.id_toolbar_title_tv)
        self.assertEqual(text_con, "签到详情")

        logger.info("点击好友信息")
        name_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_name)
        for i in range(len(name_list)):
            BaseOperate.touch_id_by_index(self, PhoneControl.id_name, i+1)
            logger.info("判断是否进入好友资料界面")
            text_con = BaseOperate.get_text_by_id(self, PhoneControl.id_toolbar_title_tv)
            self.assertEqual(text_con, "好友资料")

            logger.info("好友资料界面不可操作")
            check_res = BaseOperate.checkIfIdExist(self, PhoneControl.id_toolbar_right_tv)
            self.assertFalse(check_res)
            BaseOperate.go_back(self)


 
     
