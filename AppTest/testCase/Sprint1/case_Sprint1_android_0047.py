#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *

phoneNum = Content.register_count
password = Content.login_password
realname = "dsadfajh"


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        self.driver = deviceDriver.mydriver(self)
        BaseOperate.installApp(self, Content.app_name)

    @classmethod
    def tearDown(self):
        BaseOperate.report_screen_shot(self, self.case_name)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)

    def test_step(self):
        u"""正确的真实姓名"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录APP")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("进入修改资料界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_me_icon)

        logger.info("点击真实姓名")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_true_name)

        logger.info("输入真是姓名")
        BaseOperate.sendTextById(self, PhoneControl.id_infor_modify, realname)

        logger.info("点击保存")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)

        logger.info("点击是否修改成功")
        newname = BaseOperate.get_text_by_id(self, PhoneControl.id_true_name)
        self.assertEqual(newname, realname)



    
