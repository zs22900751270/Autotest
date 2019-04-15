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
        BaseOperate.clear_group_by_user(self, Content.register_count)
        BaseOperate.quit(self)

    def test_step(self):
        u"""分组名不能以空格开头或结尾"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录APP，进入主界面")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("进入首页")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_homeLayout)

        logger.info("进入通讯录界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_btn)

        logger.info("点击分组联系人")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_group)

        logger.info("判断是否进入分组联系人界面")
        text = BaseOperate.get_text_by_id(self, PhoneControl.id_toolbar_title_tv)
        self.assertEqual(text, "分组联系人")

        logger.info("创建分组联系人")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)

        logger.info("输入分组名称")
        BaseOperate.sendTextById(self, PhoneControl.id_group_name, "  name  ")
        
        logger.info("选择成员")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_contact_layout)

        logger.info("点击保存")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_save)

        logger.info("判断分组名是否可以空格开头结尾")
        gr_name = BaseOperate.get_text_by_id(self, PhoneControl.id_group_name)
        self.assertNotEqual(gr_name[:1], " ")
        self.assertNotEqual(gr_name[-1:], " ")


 
    
