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
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)

    def test_step(self):
        u"""安卓-写邮件-抄送人支持通讯录选择和手动输入"""
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

        logger.info("检查是否可以选择好友中的收件人")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_copyer_person)
        title = BaseOperate.get_text_list_by_id(self, PhoneControl.id_toolbar_title_tv)
        self.assertEqual(title[0], "人员选择")

        logger.info("查看是否会回显已选择人员")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_contact)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_contact_layout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_name))
        self.assertEqual(BaseOperate.get_text_by_id(self, PhoneControl.id_name), Content.spare_count_realname)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)

        logger.info("检查是否可以进行邮件箱输入")
        ele_list = BaseOperate.get_results_by_class_name(self, PhoneControl.class_name_EditText)
        BaseOperate.send_text_by_ele(self, ele_list[1], "111111111111")
        ele_list = BaseOperate.get_results_by_class_name(self, PhoneControl.class_name_EditText)
        logger.info(BaseOperate.get_text_by_ele(self, ele_list[1]))
        self.assertEqual(BaseOperate.get_text_by_ele(self, ele_list[1]), "111111111111")

        logger.info("查看收件人情况")
        ele_list_1 = BaseOperate.get_text_by_class_name(self, PhoneControl.class_name_EditText)
        ele_list_2 = BaseOperate.get_text_by_class_name(self, PhoneControl.class_name_TextView)
        self.assertTrue(BaseOperate.check_text_in_list(self, ele_list_1, "111111111111"))
        self.assertTrue(BaseOperate.check_text_in_list(self, ele_list_2, Content.spare_count_realname))


 
     
