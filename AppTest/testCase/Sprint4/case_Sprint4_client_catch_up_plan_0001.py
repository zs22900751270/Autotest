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
        u"""完善用户信息界面测试"""
        logger.info("输入账号密码进行登录")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("点击我的资料")
        touch_res = Common.get_result_by_class_name_blank(self, "div", ClassName.avator)
        Common.touch_by_element(self, touch_res)
        me_result = Common.get_result_by_id(self, ID.panelMenu)
        Common.touch_tag_name_by_element(self, me_result, "li", 4)

        logger.info("修改我的资料,清空必选项，然后点击保存")
        Common.clear_text_by_class_name_and_placeholder(self, ClassName.ivu_input, "请输入邮箱地址")
        err_result = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip)
        self.assertTrue("请填写邮箱地址" in err_result)


