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
        Mail.del_mail_record_by_user(self, Content.spare_count)
        Mail.del_mail_record_by_user(self, Content.register_count)
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

        logger.info("点击照片，进入上传照片界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_img)
        while BaseOperate.checkIfIdExist(self, PhoneControl.id_permission_allow_button):
            BaseOperate.touch_id_by_index(self, PhoneControl.id_permission_allow_button)

        logger.info("查看是否进入图片上传界面")
        tit_text = BaseOperate.get_text_by_id(self, PhoneControl.id_bar_title)
        self.assertEqual(tit_text, "选择图片和视频")

        logger.info("点击进入文件列表")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_btn_back)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_file)

        logger.info("点击是否进入文件上传列表")
        tv_path = BaseOperate.get_text_by_id(self, PhoneControl.id_tv_path)
        self.assertEqual(tv_path, "/storage/emulated/0")


 
     
