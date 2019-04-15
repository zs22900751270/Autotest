#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        warnings.filterwarnings("ignore")
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControl.web_url)

    @classmethod
    def tearDown(self):
        logger.info("收尾工作")
        Common.report_screen_shot(self, self.case_name)
        Common.clear_opened_app(self, Content.register_count)
        Common.clear_evaluation_by_user(self, Content.register_count)
        Common.quit(self)

    def test_step(self):
        u"""PC端-应用详情评论列表显示昵称验证"""
        logger.info("登录,点击应用市场")
        Common.set_up_nickname_by_user(self, Content.register_count, Content.register_nickname)
        app_name = Common.get_frist_app_name(self)
        Common.login_web_client(self, Content.register_count, Content.login_password)
        Common.touch_by_id(self, ID.toMarket)
        tab_hit = Common.get_result_by_class_name_blank(self, "ul", ClassName.tab_tit)
        Common.touch_tag_name_by_element(self, tab_hit, "li", 2)

        logger.info("点击进入应用详情")
        Common.open_app_detail_by_by_name(self, app_name)
        tab_title = Common.get_result_by_class_name_blank(self, "div", ClassName.tab_title)
        Common.touch_tag_name_by_element(self, tab_title, "span", 3)

        logger.info("点击开通")
        Common.touch_by_id(self, ID.addToMyAppBtn)

        logger.info("查看是否出现应用评论输入框")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请填写应用评论", "titanic_zs")
        Common.touch_by_id(self, ID.submitCommentBtn)

        logger.info("查看评价是否出现")
        self.assertTrue(Common.check_app_evaluation_content_by_user(self, Content.register_count, "titanic_zs"))

        logger.info("修改昵称为空")
        Common.set_up_nickname_by_user(self, Content.register_count, "")
        logger.info("查看是否出现应用评论输入框")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请填写应用评论", "titanic_zs_1")
        Common.touch_by_id(self, ID.submitCommentBtn)

        logger.info("查看评价是否出现")
        self.assertTrue(Common.check_app_evaluation_content_by_user(self, None, "titanic_zs_1"))

