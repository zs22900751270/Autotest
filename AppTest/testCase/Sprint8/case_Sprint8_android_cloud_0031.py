#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
folder_name = ".aaaaaa"


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        warnings.filterwarnings("ignore")
        self.case_name = os.path.basename(__file__)
        self.driver = deviceDriver.mydriver(self)
        BaseOperate.installApp(self, Content.app_name)

    @classmethod
    def tearDown(self):
        BaseOperate.report_screen_shot(self, self.case_name)
        BaseOperate.del_cloud_file_by_user(self, Content.register_count)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)

    def test_step(self):
        u"""上传文件选择手机文件"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击首页, 进入云盘, 打开上传界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_homeLayout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_yunpan)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_my_files)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_upload_file)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "文件")
        if BaseOperate.checkIfIdExist(self, PhoneControl.id_permission_allow_button):
            BaseOperate.touch_id_by_index(self, PhoneControl.id_permission_allow_button)
            BaseOperate.touch_id_by_index(self, PhoneControl.id_upload_file)
            BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "文件")

        logger.info("判断是否调用手机系统目录")
        name_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_tv_path)
        self.assertTrue(BaseOperate.check_text_in_list(self, name_list, "/storage/emulated/0"))


 
     
