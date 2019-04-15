#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
revised_name = "12345678945646554654645"


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        warnings.filterwarnings("ignore")
        self.case_name = os.path.basename(__file__)
        self.driver = deviceDriver.mydriver(self)
        BaseOperate.installApp(self, Content.app_name)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControlServer.web_url)
        global phone_statue
        phone_statue = False

    @classmethod
    def tearDown(self):
        BaseOperate.report_screen_shot(self, self.case_name)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)
        Common.quit(self)

    def phone(self):
        try:
            logger.info("手机端查看用户协议")
            BaseOperate.check_protocol(self, Content.no_register_count)
            BaseOperate.wait(self, 10)
            result = BaseOperate.checkIfTextExist(self, revised_name)
            if result:
                return True
            else:
                return False
        except:
            return False

    def test_step(self):
        u"""用户协议维护修改内容后手机/web端正常显示"""
        # 需要过一段时间操作一次手机，否则会断开
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)
        logger.info("web端登录")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("判断是否登陆成功")
        get_login_info = Common.check_if_class_name_exist(self, ClassName.ivu_icon_log_out, "i")
        self.assertTrue(get_login_info)

        logger.info("修改协议内容")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "运维管理")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "用户协议维护")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu, "用户协议维护")

        edit = Common.get_result_by_class_name_blank(self, "div", ClassName.ql_editor)
        Common.send_text_by_element(self, edit, revised_name)
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "保存", "button")
        Common.wait(self, 5)

        logger.info("点击打开新的web页面,并且打开用户协议进行查看，是否修改成功")
        td = threading.Thread(target=self.phone, args=())
        td.start()
        Common.open_new_page_in_chrome(self, WebControl.web_url)
        logger.info("在新的界面上，点击注册")
        Common.touch_text_by_class_name(self, ClassName.ivu_col_offset_19, "注册账号", "div")
        ele_pro = Common.get_result_by_class_name_blank(self, "label", ClassName.ivu_checkbox_wrapper)
        Common.touch_tag_name_by_element(self, ele_pro, "a")
        Common.wait(self, 20)
        handles = Common.get_window_handle(self)
        Common.switch_window_handle(self, handles[2])

        logger.info("检测用户协议是否修改成功")
        get_text_reslut = Common.get_text_by_class_name(self, ClassName.ql_editor)
        self.assertTrue(revised_name in get_text_reslut)
        self.assertTrue(self.phone())



     
