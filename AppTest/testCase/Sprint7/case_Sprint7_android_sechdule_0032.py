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
        u"""安卓-新建日程日程内容验证"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录app")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击小秘, 进入任务界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_workLayout)

        logger.info("创建日程")
        BaseOperate.creat_schedule(self, "11111111")

        logger.info("进入日程详情界面")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "日程")
        BaseOperate.swipe(self, "up")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "11111111")

        logger.info("点击编辑日程")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_btn)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "编辑日程")

        logger.info("修改提醒方式")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_remind_option)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "提前5分钟")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_left_btn)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)

        logger.info("判断是否修改成功")
        text_list = BaseOperate.get_text_by_class_name(self, PhoneControl.class_name_TextView)
        logger.info(text_list)
        res1 = BaseOperate.check_text_in_list(self, text_list, "提前5分钟")
        self.assertTrue(res1)


