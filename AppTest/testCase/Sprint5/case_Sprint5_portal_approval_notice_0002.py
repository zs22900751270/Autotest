#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
classification = "new_sen"
classification_long = "sprint_notice_5_1ssssss"


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControlServer.web_url)

    @classmethod
    def tearDown(self):
        Common.report_screen_shot(self, self.case_name)
        logger.info("收尾工作")
        Common.connect_sql(self, "delete from message_classify where name='%s'" % classification, "scap")
        Common.quit(self)

    def test_step(self):
        u"""通知管理页面点击新建分类"""
        logger.info("输入账号密码进行登录")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击运维管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "运维管理")
        Common.wait(self, 2)

        logger.info("点击创建分类")
        Common.touch_text_by_class_name(self, ClassName.btn_addClass_btn, "新建分类", "button")

        logger.info("判断分类名称长度限制")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入分类名称", classification_long)
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")
        text_list = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip)
        result = Common.check_text_in_list(self, text_list, "长度不能超过10字符")
        self.assertTrue(result)

        logger.info("创建分类")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入分类名称", classification)
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")

        logger.info("创建相同的分类")
        Common.touch_text_by_class_name(self, ClassName.btn_addClass_btn, "新建分类", "button")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入分类名称", classification)
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")

        logger.info("判断是否能创建相同的分类")
        text_exist = Common.get_text_by_class_name(self, ClassName.sweet_alert_showsweetalert_visible, "div")[0]
        logger.info(text_exist)
        self.assertTrue("分类名称不能重复" in text_exist)



    
