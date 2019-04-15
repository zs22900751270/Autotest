#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        self.driver = deviceDriver.mydriver(self)
        BaseOperate.installApp(self, Content.app_name)

    @classmethod
    def tearDown(self):
        BaseOperate.report_screen_shot(self, self.case_name)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.delete_mission_record_by_sql(self, Content.register_count)
        BaseOperate.quit(self)

    def test_step(self):
        u"""任务详情验证"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击小秘, 进入任务界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_workLayout)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "任务")

        logger.info("点击创建任务")
        BaseOperate.creat_mission(self, "mission_content1", "123412341234")

        logger.info("进入任务详情界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_title)

        logger.info("查看是否进入任务详情")
        task_detail = BaseOperate.get_text_list_by_id(self, PhoneControl.id_toolbar_title_tv)
        resu = BaseOperate.check_text_in_list(self, task_detail, "任务详情")
        self.assertTrue(resu)

        logger.info("点击修改任务")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_btn)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "编辑任务")

        logger.info("清空备注")
        BaseOperate.clear_text_by_id(self, PhoneControl.id_remark)

        logger.info("点击保存")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)

        logger.info("是否保存成功")
        task_detail = BaseOperate.get_text_list_by_id(self, PhoneControl.id_toolbar_title_tv)
        resu = BaseOperate.check_text_in_list(self, task_detail, "任务详情")
        self.assertTrue(resu)


 
    