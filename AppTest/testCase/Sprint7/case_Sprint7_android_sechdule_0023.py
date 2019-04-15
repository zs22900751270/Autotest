#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        self.driver = deviceDriver.mydriver(self)
        BaseOperate.getprojectpath(self)
        BaseOperate.installApp(self, Content.app_name)
        time.sleep(5)

    @classmethod
    def tearDown(self):
        BaseOperate.report_screen_shot(self, self.case_name)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.delete_schedule_record(self, Content.register_count)
        BaseOperate.quit(self)
        time.sleep(5)

    def test_step(self):
        u"""安卓-新建日程选择重复验证"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录app")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击小秘, 进入任务界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_workLayout)

        logger.info("进入创建日程界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_rfab)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_rfab__content_label_list_label_tv, 3)

        logger.info("查看默认的重复方式")
        mr_remind = BaseOperate.get_text_by_id(self, PhoneControl.id_again_option)
        self.assertEqual(mr_remind, "不重复")

        con = ["每天", "每周", "每月"]
        for i in con:
            BaseOperate.touch_id_by_index(self, PhoneControl.id_again_option)
            BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, i)
            BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_left_btn)
            mr_remind = BaseOperate.get_text_by_id(self, PhoneControl.id_again_option)
            self.assertEqual(mr_remind, i)


 
    
