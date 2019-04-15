#!/usr/bin/env python
# -*- coding:utf-8 -*-

from AppTest.Common.Common import *
from AppTest.Common.Interface import *


class Cloud(object):
    """"""

    def creat_folder(self, folder_name, status=True):
        """"""
        Common.touch_by_id(self, ID.addFolderBtn)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "", folder_name)
        if status:
            ok_btn = Common.get_result_by_class_name_blank(self, "i", ClassName.ivu_icon_checkmark_circled)
            Common.touch_by_element(self, ok_btn)
        else:
            cancel_btn = Common.get_result_by_class_name_blank(self, "i", ClassName.ivu_icon_close_circled)
            Common.touch_by_element(self, cancel_btn)
        Common.wait(self, 5)

    def open_folder_by_name(self, folder_name):
        """"""
        Common.touch_text_by_class_name(self, ClassName.rowName, folder_name, "span")

    def check_if_file_exist(self, file_name):
        """"""
        name_list = Common.get_text_by_class_name(self, ClassName.rowName, "span")
        return Common.check_text_in_list(self, name_list, file_name)

    def get_upload_time_by_file_name(self, file_name):
        """"""
        name_list_1 = Common.get_results_by_class_name(self, ClassName.ivu_table_row)
        for i in name_list_1:
            if file_name in i.text:
                u_l = Common.get_class_name_elements_by_element(self, i, ClassName.ivu_table_cell)[2]
                return u_l.text

    def get_upload_size_by_file_name(self, file_name):
        """"""
        name_list_1 = Common.get_results_by_class_name(self, ClassName.ivu_table_row)
        for i in name_list_1:
            if file_name in i.text:
                f_s = Common.get_class_name_elements_by_element(self, i, ClassName.ivu_table_cell)[3]
                return f_s.text

    def upload_file(self, file_name, size=1024000, t=5):
        """"""
        if not os.path.exists(project_path + "/resource/cloud_upload_file"):
            os.mkdir(project_path + "/resource/cloud_upload_file")
        upload_file_path = project_path + "/resource/cloud_upload_file/" + file_name
        os.system("fsutil file createnew %s %s" % (upload_file_path, size))
        upload_btn = Common.get_result_by_class_name(self, ClassName.ivu_upload_input)
        upload_btn.send_keys(upload_file_path)
        Common.wait(self, t)

    def get_cloud_use_status_by_phone(self, phone_num):
        """"""
        row_list = Common.get_results_by_class_name(self, ClassName.ivu_table_row)
        for row in row_list:
            p_num = Common.get_tag_name_by_element(self, row, "span", 2)
            btn_con = Common.get_tag_name_by_element(self, row, "span", 6)
            btn_text = Common.get_text_by_element(self, btn_con)
            logger.info(Common.get_text_by_element(self, p_num))
            logger.info(btn_text)
            if Common.get_text_by_element(self, p_num) == phone_num:
                if btn_text == "停用":
                    logger.info("用户%s的云盘已启用" % phone_num)
                    return True, row
                elif btn_text == "启用":
                    logger.info("用户%s的云盘已停用" % phone_num)
                    return False, row
                else:
                    logger.info("%s的数据不正确" % phone_num)

    def open_or_close_cloud_by_phone(self, phone_num, type=True):
        """"""
        use_status, btn_ele = Cloud.get_cloud_use_status_by_phone(self, phone_num)
        logger.info(use_status)
        logger.info(type)
        if type and not use_status:
            Common.touch_tag_name_by_element(self, btn_ele, "button")
        elif not type and use_status:
            Common.touch_tag_name_by_element(self, btn_ele, "button")
            Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")
        else:
            logger.info("该状态以满足")

    def modify_cloud_enable_status_by_user(self, phone_num, enable=True):
        """"""
        id = Common.get_info_by_sql(self, "SELECT id FROM user WHERE phone='%s'" % phone_num, "scap")
        if enable: status = "1"
        else: status = "0"
        sql = "UPDATE scap.mail_account SET ENABLE='%s' WHERE user_id='%s'" % (status, id)
        Common.connect_sql(self, sql, "scap")

    def del_cloud_file_by_user(self, count_phone):
        """"""
        id = Common.get_info_by_sql(self, "SELECT id FROM user WHERE phone='%s'" % count_phone, "scap")
        Common.connect_sql(self, "DELETE FROM scap.disk_user_file WHERE user_id='%s'" % id, "scap")
        Common.connect_sql(self, "UPDATE scap.`disk_user_manage` SET used_size ='0' WHERE user_id='%s'" % id, "scap")

    def clear_cloud_local_file(self):
        """"""
        file_name_list = os.listdir(project_path + "/resource/cloud_upload_file")
        for i in file_name_list:
            os.remove(project_path + "/resource/cloud_upload_file/"+i)

