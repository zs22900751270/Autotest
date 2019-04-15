#!/usr/bin/env python
# -*- coding:utf-8 -*-

from AppTest.Common.Common import *
from AppTest.Common.BaseOperate import *


class Mail(object):
    """"""

    def send_mail(self, phone_num=None, copyer=None, mail_theme="mail_theme", file_type=None, file_name=None, size=100):
        Common.touch_text_by_class_name(self, ClassName.item, "写信")
        if phone_num is not None:
            add_res = Common.get_results_by_class_name_blank(self, "i", ClassName.btn_add_icon_lius_circled)[0]
            Common.touch_by_element(self, add_res)
            realname = Common.get_realname_by_phone(self, phone_num)
            name_list = Common.get_results_by_class_name_blank(self, "label", ClassName.ivu_checkbox_wrapper_group_item)
            Common.touch_text_by_elements(self, name_list, realname)
            Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")
            Common.wait(self, 2)
        if copyer is not None:
            add_res = Common.get_results_by_class_name_blank(self, "i", ClassName.btn_add_icon_lius_circled)[1]
            Common.touch_by_element(self, add_res)
            realname = Common.get_realname_by_phone(self, copyer)
            name_list = Common.get_results_by_class_name_blank(self, "label", ClassName.ivu_checkbox_wrapper_group_item)
            Common.touch_text_by_elements(self, name_list, realname)
            Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")
            Common.wait(self, 2)
        if mail_theme is not None:
            Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "", mail_theme)
            Common.wait(self, 2)
        if file_type is not None:
            Mail.add_mail_file(self, file_type, file_name, size)
        Common.wait(self, 3)
        Common.touch_by_id(self, ID.sendMailBtn, 5)

    def get_mail_use_status_by_phone(self, phone_num):
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
                    logger.info("用户%s的邮箱已启用" % phone_num)
                    return True, row
                elif btn_text == "启用":
                    logger.info("用户%s的邮箱已停用" % phone_num)
                    return False, row
                else:
                    logger.info("%s的数据不正确" % phone_num)

    def open_or_close_mail_by_phone(self, phone_num, type=True):
        """"""
        use_status, btn_ele = Mail.get_mail_use_status_by_phone(self, phone_num)
        logger.info(use_status)
        logger.info(type)
        if type and not use_status:
            Common.touch_tag_name_by_element(self, btn_ele, "button")
        elif not type and use_status:
            Common.touch_tag_name_by_element(self, btn_ele, "button")
            Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")
        else:
            logger.info("该状态以满足")

    def modify_mail_enable_status_by_user(self, phone_num, enable=True):
        """"""
        id = Common.get_info_by_sql(self, "SELECT id FROM user WHERE phone='%s'" % phone_num, "scap")
        if enable: status = "1"
        else: status = "0"
        sql = "UPDATE scap.mail_account SET ENABLE='%s' WHERE user_id='%s'" % (status, id)
        Common.connect_sql(self, sql, "scap")

    def add_mail_file(self, file_type, file_name, size=100):
        """"""
        path_list = {"icon": "\\resource\\Img\\icon\\",
                     "isv": "\\resource\\File\\isv\\",
                     "banner": "\\resource\\Img\\banner\\",
                     "html": "\\resource\\File\\html\\",
                     "create": "\\resource\\File\\create\\"}
        file_path = project_path + path_list[file_type]+file_name
        if file_type == "create":
            if not os.path.exists(project_path+path_list["create"]):
                os.mkdir(project_path+path_list["create"])
            os.system("fsutil file createnew %s %s" % (project_path+path_list["create"]+file_name, size))
            file_path = project_path+path_list["create"]+file_name
        upload_file = Common.get_result_by_class_name(self, ClassName.ivu_upload_input)
        upload_file.send_keys(file_path)

    def creat_mail_draft(self, phone_num=None, copyer=None, mail_theme="mail_theme"):
        """"""
        Common.touch_text_by_class_name(self, ClassName.item, "写信")
        if phone_num is not None:
            add_res = Common.get_results_by_class_name_blank(self, "i", ClassName.btn_add_icon_lius_circled)[0]
            Common.touch_by_element(self, add_res)
            realname = Common.get_realname_by_phone(self, phone_num)
            name_list = Common.get_results_by_class_name_blank(self, "label", ClassName.ivu_checkbox_wrapper_group_item)
            Common.touch_text_by_elements(self, name_list, realname)
            Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")
            Common.wait(self, 2)
        if copyer is not None:
            Common.send_text_by_id(self, ID.cc, copyer)
            Common.wait(self, 2)
        if mail_theme is not None:
            Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "", mail_theme)
            Common.wait(self, 2)
        Common.touch_by_id(self, ID.saveMailBtn)
        Common.wait(self, 3)

    def del_mail_record_by_user(self, phone_num):
        """"""
        id = Common.get_info_by_sql(self, "SELECT id FROM user WHERE phone='%s'" % phone_num, "scap")
        sql = "DELETE FROM scap.mail_entity WHERE user_id = '%s'" % id
        Common.connect_sql(self, sql, "scap")

    def sign_star_by_theme(self, mail_theme):
        ele = Common.get_results_by_class_name_blank(self, "span", ClassName.td_content_sp)[1::2]
        star_ele = Common.get_results_by_class_name_blank(self, "td", ClassName.center_star)
        for i in range(len(ele)):
            if mail_theme in Common.get_text_by_element(self, ele[i]):
                Common.touch_by_element(self, star_ele[i])
                break

    def check_star_status_by_theme(self, mail_theme, status=True):
        ele = Common.get_results_by_class_name_blank(self, "span", ClassName.td_content_sp)[1::2]
        star_ele = Common.get_results_by_class_name_blank(self, "td", ClassName.center_star)
        for i in range(len(ele)):
            if mail_theme in Common.get_text_by_element(self, ele[i]):
                star_status_1 = Common.get_class_name_elements_by_element_blank(self, star_ele[i], "i",
                                                                                ClassName.ivu_icon_ios_star_outline)
                star_status_2 = Common.get_class_name_elements_by_element_blank(self, star_ele[i], "i",
                                                                                ClassName.ivu_icon_ios_star)
                if len(star_status_1) > 0 and len(star_status_2) == 0 and status is False:
                    logger.info("%s未标星")
                    return False
                if len(star_status_1) == 0 and len(star_status_2) > 0 and status is True:
                    logger.info("%s以标星")
                    return True

    def touch_delete_or_transmit_by_theme(self, mail_theme, opt_type="delete"):
        ele = Common.get_results_by_class_name_blank(self, "span", ClassName.td_content_sp)[1::2]
        opt_list = Common.get_results_by_class_name_blank(self, "td", ClassName.opt_center)
        for i in range(len(ele)):
            if mail_theme in Common.get_text_by_element(self, ele[i]):
                if opt_type == "delete":
                    Common.touch_tag_name_by_element(self, opt_list[i], "a", 1)
                    Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")
                    break
                elif opt_type == "transmit":
                    Common.touch_tag_name_by_element(self, opt_list[i], "a", 2)
                    break
                elif opt_type == "recover":
                    Common.touch_tag_name_by_element(self, opt_list[i], "a", 2)
                    break
                else:
                    logger.info("参数输入错误")
                    break

    def modify_read_state_by_sql(self, phone_num, theme, state="read"):
        """"""
        if state == "read":
            state_code = "4"
        elif state == "not_read":
            state_code = "3"
        id = Common.get_info_by_sql(self, "SELECT id FROM user WHERE phone='%s'" % phone_num, "scap")
        sql = "UPDATE scap.`mail_entity` SET state='%s' WHERE user_id='%s' AND theme='%s'" % (state_code, id, theme)
        Common.connect_sql(self, sql, "scap")

    def touch_detail_by_theme(self, mail_theme):
        """"""
        Common.wait(self, 5)
        name_list = Common.get_results_by_class_name_blank(self, "span", ClassName.td_content_sp)[1::2]
        for i in name_list:
            theme_name = i.text
            name = theme_name.split(" ")[-1]
            if mail_theme == name:
                Common.touch_by_element(self, i)
                break

    def check_down_file_sucess(self, filename):
        """"""
        file_list = os.listdir(Content.download_path)
        if Common.check_text_in_list(self, file_list, filename):
            logger.info("文件下载成功")
            Common.delete_file_in_window(self, Content.download_path+"/"+filename)
            return True
        else:
            logger.info("文件下载失败")
            return False


