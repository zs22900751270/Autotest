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
        BaseOperate.clear_android_local_file(self, folder_name)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)

    def test_step(self):
        u"""云盘搜索结果过多时显示"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("创建多个文件，以便搜索")
        BaseOperate.creat_file_in_android(self, "zhangsen_file1", folder_name)
        BaseOperate.creat_file_in_android(self, "zhangsen_file2", folder_name)

        logger.info("点击首页, 进入云盘, 打开上传界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_homeLayout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_yunpan)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_my_files)

        logger.info("多次上传文件")
        for i in range(12):
            BaseOperate.touch_id_by_index(self, PhoneControl.id_upload_file)
            BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "文件")
            if BaseOperate.checkIfIdExist(self, PhoneControl.id_permission_allow_button):
                BaseOperate.touch_id_by_index(self, PhoneControl.id_permission_allow_button)
                BaseOperate.touch_id_by_index(self, PhoneControl.id_upload_file)
                BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "文件")
            BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, folder_name)
            if i == 0:
                BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "zhangsen_file2")
            else:
                BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "zhangsen_file1")
            BaseOperate.touch_id_by_index(self, PhoneControl.id_btn_addbook)

        logger.info("进行搜索")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_search)
        BaseOperate.sendTextById(self, PhoneControl.id_search_edit, "zhangsen_file")
        BaseOperate.touch_search_by_id(self, PhoneControl.id_search_edit)

        logger.info("判断是否搜索成功")
        BaseOperate.swipe(self, "up", 2)
        name_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_name)
        res_fin = BaseOperate.check_text_in_list(self, name_list, "zhangsen_file2")
        self.assertTrue(res_fin)


 
     
