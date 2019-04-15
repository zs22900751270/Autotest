#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *

no_register_count = Content.no_register_count
phoneNum = Content.register_count
password = Content.login_password


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
        u"""中文或者英文前面，中间，后面加空格，一到三个空格。"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)
        BaseOperate.wait(self, 5)

        logger.info("登录app")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击应用中心")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_app_center_img)

        logger.info("从后台获取应用名称")
        app_name = BaseOperate.get_info_by_sql(self, "select name from app_entity", "application_center")

        logger.info("点击进行搜索")
        BaseOperate.sendTextById(self, PhoneControl.search_bar, app_name[:-2]+" "+app_name[-1:])
        BaseOperate.touch_search_by_id(self, PhoneControl.search_bar)

        logger.info("判断是否能搜索成功")
        get_toast_result = BaseOperate.find_toast(self, "未搜索到相关应用")
        self.assertTrue(get_toast_result)



    
