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
        BaseOperate.quit(self)

    def test_step(self):
        u"""安卓-邮箱菜单位置"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击首页, 进入邮箱")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_homeLayout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_mail)

        logger.info("判断是否进入邮箱界面")
        text_1 = BaseOperate.get_text_by_id(self, PhoneControl.id_toolbar_title_tv)
        self.assertEqual(text_1, "邮箱")

        logger.info("邮箱默认显示")
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_bottom_inbox))
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_bottom_my_mail))

        logger.info("进入我的邮箱, 判断功能是否齐全")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_bottom_my_mail)
        function_list = BaseOperate.get_text_by_class_name(self, PhoneControl.class_name_TextView)
        self.assertTrue(BaseOperate.check_text_in_list(self, function_list, "写邮件"))
        self.assertTrue(BaseOperate.check_text_in_list(self, function_list, "收件箱"))
        self.assertTrue(BaseOperate.check_text_in_list(self, function_list, "发件箱"))
        self.assertTrue(BaseOperate.check_text_in_list(self, function_list, "标星邮件"))
        self.assertTrue(BaseOperate.check_text_in_list(self, function_list, "草稿箱"))
        self.assertTrue(BaseOperate.check_text_in_list(self, function_list, "垃圾箱"))


 
     
