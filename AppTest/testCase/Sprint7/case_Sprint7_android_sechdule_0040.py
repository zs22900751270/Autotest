#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
sechdule_content = "ri_cheng_xiang_qing"


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        warnings.filterwarnings("ignore")
        self.case_name = os.path.basename(__file__)
        self.driver = deviceDriver.mydriver(self)
        BaseOperate.getprojectpath(self)
        BaseOperate.installApp(self, Content.app_name)

    @classmethod
    def tearDown(self):
        BaseOperate.report_screen_shot(self, self.case_name)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.delete_schedule_record(self, Content.register_count)
        BaseOperate.quit(self)

    def test_step(self):
        u"""安卓-删除日程"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录app")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击小秘, 进入任务界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_workLayout)

        logger.info("创建日程")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_rfab)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_rfab__content_label_list_label_tv, 3)
        BaseOperate.sendTextById(self, PhoneControl.id_content, sechdule_content)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_start_layout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_btnSubmit)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_end_layout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_btnSubmit)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_again_option)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "每天")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_left_btn)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)

        logger.info("进入日程详情界面")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "日程")
        BaseOperate.swipe(self, "up")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, sechdule_content)

        logger.info("点击删除日程-确定删除")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_btn)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "删除日程")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "删除当前日程")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_btn_selectNegative)

        logger.info("判断是否修改成功")
        text_list = BaseOperate.get_text_by_class_name(self, PhoneControl.class_name_TextView)
        res1 = BaseOperate.check_text_in_list(self, text_list, "11111111")
        self.assertFalse(res1)


 
    
