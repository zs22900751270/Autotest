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
        BaseOperate.quit(self)

    def test_step(self):
        u"""新建任务任务内容验证"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击小秘, 进入任务界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_workLayout)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "任务")

        for i in ["mission_content", u"张文生宿舍", "11231324123", u"！@#￥@！@￥"]:
            logger.info("点击创建任务")
            BaseOperate.creat_mission(self, i)

            logger.info("判断任务是否创建成功")
            title_name = BaseOperate.get_text_list_by_id(self, PhoneControl.id_title)
            res1 = BaseOperate.check_text_in_list(self, title_name, i)
            self.assertTrue(res1)


 
    