class Mail_phone(object):

    def send_mail(self, receiver, theme=None, copyer=None, mail_content=None, file_name=None, folder_name=None):
        """"""
        BaseOperate.touch_id_by_index(self, PhoneControl.id_new_mail)
        ele_list = BaseOperate.get_results_by_class_name(self, PhoneControl.class_name_EditText)
        BaseOperate.send_text_by_ele(self, ele_list[0], receiver)
        if copyer is not None:
            BaseOperate.send_text_by_ele(self, ele_list[1], receiver)
        if theme is not None:
            BaseOperate.sendTextById(self, PhoneControl.id_theme, theme)
        if mail_content is not None:
            BaseOperate.sendTextById(self, PhoneControl.id_content, mail_content)
        if file_name is not None:
            BaseOperate.touch_id_by_index(self, PhoneControl.id_file)
            BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "文件")
            if BaseOperate.checkIfIdExist(self, PhoneControl.id_permission_allow_button):
                BaseOperate.touch_id_by_index(self, PhoneControl.id_permission_allow_button)
                BaseOperate.touch_id_by_index(self, PhoneControl.id_file)
                BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "文件")
            BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, folder_name)
            BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, file_name)
            BaseOperate.touch_id_by_index(self, PhoneControl.id_btn_addbook)
            Mail_phone.check_upload_file_in_mail(self, file_name)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)
        if theme is None:
            BaseOperate.touch_id_by_index(self, PhoneControl.id_btn_selectPositive)
        BaseOperate.wait(self, 5)

    def check_mail_if_exist_by_theme(self, theme):
        """"""
        refre_time = 0
        while refre_time < 120:
            theme_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_theme)
            if theme in theme_list:
                logger.info("邮件接收成功")
                return True
            else:
                logger.info("网络有延迟，邮件接收需要时间，请等待。。。")
                BaseOperate.touch_id_by_index(self, PhoneControl.id_bottom_inbox)
                refre_time += 3
                BaseOperate.wait(self, 3)
        logger.info("超过两分钟未接收到邮件")
        return False

    def check_mail_if_exist_by_sender(self, phone_nume):
        """"""
        real_name = BaseOperate.get_realname_by_phone(self, phone_nume)
        refre_time = 0
        while refre_time < 120:
            send_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_send_account)
            if real_name in send_list:
                logger.info("邮件接收成功")
                return True
            else:
                logger.info("网络有延迟，邮件接收需要时间，请等待。。。")
                BaseOperate.touch_id_by_index(self, PhoneControl.id_bottom_inbox)
                refre_time += 3
                BaseOperate.wait(self, 3)
        logger.info("超过两分钟未接收到邮件")
        return False

    def check_upload_file_in_mail(self, file_name):
        """"""
        timeout = 0
        while timeout < 50:
            file_name_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_name)
            if BaseOperate.check_text_in_list(self, file_name_list, file_name):
                logger.info("上传成功")
                return True
            logger.info("上传中，请稍等。。。")
            BaseOperate.wait(self, 1)
            timeout += 1
            return False

    def del_upload_file_in_mail_by_filename(self, filename):
        """"""
        file_name_list = BaseOperate.get_results_by_id(self, PhoneControl.id_name)
        del_btn_list = BaseOperate.get_results_by_id(self, PhoneControl.id_oper)
        for i in file_name_list:
            if i.text == filename:
                ele_num = file_name_list.index(i)
                BaseOperate.touch_by_element(self, del_btn_list[ele_num])
                break

    def creat_draft(self, receiver, theme=None, copyer=None, mail_content=None, file_name=None, folder_name=None):
        BaseOperate.touch_id_by_index(self, PhoneControl.id_new_mail)
        ele_list = BaseOperate.get_results_by_class_name(self, PhoneControl.class_name_EditText)
        BaseOperate.send_text_by_ele(self, ele_list[0], receiver)
        if copyer is not None:
            BaseOperate.send_text_by_ele(self, ele_list[1], receiver)
        if theme is not None:
            BaseOperate.sendTextById(self, PhoneControl.id_theme, theme)
        if mail_content is not None:
            BaseOperate.sendTextById(self, PhoneControl.id_content, mail_content)
        if file_name is not None:
            BaseOperate.touch_id_by_index(self, PhoneControl.id_file)
            BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "文件")
            if BaseOperate.checkIfIdExist(self, PhoneControl.id_permission_allow_button):
                BaseOperate.touch_id_by_index(self, PhoneControl.id_permission_allow_button)
                BaseOperate.touch_id_by_index(self, PhoneControl.id_file)
                BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "文件")
            BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, folder_name)
            BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, file_name)
            BaseOperate.touch_id_by_index(self, PhoneControl.id_btn_addbook)
            Mail_phone.check_upload_file_in_mail(self, file_name)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_left_btn)
        BaseOperate.touch_text_by_id(self, "保存草稿", PhoneControl.id_text)

    def creat_dustbin_from_other_place(self, place, *args):
        """"""
        if place == "草稿箱":
            BaseOperate.touch_id_by_index(self, PhoneControl.id_drafts)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)
        for theme_name in args:
            BaseOperate.touch_text_by_id(self, theme_name, PhoneControl.id_theme)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_delete)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_btn_selectPositive)
        BaseOperate.go_back(self)

    def recover_mail_from_dustbin_by_theme(self, theme_name):
        """"""
        BaseOperate.touch_text_by_id(self, theme_name, PhoneControl.id_theme)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_redo)

