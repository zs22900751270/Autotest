#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
title = "new_fl"


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
        Common.quit(self)

    def test_step(self):
        u"""通知管理页面点击所有分类下方显示所有分类"""
        logger.info("输入账号密码进行登录")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击运维管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "运维管理")
        Common.wait(self, 2)

        logger.info("点击发布事件")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "发布事件", "button")

        logger.info("点击保存")
        Common.touch_text_by_class_name(self, ClassName.ivu_reload_success, "发送", "button")

        logger.info("获取参数限制信息")
        text_list = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip, "div")
        result = True
        for i in ["请输入标题", "请输入正文", "请选择分类", "请选择类型"]:
            if Common.check_text_in_list(self, text_list, i):
                pass
            else:
                result = False
                break
        self.assertTrue(result)



    
