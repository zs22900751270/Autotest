#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
folder_name = ".aaaaaa"
file_name = "zhangsen_1K"
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
        BaseOperate.del_dept_cloud_file_by_user_and_file(self, Content.register_count, file_name)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)

    def test_step(self):
        u"""安卓-部门云盘-云盘页面显示"""
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

        logger.info("查看路径是否存在")
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_path))
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_path_blue))

        logger.info("查看该界面是否有搜索框")
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_search))

        logger.info("查看文件的创建信息是否齐全")
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_creator_name))
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_size))
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_date))

        logger.info("查看界面底部，创建文件夹与上传文件是否存在")
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_new_folder))
        self.assertTrue(BaseOperate.checkIfIdExist(self, PhoneControl.id_upload_file))

        logger.info("创建文件夹")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_new_folder)
        BaseOperate.sendTextById(self, PhoneControl.id_remark, my_folder_name)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)

        logger.info("查看文件夹的操作方式")
        BaseOperate.touch_more_by_name_in_cloud(self, my_folder_name)
        option_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_text)
        self.assertTrue(BaseOperate.check_text_in_list(self, option_list, "重命名"))
        self.assertTrue(BaseOperate.check_text_in_list(self, option_list, "删除"))
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "取消")

        logger.info("查看上传的文件可进行的操作")
        BaseOperate.touch_more_by_name_in_cloud(self, file_name)
        option_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_text)
        self.assertTrue(BaseOperate.check_text_in_list(self, option_list, "下载"))
        self.assertTrue(BaseOperate.check_text_in_list(self, option_list, "重命名"))
        self.assertTrue(BaseOperate.check_text_in_list(self, option_list, "删除"))


 
     
