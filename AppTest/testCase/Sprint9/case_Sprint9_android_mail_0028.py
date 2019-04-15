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

        logger.info("点击是否进入文件上传列表")
        BaseOperate.creat_file_from_window_to_android(self, file_name_1K, folder_name, 1024)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_file)
        if BaseOperate.checkIfIdExist(self, PhoneControl.id_permission_allow_button):
            BaseOperate.touch_id_by_index(self, PhoneControl.id_permission_allow_button)
            BaseOperate.touch_id_by_index(self, PhoneControl.id_upload_file)
            BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "文件")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, folder_name)

        logger.info("上传邮件附件")

        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, file_name_1K)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_btn_addbook, t=0)
        self.assertTrue(Mail_phone.check_upload_file_in_mail(self, file_name_1K))

        logger.info("点击删除已上传附件")
        Mail_phone.del_upload_file_in_mail_by_filename(self, file_name_1K)

        logger.info("查看是否删除成功")
        self.assertFalse(Mail_phone.check_upload_file_in_mail(self, file_name_1K))


 
     
