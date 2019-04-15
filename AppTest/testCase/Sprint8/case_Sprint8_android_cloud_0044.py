#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
folder_name = ".aaaaaa"
file_name_txt = "zhangsen.txt"


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
        BaseOperate.clear_android_local_file(self, folder_name)
        BaseOperate.clear_window_local_file(self)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)

    def test_step(self):
        u"""文件或文件夹名过长时层级测试"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("创建一个大小为9M的文件")
        BaseOperate.creat_file_in_android(self, file_name_txt, folder_name)

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
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, folder_name)

        logger.info("上传文件")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, file_name_txt)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_btn_addbook)

        logger.info("上传成功")
        name_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_name)
        self.assertTrue(BaseOperate.check_text_in_list(self, name_list, file_name_txt))

        logger.info("修改名称")
        BaseOperate.touch_more_by_name_in_cloud(self, file_name_txt)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "重命名")
        BaseOperate.sendTextById(self, PhoneControl.id_remark, "new_name")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)
        name_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_name)
        self.assertTrue(BaseOperate.check_text_in_list(self, name_list, "new_name.txt"))


 
     
