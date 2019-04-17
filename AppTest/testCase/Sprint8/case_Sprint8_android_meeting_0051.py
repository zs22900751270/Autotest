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
        u"""android—会议列表搜索"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("创建好友关系")
        BaseOperate.creat_friend_by_sql(self, Content.register_count, Content.spare_count)

        logger.info("点击小秘, 进入会议界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_workLayout)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "会议")

        logger.info("点击创建会议")
        BaseOperate.creat_meeting(self, "meeting_test1", "content", "area")
        BaseOperate.creat_meeting(self, "meeting_test2", "content", "area")
        BaseOperate.creat_meeting(self, "meeting_test3", "content", "area")
        BaseOperate.creat_meeting(self, "meeting_test4", "content", "area")

        logger.info("进行会议搜索")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_search)
        BaseOperate.sendTextById(self, PhoneControl.id_search_edit, "meeting_test1")
        BaseOperate.touch_search_by_id(self, PhoneControl.id_search_edit)
        tit_text = BaseOperate.get_text_list_by_id(self, PhoneControl.id_title)
        self.assertTrue(BaseOperate.check_text_in_list(self, tit_text, "meeting_test1"))


 
     
