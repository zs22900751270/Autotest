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
        BaseOperate.clear_opened_app(self, Content.register_count)
        BaseOperate.quit(self)

    def test_step(self):
        u"""搜索，精选，行业分类里面的app可以都可以开通服务行业分类点击已开通，已开通的的app显示正确。首页服务页显示正确"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录app")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击应用中心")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_app_center_img)

        logger.info("从后台获取应用名称")
        app_name = BaseOperate.get_info_by_sql(self, "select name from app_entity", "application_center")
        BaseOperate.sendTextById(self, PhoneControl.search_bar, app_name)

        logger.info("通过坐标点击搜索")
        BaseOperate.touch_search_by_id(self, PhoneControl.search_bar)

        logger.info("点击应用")
        BaseOperate.touchById(self, PhoneControl.id_business_app_tag1)
        BaseOperate.touchById(self, PhoneControl.open_server)
        get_toast = BaseOperate.find_toast(self, "开通成功")
        self.assertTrue(get_toast)



     
