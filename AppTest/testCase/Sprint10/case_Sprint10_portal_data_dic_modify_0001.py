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
        Common.quit(self)

    def test_step(self):
        u"""数据字典标准数据字典页面修改增加ID"""
        logger.info("打开客户端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("进入我的界面")
        me_ele = Common.get_result_by_class_name(self, ClassName.avator)
        Common.touch_by_element(self, me_ele)
        id_result = Common.get_result_by_id(self, ID.panelMenu)
        Common.touch_tag_name_by_element(self, id_result, "li", 4)

        logger.info("进入修改手机号界面")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "修改验证手机号", "li")

        logger.info("检测是否进入修改手机号界面")
        tit_text = Common.get_text_by_class_name(self, ClassName.title)
        self.assertTrue(Common.check_text_in_list(self, tit_text, "修改验证手机号"))

        logger.info("点击替换，输入错误的手机号")
        Common.touch_text_by_class_name(self, ClassName.toright, "替换")
        input_list = Common.get_results_by_class_name_blank(self, "input", ClassName.ivu_input)
        Common.send_text_by_element(self, input_list[-2], "19899999999")

        logger.info("点击获取验证码")
        Common.touch_by_id(self, ID.getPhoneFormCodeBtn)
        identify_code = Common.get_identifying_code(self, "19899999999")
        Common.send_text_by_element(self, input_list[-1], identify_code)
        Common.touch_by_id(self, ID.changePhoneBtn)

        logger.info("使用新账号进行登录")
        Common.open_new_page_in_chrome(self, WebControl.web_url)
        Common.login_web_client(self, "19899999999", Content.login_password)

        logger.info("判断是否登陆成功")
        self.assertTrue(Common.check_if_id_exist(self, ID.userInfo))

        logger.info("恢复手机号")
        me_ele = Common.get_result_by_class_name(self, ClassName.avator)
        Common.touch_by_element(self, me_ele)
        id_result = Common.get_result_by_id(self, ID.panelMenu)
        Common.touch_tag_name_by_element(self, id_result, "li", 4)

        logger.info("进入修改手机号界面")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "修改验证手机号", "li")

        logger.info("检测是否进入修改手机号界面")
        tit_text = Common.get_text_by_class_name(self, ClassName.title)
        self.assertTrue(Common.check_text_in_list(self, tit_text, "修改验证手机号"))

        logger.info("点击替换，输入错误的手机号")
        Common.touch_text_by_class_name(self, ClassName.toright, "替换")
        input_list = Common.get_results_by_class_name_blank(self, "input", ClassName.ivu_input)
        Common.send_text_by_element(self, input_list[-2], Content.register_count)

        logger.info("点击获取验证码")
        Common.touch_by_id(self, ID.getPhoneFormCodeBtn)
        identify_code = Common.get_identifying_code(self, Content.register_count)
        Common.send_text_by_element(self, input_list[-1], identify_code)
        Common.touch_by_id(self, ID.changePhoneBtn)
        logger.info("查看是否操作成功")
        tip_test = Common.get_text_by_class_name(self, ClassName.ivu_modal_confirm_head_title, "div")
        self.assertTrue(Common.check_text_in_list(self, tip_test, "操作成功"))

