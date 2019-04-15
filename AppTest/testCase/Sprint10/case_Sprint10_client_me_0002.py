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

    def check_Tips(self):
        i = 0
        global tip_res
        tip_res = False
        while i <= 5:
            error_list = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip, "div")
            if Common.check_text_in_list(self, error_list, "验证码输入错误"):
                logger.info("提示正常显示")
                tip_res = True
                break
            logger.info("验证码提示检测中，请等待")
            Common.wait(self, 1)
            i += 1

    def test_step(self):
        u"""修改密码界面输入错误的验证码"""
        logger.info("打开客户端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("进入我的界面")
        me_ele = Common.get_result_by_class_name(self, ClassName.avator)
        Common.touch_by_element(self, me_ele)
        id_result = Common.get_result_by_id(self, ID.panelMenu)
        Common.touch_tag_name_by_element(self, id_result, "li", 4)

        logger.info("进入修改账号密码界面")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "修改账号密码", "li")

        logger.info("点击获取验证码, 输入错误的验证码")
        Common.touch_by_id(self, ID.getCodeFormCodeBtn)
        res_1 = Common.get_result_by_class_name_blank(self, "div", ClassName.checkCodeInp_toleft_ivu_input_wrapper_type)
        input_ele = Common.get_tag_name_by_element(self, res_1, "input")
        Common.send_text_by_element(self, input_ele, "123456")

        logger.info("提示验证码错误")
        td = threading.Thread(target=self.check_Tips, args=())
        td.start()
        Common.touch_by_id(self, ID.codeFormNextBtn)
        self.assertTrue(tip_res)




