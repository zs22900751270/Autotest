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
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)

    def test_step(self):
        u"""安卓-写邮件-主题为空验证"""
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

        logger.info("点击写邮件")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_new_mail)

        logger.info("查看输入进入写邮件界面")
        title = BaseOperate.get_text_list_by_id(self, PhoneControl.id_toolbar_title_tv)
        self.assertEqual(title[0], "写邮件")

        logger.info("发送一封无主题的邮件")
        ele_list = BaseOperate.get_results_by_class_name(self, PhoneControl.class_name_EditText)
        BaseOperate.send_text_by_ele(self, ele_list[0], Content.spare_mail_address)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_theme)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)
        logger.info("查看是否弹出‘无主题是否继续发送’提示")
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_btn_selectPositive))
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_btn_selectNegative))

        logger.info("点击否，取消发送邮件")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_btn_selectNegative)
        text_2 = BaseOperate.get_text_by_id(self, PhoneControl.id_toolbar_title_tv)
        self.assertEqual(text_2, "写邮件")

        logger.info("点击发送，点击确定发送")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_btn_selectPositive, 1)
        self.assertTrue(BaseOperate.find_toast(self, "发送成功"))

        logger.info("切换账号")
        BaseOperate.app_login_out(self)
        BaseOperate.app_login(self, Content.spare_count, Content.spare_password)

        logger.info("辅助账号进入邮箱")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_homeLayout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_mail)

        logger.info("查看邮件是否接收成功")
        self.assertTrue(Mail_phone.check_mail_if_exist_by_sender(self, Content.register_count))


 
     
