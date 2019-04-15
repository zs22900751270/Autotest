#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *

no_register_count = Content.no_register_count
phoneNum = Content.register_count
password = Content.login_password


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
        u"""应用详情联系服务商"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录app")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击应用中心")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_app_center_img)

        logger.info("从后台获取应用名称")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_item_horizon_imageView)

        logger.info("点击ISV服务商")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_contact_isv)
        get_text = BaseOperate.get_text_by_id(self, PhoneControl.id_btn_selectNegative)
        self.assertEqual(get_text, "取消")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_btn_selectNegative)
        self.assertFalse(BaseOperate.checkIfIdExist(self, PhoneControl.id_btn_selectNegative))



    
