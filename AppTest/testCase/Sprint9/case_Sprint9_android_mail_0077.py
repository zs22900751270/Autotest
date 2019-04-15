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
        BaseOperate.del_friend_by_sql(self, Content.register_count, Content.spare_count)
        Mail.del_mail_record_by_user(self, Content.register_count)
        Mail.del_mail_record_by_user(self, Content.spare_count)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)

    def test_step(self):
        u"""安卓-发件箱-详情页面-转发页面发送验证"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)
        BaseOperate.creat_friend_by_sql(self, Content.register_count, Content.spare_count)

        logger.info("点击首页, 进入邮箱")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_homeLayout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_mail)

        logger.info("判断是否进入邮箱界面")
        text_1 = BaseOperate.get_text_by_id(self, PhoneControl.id_toolbar_title_tv)
        self.assertEqual(text_1, "邮箱")

        logger.info("进入我的邮箱")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_bottom_my_mail)

        logger.info("发送邮件")
        Mail_phone.send_mail(self, Content.spare_mail_address, "mail_theme_1", mail_content="123")

        logger.info("进入发件箱")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_send_box)

        logger.info("点击进入邮件详情")
        BaseOperate.touch_text_by_id(self, "mail_theme_1", PhoneControl.id_theme)

        logger.info("点击转发")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_forward)

        logger.info("输入转发人信息")
        ele_list = BaseOperate.get_results_by_class_name(self, PhoneControl.class_name_EditText)
        BaseOperate.send_text_by_ele(self, ele_list[0], Content.register_mail_address)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_theme)

        logger.info("点击返回")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_left_btn)

        logger.info("弹出提示")
        text_list = BaseOperate.get_text_by_class_name(self, PhoneControl.class_name_TextView)
        self.assertTrue(BaseOperate.check_text_in_list(self, text_list, "保存草稿"))
        self.assertTrue(BaseOperate.check_text_in_list(self, text_list, "不保存草稿"))

        logger.info("点击继续,回到邮件详情界面")
        BaseOperate.touch_text_by_id(self, "不保存草稿", PhoneControl.id_text)
        tit_text = BaseOperate.get_text_by_id(self, PhoneControl.id_toolbar_title_tv)
        self.assertEqual(tit_text, "邮件详情")


 
     
