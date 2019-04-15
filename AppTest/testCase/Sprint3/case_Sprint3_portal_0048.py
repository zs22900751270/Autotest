#!/usr/bin/env python
# _*_coding:utf-8_*_


from AppTest.Common import *


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControlServer.web_url)

    @classmethod
    def tearDown(self):
        Common.report_screen_shot(self, self.case_name)
        Common.quit(self)

    def test_step(self):
        u"""ISV信息完成页面企业邮箱框输入错误的邮箱格式时，无法保存成功"""
        logger.info("web端登录")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("判断是否登陆成功")
        get_login_result = Common.check_if_class_name_exist(self, ClassName.ivu_icon_log_out, "i")
        self.assertTrue(get_login_result)

        logger.info("点击应用管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "应用管理", "li")

        logger.info("点击isv字典管理")
        if Common.get_display_status_by_text(self, "ISV管理"):
            Common.touch_text_by_class_name(self, ClassName.ivu_menu_submenu_title, "ISV管理", "div")
            Common.touch_text_by_class_name(self, ClassName.layout_text, "ISV管理", "span")

        logger.info("点击添加ISV")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "添加ISV", "button")

        logger.info("上传图片")
        Common.upload_file(self, ClassName.ivu_upload_input, "icon", "icon.jpg")

        logger.info("输入ISV服务商名称")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入ISV服务商名称", "isv_name")

        logger.info("输入所属行业")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入企业所属行业", "classify")

        logger.info("选择企业所在地区")
        Common.select_area_by_text(self, "企业所在地区")

        logger.info("上传主页banner")
        Common.upload_file(self, ClassName.ivu_upload_input, "banner", "banner.jpg", 2)

        logger.info("输入企业服务电话")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入企业服务电话", "000-0000000")

        logger.info("请输入企业邮箱")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入企业邮箱", u"11111111")

        logger.info("请输入传真")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入传真", "000-00000000")

        logger.info("请输入企业地址")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入企业地址", u"企业地址")

        logger.info("请输入企业法人")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入企业法人", u"企业法人")

        logger.info("请输入企业性质")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入企业性质", "IT")

        logger.info("请输入注册资金")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入注册资金", "666")

        logger.info("请选择成立日期")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请选择成立日期", "2018-10-01")

        logger.info("请输入社会信用代码")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入社会信用代码", "aaaaaaaaa")

        logger.info("选择企业地区")
        Common.select_area_by_text(self, "企业注册地址")

        logger.info("请输入企业经营范围")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入企业经营范围", "ssssssssssssss")

        logger.info("点击保存")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "保存", "button")

        logger.info("判断是否出现错误提示")
        get_phone_error = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip, "div")
        self.assertTrue("请输入正确的邮箱地址(xxx@xxx.xxx)" in get_phone_error)



     
