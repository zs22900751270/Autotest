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
        u"""android—新建会议提醒选择"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击小秘, 进入任务界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_workLayout)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "会议")

        logger.info("进入创建会议界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_rfab)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_rfab__content_label_list_label_tv, 2)
        logger.info("判断提醒可选项")
        remind_list = ["不提醒", "提前5分钟", "提前15分钟", "提前30分钟", "提前1小时", "提前1天"]
        for i in remind_list:
            BaseOperate.touch_id_by_index(self, PhoneControl.id_remind_option)
            BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, i)
            logger.info("判断提醒是否设置成功")
            title_name = BaseOperate.get_text_by_id(self, PhoneControl.id_remind_option)
            self.assertEqual(title_name, i)


 
     
