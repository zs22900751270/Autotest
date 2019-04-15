#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
classification = "new_sen"
classification_new = "zhangsen"


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
        Common.connect_sql(self, "delete from message_classify where name='%s'" % classification_new, "scap")
        Common.quit(self)

    def test_step(self):
        u"""通知管理页面点击其中一个分类进行重命名"""
        logger.info("输入账号密码进行登录")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击运维管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "运维管理")
        Common.wait(self, 2)

        logger.info("创建分类")
        Common.touch_text_by_class_name(self, ClassName.btn_addClass_btn, "新建分类", "button")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入分类名称", classification)
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")

        logger.info("点击重命名")
        left_ele = Common.get_result_by_class_name_blank(self, "div", ClassName.left)
        new_name = Common.get_class_name_elements_by_element_blank(self, left_ele, "li", ClassName.ivu_menu_item)[-1]
        Common.move_mouse_on(self, new_name)
        Common.wait(self, 3)
        rename1 = Common.get_class_name_elements_by_element_blank(self, left_ele, "div", ClassName.group_edit)[-1]
        rename2 = Common.get_class_name_elements_by_element_blank(self, rename1, "div", ClassName.edit_item)[0]
        logger.info(Common.get_text_by_element(self, rename2))
        Common.touch_by_element(self, rename2)

        logger.info("修改名称")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入分类名称", classification_new)
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")

        logger.info("判断修改成功")
        left_ele = Common.get_result_by_class_name_blank(self, "div", ClassName.left)
        new_name = Common.get_class_name_elements_by_element_blank(self, left_ele, "li", ClassName.ivu_menu_item)[-1]
        text = Common.get_text_by_element(self, new_name)
        self.assertEqual(text, classification_new)



    
