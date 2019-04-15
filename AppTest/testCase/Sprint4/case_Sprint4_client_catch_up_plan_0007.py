#!/usr/bin/env python
# _*_coding:utf-8_*_


from AppTest.Common import *


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControl.web_url)

    @classmethod
    def tearDown(self):
        Common.report_screen_shot(self, self.case_name)
        Common.quit(self)

    def test_step(self):
        u"""服务页面常用应用中显示已开通应用"""
        logger.info("输入账号密码进行登录")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("点击应用集合界面")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "应用市场")
        all_ele = Common.get_result_by_class_name_blank(self, "ul", ClassName.tab_tit)
        Common.touch_tag_name_by_element(self, all_ele, "li", 2)

        logger.info("点击行业分类")
        app_card = Common.get_results_by_class_name_blank(self, "div", ClassName.app_card)
        self.assertTrue(len(app_card) > 0)

        logger.info("判断是否进入行业分类界面")
        get_result_list = Common.get_text_by_class_name(self, ClassName.ivu_col_span_2, "div")
        self.assertTrue("行业分类：" in get_result_list)



    
