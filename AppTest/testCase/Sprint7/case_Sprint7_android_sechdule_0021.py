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
        BaseOperate.delete_schedule_record(self, Content.register_count)
        BaseOperate.quit(self)

    def test_step(self):
        u"""安卓-新建日程选择提醒验证"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录app")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击小秘, 进入任务界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_workLayout)

        logger.info("进入创建日程界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_rfab)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_rfab__content_label_list_label_tv, 3)

        logger.info("查看默认的提醒方式")
        mr_remind = BaseOperate.get_text_by_id(self, PhoneControl.id_remind_option)
        self.assertEqual(mr_remind, "不提醒")

        con = ["提前5分钟", "提前15分钟", "提前30分钟", "提前1小时", "提前1天"]
        for i in con:
            BaseOperate.touch_id_by_index(self, PhoneControl.id_remind_option)
            BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, i)
            BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_left_btn)
            mr_remind = BaseOperate.get_text_by_id(self, PhoneControl.id_remind_option)
            self.assertEqual(mr_remind, i)


