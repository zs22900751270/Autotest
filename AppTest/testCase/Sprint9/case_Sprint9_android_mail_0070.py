#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
file_name = "file_name_1K"
folder_name = ".aaaaaa"


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        warnings.filterwarnings("ignore")
        self.case_name = os.path.basename(__file__)
        self.driver = deviceDriver.mydriver(self)
        # BaseOperate.installApp(self, Content.app_name)

    @classmethod
    def tearDown(self):
        BaseOperate.report_screen_shot(self, self.case_name)
        BaseOperate.del_friend_by_sql(self, Content.register_count, Content.spare_count)
        Mail.del_mail_record_by_user(self, Content.register_count)
        Mail.del_mail_record_by_user(self, Content.spare_count)
        BaseOperate.clear_window_local_file(self)
        BaseOperate.clear_android_local_file(self, folder_name)
        # BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)

    def test_step(self):
        u"""安卓-发件箱-详情页面-附件下载按钮验证"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login_out(self)
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
        BaseOperate.creat_file_from_window_to_android(self, file_name, folder_name)
        Mail_phone.send_mail(self, Content.spare_mail_address, "mail_theme_1", file_name=file_name,
                             folder_name=folder_name)

        logger.info("进入发件箱")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_send_box)

        logger.info("点击进入邮件详情")
        BaseOperate.touch_text_by_id(self, "mail_theme_1", PhoneControl.id_theme)

        logger.info("查看附件下载按钮是否存在")
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_oper))


 
     
