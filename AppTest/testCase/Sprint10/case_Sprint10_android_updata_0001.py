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
        BaseOperate.quit(self)

    def test_step(self):
        u"""安卓-我的消息点击验证"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("查看我的界面中选项是否存在通讯录入口")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_update)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_update)
        cancel = BaseOperate.get_text_list_by_id(self, PhoneControl.id_btn_selectNegative)
        updata = BaseOperate.get_text_list_by_id(self, PhoneControl.id_btn_selectPositive)
        logger.info(cancel)
        logger.info(updata)
        self.assertTrue(BaseOperate.check_text_in_list(self, cancel, "取消"))
        self.assertTrue(BaseOperate.check_text_in_list(self, updata, "下载更新"))

