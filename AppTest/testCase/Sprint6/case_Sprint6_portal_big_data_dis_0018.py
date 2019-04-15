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
        logger.info("清除所下载的文件")
        Common.delete_file_in_window(self, Content.download_path + "大数据可视化.html")
        Common.quit(self)

    def test_step(self):
        u"""导航栏点击服务"""
        logger.info("打开App")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击大数据管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "大数据管理")
        Common.wait(self, 2)

        logger.info("点击大数据展示")
        if Common.get_display_status_by_text(self, "图表设计"):
            Common.touch_text_by_class_name(self, ClassName.layout_text, "大数据展示")
            Common.wait(self, 2)

        logger.info("点击图标设计, 添加组件")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "图表设计")
        Common.wait(self, 2)

        logger.info("点击添加资源框")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "添加资源框", "button")

        logger.info("点击插入组件")
        Common.touch_text_by_class_name(self, ClassName.btn_component, "插入组件", "span")
        Common.wait(self, 5)

        logger.info("输入Url路径")
        url = Common.get_elements_by_placeholder_and_class_name(self, ClassName.ivu_input, "请输入第三方组件Url地址")
        Common.send_text_by_element(self, url[-1], "www.baidu.com")

        logger.info("点击图标设计, 添加图表")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "添加资源框", "button")

        logger.info("点击插入图表")
        Common.touch_text_by_class_name(self, ClassName.btn_chart, "插入图表", "span")

        logger.info("点击保存图表")
        Common.touch_text_by_class_name(self, ClassName.ivu_reload_success, "保存", "button")

        logger.info("判断是否创建图表成功")
        text_list = Common.get_text_by_class_name(self, "span", ClassName.btn_chart)
        result = Common.check_text_in_list(self, text_list, "插入图表")
        self.assertFalse(result)

        logger.info("点击添加资源框，添加文本")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "添加资源框", "button")

        logger.info("点击插入文本")
        Common.touch_text_by_class_name(self, ClassName.btn_text, "插入文本", "span")

        logger.info("输入文本")
        Common.send_text_in_window(self, "xiu_shi_shi_jie")

        logger.info("判断是否创建文本成功")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "图表设计")
        text_list = Common.get_text_by_class_name(self, ClassName.textarea_render, "div")
        result = Common.check_text_in_list(self, text_list, "xiu_shi_shi_jie")
        self.assertTrue(result)

        resource = Common.get_results_by_class_name_blank(self, "div", ClassName.vue_grid_item_resizable)
        self.assertEqual(len(resource), 3)

        logger.info("点击导出")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_warning, "导出", "button")

        logger.info("判断是否导出成功")
        exist = os.path.exists(Content.download_path + "大数据可视化.html")
        self.assertTrue(exist)



    
