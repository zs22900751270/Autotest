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
        u"""安卓-收件箱-编辑模式"""
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

        logger.info("进入收件箱")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_bottom_my_mail)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_inbox)

        logger.info("点击编辑")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "编辑")
        text_list = BaseOperate.get_text_by_class_name(self, PhoneControl.class_name_TextView)
        self.assertTrue(BaseOperate.check_text_in_list(self, text_list, "全选"))
        self.assertTrue(BaseOperate.check_text_in_list(self, text_list, "取消"))
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_check))
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_cancel_check))
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_delete))


 
     
