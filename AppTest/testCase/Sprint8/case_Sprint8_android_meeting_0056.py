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
        BaseOperate.delete_schedule_record(self, Content.spare_count)
        BaseOperate.del_friend_by_sql(self, Content.register_count, Content.spare_count)
        BaseOperate.quit(self)

    def test_step(self):
        u"""android—单日程删除"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击小秘, 进入日程界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_workLayout)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "日程")

        logger.info("点击创建日程")
        BaseOperate.creat_schedule(self, "schedule_test", "content", "每天")

        logger.info("进行修改日程时间")
        s_time, e_time = BaseOperate.get_start_and_end_time(self, "minute", 5)
        BaseOperate.modify_sechdule_time(self, s_time, e_time, "schedule_test", Content.register_count)

        logger.info("进入日程详情,修改日程")
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_workLayout)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "日程")
        BaseOperate.swipe(self, "up")
        BaseOperate.touch_text_by_id(self, "schedule_test", PhoneControl.id_content)

        logger.info("点击删除日程")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_btn)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "删除日程")

        logger.info("判断是否是否出现“删除全部日程”“删除当前日程”")
        text_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_text)
        check_1 = BaseOperate.check_text_in_list(self, text_list, "删除当前日程")
        check_2 = BaseOperate.check_text_in_list(self, text_list, "删除全部日程")
        self.assertTrue(check_1)
        self.assertTrue(check_2)

        logger.info("点击删除当前日程")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "删除当前日程")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_btn_selectPositive)

        logger.info("判断是否删除成功")
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_workLayout)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "日程")
        BaseOperate.swipe(self, "up")
        content_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_content)
        check_3 = BaseOperate.check_text_in_list(self, content_list, "schedule_test")
        self.assertFalse(check_3)


 
     
