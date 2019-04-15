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
        BaseOperate.delete_meeting_record(self, Content.spare_count)
        BaseOperate.del_friend_by_sql(self, Content.register_count, Content.spare_count)
        BaseOperate.quit(self)

    def test_step(self):
        u"""android—会议列表界面筛选显示会议信息"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("创建好友关系")
        BaseOperate.creat_friend_by_sql(self, Content.register_count, Content.spare_count)

        logger.info("点击小秘, 进入会议界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_workLayout)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "会议")

        logger.info("点击创建会议")
        BaseOperate.creat_meeting(self, "meeting_test", "content", "area")

        logger.info("判断会议时间，参会人，地点，组织者是否存在")
        check_1 = BaseOperate.checkIfIdExist(self, PhoneControl.id_date)
        check_2 = BaseOperate.checkIfIdExist(self, PhoneControl.id_creator)
        check_3 = BaseOperate.checkIfIdExist(self, PhoneControl.id_take_in)
        check_4 = BaseOperate.checkIfIdExist(self, PhoneControl.id_locate)
        self.assertTrue(check_1)
        self.assertTrue(check_2)
        self.assertTrue(check_3)
        self.assertTrue(check_4)


 
     
