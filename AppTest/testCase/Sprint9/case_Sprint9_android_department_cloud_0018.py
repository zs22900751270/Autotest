#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
folder_name = ".aaaaaa"
file_name = "zhangsen_1K"
new_file_name = "1K_zs"
my_folder_name = "zs_test"


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
        BaseOperate.clear_android_local_file(self, folder_name)
        BaseOperate.del_dept_cloud_file_by_user_and_file(self, Content.register_count, my_folder_name)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)

    def test_step(self):
        u"""安卓-部门云盘-部门云盘角色权限控制-部门员工-自己所属文件文件夹…下可操作按钮验证"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("创建一个大小为1K的文件")
        BaseOperate.creat_file_from_window_to_android(self, file_name, folder_name, 1024)

        logger.info("点击首页, 进入云盘")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_homeLayout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_yunpan)

        logger.info("判断是否进入云盘界面")
        text_1 = BaseOperate.get_text_by_id(self, PhoneControl.id_toolbar_title_tv)
        self.assertEqual(text_1, "云盘")

        logger.info("进入云盘节点")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_dept_files)

        logger.info("判断是否进入云盘节点")
        self.assertEqual(BaseOperate.get_text_by_id(self, PhoneControl.id_toolbar_title_tv), "云盘节点")

        logger.info("进入组织云盘")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_title)

        logger.info("判断是否进入组织云盘")
        self.assertEqual(BaseOperate.get_text_by_id(self, PhoneControl.id_toolbar_title_tv), "组织云盘")

        logger.info("创建文件夹")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_new_folder)
        BaseOperate.sendTextById(self, PhoneControl.id_remark, my_folder_name)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)

        logger.info("判断是否创建成功")
        name_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_name)
        self.assertTrue(BaseOperate.check_text_in_list(self, name_list, my_folder_name))

        logger.info("进入文件夹")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, my_folder_name)

        logger.info("上传一个文件")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_upload_file)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "文件")
        if BaseOperate.checkIfIdExist(self, PhoneControl.id_permission_allow_button):
            BaseOperate.touch_id_by_index(self, PhoneControl.id_permission_allow_button)
            BaseOperate.touch_id_by_index(self, PhoneControl.id_upload_file)
            BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "文件")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, folder_name)

        logger.info("选择文件开始上传")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, file_name)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_btn_addbook)

        logger.info("判断是否上传成功")
        name_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_name)
        self.assertTrue(BaseOperate.check_text_in_list(self, name_list, file_name))

        logger.info("重命名文件")
        BaseOperate.touch_more_by_name_in_cloud(self, file_name)
        BaseOperate.touch_text_by_id(self, "重命名", PhoneControl.id_text)
        BaseOperate.sendTextById(self, PhoneControl.id_remark, new_file_name)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)
        logger.info("判断是否修改文件名成功")
        name_list_1 = BaseOperate.get_text_list_by_id(self, PhoneControl.id_name)
        self.assertTrue(BaseOperate.check_text_in_list(self, name_list_1, new_file_name))

        logger.info("下载文件")
        BaseOperate.touch_more_by_name_in_cloud(self, new_file_name)
        BaseOperate.touch_text_by_id(self, "下载", PhoneControl.id_text)
        logger.info("点击进入下载列表，查看是否下载成功,新下载的文件会覆盖源文件")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_btn)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_downloaded_title)
        name_list_2 = BaseOperate.get_text_list_by_id(self, PhoneControl.id_name)
        logger.info(name_list_2)
        self.assertTrue(BaseOperate.check_text_in_list(self, name_list_2, new_file_name))

        logger.info("删除文件")
        BaseOperate.go_back(self)
        BaseOperate.touch_more_by_name_in_cloud(self, new_file_name)
        BaseOperate.touch_text_by_id(self, "删除", PhoneControl.id_text)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_btn_selectPositive)
        logger.info("判断删除是否成功")
        name_list_3 = BaseOperate.get_text_list_by_id(self, PhoneControl.id_name)
        self.assertFalse(BaseOperate.check_text_in_list(self, name_list, name_list_3))


 
     
