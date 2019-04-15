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
        u"""搜索出来的app可以点击应用详情页面"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录app")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击应用中心")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_app_center_img)

        logger.info("从后台获取应用名称")
        app_name = BaseOperate.get_info_by_sql(self, "select name from app_entity", "application_center")
        BaseOperate.operate_sql(self,
                                "update application_center.app_entity set run_state='1' where name = '%s'" % app_name,
                                "application_center")
        BaseOperate.sendTextById(self, PhoneControl.search_bar, app_name)
        BaseOperate.touch_search_by_id(self, PhoneControl.search_bar)

        logger.info("判断是否可以进入APP详情界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_business_app_tag1)
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_contact_isv))



    
