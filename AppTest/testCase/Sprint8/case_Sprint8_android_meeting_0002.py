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
        u"""android—会议搜索"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击小秘, 进入任务界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_workLayout)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "会议")

        logger.info("点击创建会议")
        for i in range(3):
            BaseOperate.creat_meeting(self, "meeting%s" % i, "content", "area")
            logger.info("判断会议是否创建成功")
            title_name = BaseOperate.get_text_by_id(self, PhoneControl.id_title)
            self.assertEqual(title_name, "meeting%s" % i)

        logger.info("进行搜索会议")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_search)
        BaseOperate.sendTextById(self, PhoneControl.id_search_edit, "meeting2")
        BaseOperate.touch_search_by_id(self, PhoneControl.id_search_edit)

        logger.info("判断是否搜索成功")
        tit_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_title)
        check_res = BaseOperate.check_text_in_list(self, tit_list, "meeting2")
        self.assertTrue(check_res)


 
     
