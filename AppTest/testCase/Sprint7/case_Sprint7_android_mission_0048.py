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
        BaseOperate.delete_mission_record_by_sql(self, Content.register_count)
        BaseOperate.del_friend_by_sql(self, Content.register_count, Content.spare_count)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)

    def test_step(self):
        u"""任务状态-我转发的验证"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)
        BaseOperate.creat_friend_by_sql(self, Content.register_count, Content.spare_count)

        logger.info("点击小秘, 进入任务界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_workLayout)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "任务")

        logger.info("点击创建任务")
        BaseOperate.creat_mission(self, "mission_content")

        logger.info("标记任务已完成")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_title)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_checkbox)

        logger.info("点击进入已完成界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_left_btn)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_spinner)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "已完成的")

        logger.info("判断是否创建成功")
        tit_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_title)
        resu = BaseOperate.check_text_in_list(self, tit_list, "mission_content")
        self.assertTrue(resu)

        logger.info("进入任务详情")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_title)

        logger.info("转发任务")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_btn)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "转发任务")

        logger.info("选择转发人")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_contact)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_contact_layout, 1)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)

        logger.info("判断是否转发成功")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_spinner)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "我转发的")
        tit_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_title)
        resu = BaseOperate.check_text_in_list(self, tit_list, "mission_content")
        self.assertTrue(resu)


 
    
