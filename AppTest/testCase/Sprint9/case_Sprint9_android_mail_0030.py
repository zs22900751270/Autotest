#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
folder_name = ".aaaaaa"
file_name_1K = "file_name_1K"


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
        Mail.del_mail_record_by_user(self, Content.spare_count)
        Mail.del_mail_record_by_user(self, Content.register_count)
        BaseOperate.clear_window_local_file(self)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)

    def test_step(self):
        u"""安卓-写邮件-邮件附件选择验证"""
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
        BaseOperate.touch_id_by_index(self, PhoneControl.id_new_mail)
        BaseOperate.sendTextById(self, PhoneControl.id_theme, "theme_1")

        logger.info("点击返回")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_left_btn)

        logger.info("查看是否提示保存草稿")
        text_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_text)
        self.assertTrue(BaseOperate.check_text_in_list(self, text_list, "保存草稿"))
        self.assertTrue(BaseOperate.check_text_in_list(self, text_list, "不保存草稿"))

        logger.info("点击保存草稿")
        BaseOperate.touch_text_by_id(self, "保存草稿", PhoneControl.id_text)

        logger.info("查看草稿箱是否出现+1")
        draft_name = BaseOperate.get_text_by_id(self, PhoneControl.id_drafts_tv)
        logger.info(draft_name)
        self.assertTrue("（1）" in draft_name)


 
     
