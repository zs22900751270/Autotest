#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Content:
    # 已注册账号
    register_count = "18888880018"
    login_password = "zs123456"
    register_mail_address = "zhangsen@sxlehua.club"
    register_realname = "zhangsen"
    register_nickname = "nicknamesen"
    # 未注册账号
    no_register_count = "15594819121"
    # 备用账号
    spare_count = "18888880017"
    spare_password = "qwe123"
    spare_count_realname = "aaazs"
    spare_mail_address = "18888880017@yx.cnhqd.net"
    spare_count1 = "18709212578"
    spare_password1 = "qwe123"
    # 需要安装的app名
    app_name = "HQD.apk"
    # 应用中心-添加分类-分类图标位置
    app_add_classifiacation_icon = "/appcenter/image/app/3.png"
    # 默认下载路径
    download_path = "C:/Users/sangfor/Downloads/"
    # 默认文件创建路径
    create_file = "/resource/File/create/"
    # 安卓云盘默认路径
    cloud_path = "/storage/emulated/0/"


class PhoneControl:
    # 包名
    package_name = "com.hqd.app_manager"
    # 活动名
    activity_name = "com.hqd.app_manager.feature.SplashActivity"
    SettingActivity = "com.hqd.app_manager.feature.SettingActivity"
    # 登录界面账号框ID
    login_count = "com.hqd.app_manager:id/login_tel_num"
    # 登录界面密码框ID
    login_password = "com.hqd.app_manager:id/login_password_num"
    # 登录界面登录按钮ID
    login_login_button = "com.hqd.app_manager:id/next_btn"

    # 我的界面-点击登录或注册
    login_or_register = "com.hqd.app_manager:id/login_hint"
    # 登录界面-注册按钮
    register_button = "com.hqd.app_manager:id/go_register"
    # 注册界面-手机号码框
    register_phone_num = "com.hqd.app_manager:id/tel_num"
    # 注册界面-获取验证码按钮
    register_verify_button = "com.hqd.app_manager:id/verify_code_btn"
    # 注册界面-输入获取的验证码
    register_verify_input = "com.hqd.app_manager:id/verify_code_edit"
    # 注册界面-点击下一步
    register_next_button = "com.hqd.app_manager:id/next_btn"
    # 注册界面-输入密码
    register_input_password = "com.hqd.app_manager:id/password_tel_num"
    # 注册界面-确认密码
    register_input_password_again = "com.hqd.app_manager:id/password_verify_code_edit"

    # 登录界面-忘记密码入口
    login_forget_password = "com.hqd.app_manager:id/login_forget_password"
    # 忘记密码界面-手机号输入框
    forget_count = "com.hqd.app_manager:id/tel_num"
    # 忘记密码界面-获取验证码
    forget_verify_button = "com.hqd.app_manager:id/verify_code_btn"
    # 忘记密码界面-输入验证码
    forget_verify_input = "com.hqd.app_manager:id/verify_code_edit"
    # 忘记密码界面-下一步
    forget_next_button = "com.hqd.app_manager:id/next_btn"
    # 忘记密码界面-输入新密码
    forget_input_password = "com.hqd.app_manager:id/password_tel_num"
    # 忘记密码界面-确认密码
    forget_input_password_again = "com.hqd.app_manager:id/password_verify_code_edit"
    # 忘记密码界面-输入密码后-点击确定
    forget_input_password_next_button = "com.hqd.app_manager:id/password_next_btn"

    # 我的界面-我的资料入口
    id_me_icon = "com.hqd.app_manager:id/me_icon"
    # 我的资料界面-真实姓名
    id_true_name = "com.hqd.app_manager:id/true_name"
    # 我的资料界面-真实姓名-输入真实姓名
    id_infor_modify = "com.hqd.app_manager:id/infor_modify"
    # 我的资料界面-昵称
    id_nick_name = "com.hqd.app_manager:id/nick_name"
    # 我的资料界面-性别选择-男
    my_data_user_sex_m = "com.hqd.app_manager:id/btn1"
    # 我的资料界面-性别选择-女
    my_data_user_sex_f = "com.hqd.app_manager:id/btn2"
    # 我的资料界面-性别选择-取消
    my_data_user_sex_cancel = "com.hqd.app_manager:id/btn_cancel"
    # 我的资料界面-生日
    my_data_birthday = "com.hqd.app_manager:id/birthday_"
    # 设置生日界面-取消
    my_data_birthday_cancel = "com.hqd.app_manager:id/btnCancel"

    # 我的资料界面-邮箱-输入邮箱
    me_data_mail_input = "com.hqd.app_manager:id/infor_modify"
    # 我的资料界面-地址
    my_data_place = "com.hqd.app_manager:id/place"
    # 我的资料界面-地址-输入地址
    my_data_place_input = "com.hqd.app_manager:id/infor_modify"
    # 我的资料界面-授权开关
    my_data_authorization_switch_button = "com.hqd.app_manager:id/auto_author_switch"

    # 应用中心ID
    id_app_center_img = "com.hqd.app_manager:id/app_center_img"
    # 联系服务商ID
    id_contact_isv = "com.hqd.app_manager:id/contact_isv"
    # 联系服务商-取消ID
    id_dialog_neg_btn = "com.hqd.app_manager:id/btn_selectNegative"
    # 应用中心界面-搜索框
    search_bar = "com.hqd.app_manager:id/search_bar"
    # 验证码框ID

    # 开通应用按钮ID
    open_server = "com.hqd.app_manager:id/open_up_tv"
    class_name_EditText = "android.widget.EditText"
    class_name_TextView = "android.widget.TextView"
    id_password_warning_tv = "com.hqd.app_manager:id/password_warning_tv"
    id_notify_list = "com.hqd.app_manager:id/notify_list"
    id_empty_msg_layout = "com.hqd.app_manager:id/empty_msg_layout"
    id_shenpi = "com.hqd.app_manager:id/shenpi"
    id_verify_code_iv = "com.hqd.app_manager:id/verify_code_iv"
    id_app_center_img = "com.hqd.app_manager:id/app_center_img"
    id_feedback = "com.hqd.app_manager:id/feedback"
    id_shezhi = "com.hqd.app_manager:id/shezhi"
    id_guanyuwomen = "com.hqd.app_manager:id/guanyuwomen"
    id_modify_pass = "com.hqd.app_manager:id/modify_pass"
    id_modify_phone = "com.hqd.app_manager:id/modify_phone"
    id_finger_toggle_layout = "com.hqd.app_manager:id/finger_toggle_layout"
    id_clear_cache = "com.hqd.app_manager:id/clear_cache"
    id_log_out = "com.hqd.app_manager:id/log_out"
    id_permission_deny_button = "com.android.packageinstaller:id/permission_deny_button"
    id_update = "com.hqd.app_manager:id/update"
    id_my_msg = "com.hqd.app_manager:id/my_msg"
    id_tel_num_tv = "com.hqd.app_manager:id/tel_num_tv"
    id_warning_tv = "com.hqd.app_manager:id/warning_tv"
    id_toolbar_right_second_btn = "com.hqd.app_manager:id/toolbar_right_second_btn"
    id_toolbar_title_tv = "com.hqd.app_manager:id/toolbar_title_tv"
    id_toolbar_right_tv = "com.hqd.app_manager:id/toolbar_right_tv"
    id_search_edit = "com.hqd.app_manager:id/search_edit"
    id_add = "com.hqd.app_manager:id/add"
    id_refuse = "com.hqd.app_manager:id/refuse"
    id_remark = "com.hqd.app_manager:id/remark"
    id_setting = "com.hqd.app_manager:id/shezhi"
    id_log_out = "com.hqd.app_manager:id/log_out"
    id_new_friend = "com.hqd.app_manager:id/new_friend"
    id_contact_layout = "com.hqd.app_manager:id/contact_layout"
    id_result = "com.hqd.app_manager:id/result"
    me = "com.hqd.app_manager:id/meLayout"
    id_contact_item_name = "com.hqd.app_manager:id/contact_item_name"
    id_contact_item_name_tv = "com.hqd.app_manager:id/contact_item_name_tv"
    id_search = "com.hqd.app_manager:id/search"
    id_btn_login = "com.hqd.app_manager:id/btn_login"
    id_toolbar_left_btn = "com.hqd.app_manager:id/toolbar_left_btn"
    id_new_count = "com.hqd.app_manager:id/new_count"
    id_next_btn = "com.hqd.app_manager:id/next_btn"
    id_warning_tv = "com.hqd.app_manager:id/warning_tv"
    id_address = "com.hqd.app_manager:id/address"
    id_address_layout = "com.hqd.app_manager:id/address_layout"
    id_infor_modify = "com.hqd.app_manager:id/infor_modify"
    id_content_container = "com.hqd.app_manager:id/content_container"
    id_business_app_tag1 = "com.hqd.app_manager:id/business_app_tag1"
    id_business_app_name = "com.hqd.app_manager:id/business_app_name"
    id_homeLayout = "com.hqd.app_manager:id/homeLayout"
    id_serviceLayout = "com.hqd.app_manager:id/serviceLayout"
    id_contact_item_remark = "com.hqd.app_manager:id/contact_item_remark"
    id_profile_layout = "com.hqd.app_manager:id/profile_layout"
    id_head_actionmode_title = "com.android.gallery3d:id/head_actionmode_title"
    id_permission_allow_button = "com.android.packageinstaller:id/permission_allow_button"
    id_shutter_button = "com.huawei.camera:id/shutter_button"
    id_head_select_left = "com.android.gallery3d:id/head_select_left"
    id_group = "com.hqd.app_manager:id/group"
    id_group_name = "com.hqd.app_manager:id/group_name"
    id_save = "com.hqd.app_manager:id/save"
    id_disslove = "com.hqd.app_manager:id/dissolve"
    id_btn_selectPositive = "com.hqd.app_manager:id/btn_selectPositive"
    id_btn_selectNegative = "com.hqd.app_manager:id/btn_selectNegative"
    id_serviceLayout = "com.hqd.app_manager:id/serviceLayout"
    id_name = "com.hqd.app_manager:id/name"
    id_webView = "com.hqd.app_manager:id/webView"
    id_title = "com.hqd.app_manager:id/title"
    id_close = "com.hqd.app_manager:id/close"
    id_oper = "com.hqd.app_manager:id/oper"
    id_common = "com.hqd.app_manager:id/common"
    id_workLayout = "com.hqd.app_manager:id/workLayout"
    id_rfab = "com.hqd.app_manager:id/rfab"
    id_rfab_content_label_list_root_view = "com.hqd.app_manager:id/rfab__content_label_list_root_view"
    id_rfab__content_label_list_label_tv = "com.hqd.app_manager:id/rfab__content_label_list_label_tv"
    id_content = "com.hqd.app_manager:id/content"
    id_executor = "com.hqd.app_manager:id/executor"
    id_executor_layout = "com.hqd.app_manager:id/executor_layout"
    id_self_layout = "com.hqd.app_manager:id/self_layout"
    id_start_layout = "com.hqd.app_manager:id/start_layout"
    id_btnSubmit = "com.hqd.app_manager:id/btnSubmit"
    id_end_layout = "com.hqd.app_manager:id/end_layout"
    id_contact = "com.hqd.app_manager:id/contact"
    id_copy_layout = "com.hqd.app_manager:id/copy_layout"
    id_copys_count = "com.hqd.app_manager:id/copys_count"
    id_remind_option = "com.hqd.app_manager:id/remind_option"
    id_end_option_layout = "com.hqd.app_manager:id/end_option_layout"
    id_toolbar_right_btn = "com.hqd.app_manager:id/toolbar_right_btn"
    id_spinner = "com.hqd.app_manager:id/spinner"
    id_checkbox = "com.hqd.app_manager:id/checkbox"
    id_process_content = "com.hqd.app_manager:id/process_content"
    id_button1 = "android:id/button1"
    id_ok_button = "com.android.packageinstaller:id/ok_button"
    id_done_button = "com.android.packageinstaller:id/done_button"
    id_again_option = "com.hqd.app_manager:id/again_option"
    id_sex = "com.hqd.app_manager:id/sex"
    id_tel_num = "com.hqd.app_manager:id/tel_num"
    id_verify_code_btn = "com.hqd.app_manager:id/verify_code_btn"
    id_verify_code_edit = "com.hqd.app_manager:id/verify_code_edit"
    id_password_tel_num = "com.hqd.app_manager:id/password_tel_num"
    id_password_next_btn = "com.hqd.app_manager:id/password_next_btn"
    id_denglu_tv = "com.hqd.app_manager:id/denglu_tv"
    id_password_verify_code_edit = "com.hqd.app_manager:id/password_verify_code_edit"
    id_theme = "com.hqd.app_manager:id/theme"
    id_redo = "com.hqd.app_manager:id/redo"
    id_locate = "com.hqd.app_manager:id/locate"
    id_take_in_layout = "com.hqd.app_manager:id/take_in_layout"
    id_sign_in_layout = "com.hqd.app_manager:id/sign_in_layout"
    id_start_time = "com.hqd.app_manager:id/start_time"
    id_star = "com.hqd.app_manager:id/star"
    id_end_time = "com.hqd.app_manager:id/end_time"
    id_right_btn = "com.hqd.app_manager:id/right_btn"
    id_input = "com.hqd.app_manager:id/input"
    id_sign = "com.hqd.app_manager:id/sign"
    id_status = "com.hqd.app_manager:id/status"
    id_tv_tinted_spinner = "com.hqd.app_manager:id/tv_tinted_spinner"
    id_end_date = "com.hqd.app_manager:id/end_date"
    id_date = "com.hqd.app_manager:id/date"
    id_creator = "com.hqd.app_manager:id/creator"
    id_take_in = "com.hqd.app_manager:id/take_in"
    id_again_layout = "com.hqd.app_manager:id/again_layout"
    id_text = "com.hqd.app_manager:id/text"
    id_yunpan = "com.hqd.app_manager:id/yunpan"
    id_tv_name = "com.hqd.app_manager:id/tv_name"
    id_my_files = "com.hqd.app_manager:id/my_files"
    id_upload_file = "com.hqd.app_manager:id/upload_file"
    id_btn_addbook = "com.hqd.app_manager:id/btn_addbook"
    id_permission_allow_button = "com.android.packageinstaller:id/permission_allow_button"
    id_new_folder = "com.hqd.app_manager:id/new_folder"
    id_name = "com.hqd.app_manager:id/name"
    id_size = "com.hqd.app_manager:id/size"
    id_user_agreement_text = "com.hqd.app_manager:id/user_agreement_text"
    id_user_agreement_check = "com.hqd.app_manager:id/user_agreement_check"
    id_remove_this_folder = "com.hqd.app_manager:id/remove_this_folder"
    id_bubble_bg = "com.hqd.app_manager:id/bubble_bg"
    id_downloaded_title = "com.hqd.app_manager:id/downloaded_title"
    id_tv_path = "com.hqd.app_manager:id/tv_path"
    id_bubble = "com.hqd.app_manager:id/bubble"
    id_toolbar_right_btn_bubble = "com.hqd.app_manager:id/toolbar_right_btn_bubble"
    id_path = "com.hqd.app_manager:id/path"
    id_path_blue = "com.hqd.app_manager:id/path_blue"
    id_upload_title = "com.hqd.app_manager:id/upload_title"
    id_remove = "com.hqd.app_manager:id/remove"
    id_backlog_btn = "com.hqd.app_manager:id/backlog_btn"
    id_item_horizon_imageView = "com.hqd.app_manager:id/item_horizon_imageView"
    id_verify_code_content = "com.hqd.app_manager:id/verify_code_content"
    id_count = "com.hqd.app_manager:id/count"
    id_theme1 = "com.hqd.app_manager:id/theme1"
    id_dept_files = "com.hqd.app_manager:id/dept_files"
    id_creator_name = "com.hqd.app_manager:id/creator_name"
    id_mail = "com.hqd.app_manager:id/mail"
    id_bottom_inbox = "com.hqd.app_manager:id/bottom_inbox"
    id_bottom_my_mail = "com.hqd.app_manager:id/bottom_my_mail"
    id_new_mail = "com.hqd.app_manager:id/new_mail"
    id_receiver = "com.hqd.app_manager:id/receiver"
    id_reply = "com.hqd.app_manager:id/reply"
    id_reply_all = "com.hqd.app_manager:id/reply_all"
    id_forward = "com.hqd.app_manager:id/forward"
    id_copyer = "com.hqd.app_manager:id/copyer"
    id_file = "com.hqd.app_manager:id/file"
    id_receiver_person = "com.hqd.app_manager:id/receiver_person"
    id_copyer_person = "com.hqd.app_manager:id/copyer_person"
    id_mem_layout = "com.hqd.app_manager:id/mem_layout"
    id_send_account = "com.hqd.app_manager:id/send_account"
    id_send = "com.hqd.app_manager:id/send"
    id_bar_title = "com.hqd.app_manager:id/bar_title"
    id_btn_back = "com.hqd.app_manager:id/btn_back"
    id_img = "com.hqd.app_manager:id/img"
    id_drafts = "com.hqd.app_manager:id/drafts"
    id_drafts_tv = "com.hqd.app_manager:id/drafts_tv"
    id_inbox = "com.hqd.app_manager:id/inbox"
    id_select = "com.hqd.app_manager:id/select"
    id_check = "com.hqd.app_manager:id/check"
    id_cancel_check = "com.hqd.app_manager:id/cancel_check"
    id_delete = "com.hqd.app_manager:id/delete"
    id_time = "com.hqd.app_manager:id/time"
    id_receiver_title = "com.hqd.app_manager:id/receiver_title"
    id_copyer_title = "com.hqd.app_manager:id/copyer_title"
    id_theme_title = "com.hqd.app_manager:id/theme_title"
    id_send_box = "com.hqd.app_manager:id/send_box"
    id_resend = "com.hqd.app_manager:id/resend"
    id_dustbin = "com.hqd.app_manager:id/dustbin"


class WebControl:
    # web url client
    web_url = "http://114.116.46.120:8090/#/sign/in"
    # 登录界面-账号框
    web_login_count = "/html/body/div[1]/div/section[1]/div/div/div/div/div[2]/div/div/form/div[1]/div/div/input"
    # 网页登录手机号码错误
    web_error_count = "/html/body/div[1]/div/section[1]/div/div/div/div/div[2]/div/div/form/div[1]/div/div[2]"
    # 登录界面-密码框
    web_login_password = "/html/body/div[1]/div/section[1]/div/div/div/div/div[2]/div/div/form/div[2]/div/div/input"
    # 登录界面-密码错误
    web_login_password_error = "//*[@id=\"app\"]/div/section[1]/div/div/div/div/div[2]/div/div/form/div[2]/div/div[2]"
    # 登录界面-参数错误-class-name
    web_login_parameter_error = "ivu-form-item-error-tip"
    # 登录界面-确定按钮
    web_login_button = "/html/body/div[1]/div/section[1]/div/div/div/div/div[2]/div/div/form/div[4]/div"
    # 登陆成功的判断
    web_login_success = "//*[@id=\"app\"]/div/header/div/div[1]/span"
    # 登录时弹出的错误提示
    web_login_error = "/html/body/div[3]/p/div"
    # 关闭登录时弹出的错误提示
    web_close_login_error = "/html/body/div[3]/div[7]/div/button"

    # 登录界面-注册按钮
    web_register = "//*[@id=\"app\"]/div/header/div/div[1]/a[2]/button"
    # 注册界面-用户协议链接
    web_register_procotol = "//*[@id=\"app\"]/div/section[1]/div/div/div/div/form/div[4]/div/label/a"
    # 注册界面-手机号码输入框
    web_register_phone_num = "//*[@id=\"app\"]/div/section[1]/div/div/div/div/form/div[1]/div/div[1]/input"
    # 注册界面-登录密码输入框
    web_register_password = "//*[@id=\"app\"]/div/section[1]/div/div/div/div/form/div[2]/div/div/input"
    # 注册界面-登录密码输入错误框
    web_register_password_error = "//*[@id=\"app\"]/div/section[1]/div/div/div/div/form/div[2]/div/div[2]"
    # 注册界面-手机号码错误
    web_register_phone_num_error = "//*[@id=\"app\"]/div/section[1]/div/div/div/div/form/div[1]/div/div[2]"
    # 注册界面-获取验证码按钮
    web_identify_button = "//*[@id=\"app\"]/div/section[1]/div/div/div/div/form/div[3]/div/div/div[2]/button"
    # 注册界面-验证码输入框
    web_identify_input = "//*[@id=\"app\"]/div/section[1]/div/div/div/div/form/div[3]/div/div/div[1]/div/input"
    # 注册界面-验证码为空的报错
    web_identify_input_error = "//*[@id=\"app\"]/div/section[1]/div/div/div/div/form/div[3]/div/div[2]"
    # 注册界面-验证码错误提示
    web_register_identify_error_sign = "/html/body/div[3]/p/div"
    # 注册界面-关闭验证码错误提示
    web_register_close_identify_error_sign = "/html/body/div[3]/div[7]/div/button"
    # 注册界面-注册按钮
    web_register_save = "//*[@id=\"app\"]/div/section[1]/div/div/div/div/form/div[5]/div/button"
    # 注册界面-用户协议判断是否默认勾选
    web_register_procotol_label = "//*[@id=\"app\"]/div/section[1]/div/div/div/div/form/div[4]/div/label"
    # 注册界面-用户协议复选框
    web_register_procotol_checkbox = "//*[@id=\"app\"]/div/section[1]/div/div/div/div/form/div[4]/div/label/span/input"
    # 注册界面-用户协议内容
    web_user_procotol = "//*[@id=\"app\"]/div/div"
    # 注册界面-用户已存在
    web_user_already_exist = "/html/body/div[3]/p/div"
    web_close_user_already_exist = "/html/body/div[3]/div[7]/div/button"

    # 登录界面-忘记密码
    web_forget_password = "//*[@id=\"app\"]/div/section[1]/div/div/div/div/div[2]/div/div/form/div[5]/div/div/div[1]"
    # 忘记密码界面-输入手机号码框
    web_fgpswd_phone = "//*[@id=\"app\"]/div/section[1]/div/div/div/div/div[2]/form/div[1]/div/div/input"
    # 忘记密码界面-获取验证码按钮
    web_iden_code_button = "//*[@id=\"app\"]/div/section[1]/div/div/div/div/div[2]/form/div[2]/div/div/div[2]/button"
    # 忘记密码界面-验证码输入框
    web_iden_code_input = "//*[@id=\"app\"]/div/section[1]/div/div/div/div/div[2]/form/div[2]/div/div/div[1]/div/input"
    # 忘记密码界面-手机号码输入错误提示
    web_fgpd_count_error = "//*[@id=\"app\"]/div/section[1]/div/div/div/div/div[2]/form/div[1]/div/div[2]"
    # 忘记密码界面-验证码输入错误提示
    web_fgpd_iden_error = "//*[@id=\"app\"]/div/section[1]/div/div/div/div/div[2]/form/div[2]/div/div[2]"
    # 忘记密码界面-用户不存在提示
    web_fgpd_count_not_exist = "/html/body/div[3]/p/div"
    # 忘记密码界面-下一步
    web_fgpd_next_button = "//*[@id=\"app\"]/div/section[1]/div/div/div/div/div[2]/form/div[3]/div/button"
    # 忘记密码界面-验证码错误弹出提示框
    web_fgpd_iden_alert_error = "/html/body/div[3]/p/div"
    # 忘记密码界面-验证码错误弹出提示框-OK
    web_fgpd_iden_alert_error_ok = "/html/body/div[3]/div[7]/div/button"
    # 忘记密码界面-验证码超时提示
    web_fgpd_iden_timeout = "/html/body/div[3]/p/div"
    # 忘记密码界面-输入新密码
    web_fgpd_new_password = "//*[@id=\"app\"]/div/section[1]/div/div/div/div/div[3]/form/div[1]/div/div/input"
    # 忘记密码界面-重新输入新密码
    web_fgpd_re_new_password = "//*[@id=\"app\"]/div/section[1]/div/div/div/div/div[3]/form/div[2]/div/div/input"
    # 忘记密码界面－输入新密码后－确定
    web_fgpd_ok_button = "//*[@id=\"app\"]/div/section[1]/div/div/div/div/div[3]/form/div[3]/div/button"
    # 忘记密码界面-提示输入的密码不规范
    web_fgpd_count_norm = "//*[@id=\"app\"]/div/section[1]/div/div/div/div/div[3]/form/div[1]/div/div[2]"
    # 登录退出
    web_login_out = "//*[@id=\"app\"]/div/header/div/div[1]/span"
    # 忘记密码界面-两次输入的密码不一致
    web_input_password_diff = "//*[@id=\"app\"]/div/section[1]/div/div/div/div/div[3]/form/div[2]/div/div[2]"

    # 我的资料界面
    web_my_data = "//*[@id=\"app\"]/div/header/div/div[1]/div[2]"
    # 修改资料界面-昵称
    web_revise_data_nickname = "//*[@id=\"app\"]/div/section[1]/section/div/div[2]/div/form/div[1]/div/div/div/div/input"
    # 修改资料界面-真实姓名
    web_revise_data_realname = "//*[@id=\"app\"]/div/section[1]/section/div/div[2]/div/form/div[2]/div/div/div/div/input"
    # 修改资料界面-真实姓名错误
    web_revise_data_realname_error = "//*[@id=\"app\"]/div/section[1]/section/div/div[2]/div/form/div[2]/div/div[2]"
    # 修改资料界面-性别
    web_revise_data_sex = "//*[@id=\"app\"]/div/section[1]/section/div/div[2]/div/form/div[3]/div/div/label[1]/span/input"
    # 修改资料界面-邮箱
    web_revise_data_mail = "//*[@id=\"app\"]/div/section[1]/section/div/div[2]/div/form/div[5]/div/div/div/div/input"
    # 修改资料界面-保存
    web_revise_data_save = "//*[@id=\"app\"]/div/section[1]/section/div/div[2]/div/form/div[8]/div/button/span"

    # 首页
    web_home_page = "//*[@id=\"app\"]/div/header/div/div[2]/ul/li[1]/a"
    # 首页轮播图片
    web_home_page_pictrue = "//*[@id=\"app\"]/div/section[1]/div/div/div/div/div/div"
    # 是否已开通应用按钮
    web_open_app_server_button = "//*[@id=\"app\"]/div/section[1]/div/div/div/div/div[1]/div[1]/button"
    # 首页-最下方-推荐APP
    web_recommend_APP = "center"

    # 应用集合入口
    web_APP_set = "//*[@id=\"app\"]/div/header/div/div[2]/ul/li[4]/a"
    # 应用集合-精品-热门推荐-class-name
    web_hot_recommend_server = "app-card"
    # 应用集合-行业分类（标题）
    web_category = "//*[@id=\"app\"]/div/section[1]/div/div/ul/li[2]/span"
    # 应用集合-行业分类（内容）-class-name
    web_category_content = "ivu-row"
    # 应用集合-行业分类-APP-服务
    web_category_app_server = "app-card"
    # 应用集合-行业分类-应用详情-入口
    web_APP_detail = "//*[@id=\"app\"]/div/section[1]/div/div/div[2]/div/div/div/div[1]/div/div[1]/a/img"
    # 应用集合-应用详情界面-应用介绍
    web_APP_introduction = "//*[@id=\"app\"]/div/section[1]/div/div/div/div/div[1]/div[2]/h6"
    # 应用集合-应用详情界面-ISV信息
    web_APP_isv_info = "//*[@id=\"app\"]/div/section[1]/div/div/div/div/div[2]"


class WebControlServer:
    # web url server
    web_url = "http://114.116.46.120:8080/scap-portal/#/login"
    # 登录界面-账号框
    web_login_count = "//*[@id=\"app\"]/div/div/div/div[2]/div/form/div[1]/div/div/input"
    # 登录界面-密码框
    web_login_password = "//*[@id=\"app\"]/div/div/div/div[2]/div/form/div[2]/div/div/input"
    # 登录界面-确认按钮
    web_login_button = "//*[@id=\"app\"]/div/div/div/div[2]/div/form/div[3]/div/button"
    # 登录界面-退出按钮
    web_login_out = "//*[@id=\"app\"]/div/div[1]/div[2]/ul/li[6]"
    # 登录成功之后-用户中心
    web_user_center = "//*[@id=\"app\"]/div/div[1]/div[2]/ul/li[5]"
    # 用户中心界面正文
    web_user_protocol = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[2]/div/form/div[2]/div/div/div[2]/div[1]"
    # 用户中心界面-启用协议按钮
    web_user_protocol_start_used = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[2]/div/form/div[3]/div/div/label[1]"
    # 用户中心界面-停用协议按钮
    web_user_protocol_stop_used = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[2]/div/form/div[3]/div/div/label[2]"
    # 用户中心界面-保存协议
    web_user_protocol_save = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[2]/div/form/div[4]/div/button"

    # 登录成功之后-大数据管理
    web_big_data = "//*[@id=\"app\"]/div/div[1]/div[2]/ul/li[1]"
    # 大数据管理界面-数据字典主题维护
    web_data_dictionary_theme_maintain = "//*[@id=\"app\"]/div/div[2]/div[1]/div/div[2]/ul/li[4]/div"
    # 大数据管理平台-数据字典主题
    web_data_dictionary_theme = "//*[@id=\"app\"]/div/div[2]/div[1]/div/div[2]/ul/li[4]/ul/li"
    # 大数据管理平台-添加主题
    web_data_add_theme = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[2]/div[2]/div/button"
    # 大数据管理平台-主题名称
    web_data_theme_name = "/html/body/div[10]/div[2]/div/div/div[2]/form/div[1]/div/div/input"
    # 大数据管理-主题分类
    web_data_theme_type = "/html/body/div[10]/div[2]/div/div/div[2]/form/div[2]/div/div/div[1]/div/span"
    # 大数据管理-主题分类-第一个主题
    web_data_first_theme_type = "/html/body/div[10]/div[2]/div/div/div[2]/form/div[2]/div/div/div[2]/ul[2]/li[1]"
    # 大数据管理-添加主题保存
    web_data_add_theme_save = "/html/body/div[10]/div[2]/div/div/div[3]/button[2]"
    # 大数据管理-搜索主题输入框
    web_data_theme_search_input = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/input"
    # 大数据管理-搜索主题输入框-点击搜索
    web_data_theme_search_button = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/i"
    # 大数据管理-添加标准字典
    web_data_add_standard_dic_management = "//*[@id=\"app\"]/div/div[2]/div[1]/div/div[2]/ul/li[5]/div"
    # 大数据管理-标准字典管理
    web_data_standard_dic = "//*[@id=\"app\"]/div/div[2]/div[1]/div/div[2]/ul/li[5]/ul/li"
    # 大数据管理-添加字典
    web_data_add_dic = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[2]/div[2]/button"
    # 大数据管理-添加字典-选择主题
    web_data_dic_theme = "/html/body/div[10]/div[2]/div/div/div[2]/form/div[1]/div/div/div[1]"
    # 大数据管理-添加字典-选择第一个主题
    web_data_dic_first_theme = "/html/body/div[10]/div[2]/div/div/div[2]/form/div[1]/div/div/div[2]/ul[2]"
    # 大数据管理-添加字典-输入库名称
    web_data_dic_lib_name = "/html/body/div[10]/div[2]/div/div/div[2]/form/div[2]/div/div/input"
    # 大数据管理-添加字典-输入表名称
    web_data_dic_table_name = "/html/body/div[10]/div[2]/div/div/div[2]/form/div[3]/div/div/input"
    # 大数据管理-添加字典-输入字段名称
    web_data_dic_str_name = "/html/body/div[10]/div[2]/div/div/div[2]/form/div[4]/div/div/input"
    # 大数据管理-添加字典-输入字段名称错误
    web_data_dic_str_name_error = "/html/body/div[10]/div[2]/div/div/div[2]/form/div[4]/div/div[2]"
    # 大数据管理-添加字典-输入字段描述
    web_data_dic_str_dis = "/html/body/div[10]/div[2]/div/div/div[2]/form/div[5]/div/div/input"
    # 大数据管理-添加字典-输入字段内容
    web_data_dic_str_content = "/html/body/div[10]/div[2]/div/div/div[2]/form/div[6]/div/div/input"
    # 大数据管理-添加字典-输入字段类型
    web_data_dic_str_type = "/html/body/div[10]/div[2]/div/div/div[2]/form/div[7]/div/div/input"
    # 大数据管理-添加字典-输入字段类型错误
    wen_data_dic_str_type_error = "/html/body/div[10]/div[2]/div/div/div[2]/form/div[7]/div/div[2]"
    # 大数据管理-添加字典-输入字段长度
    web_data_dic_str_len = "/html/body/div[10]/div[2]/div/div/div[2]/form/div[8]/div/div/input"
    # 大数据管理-添加字典-输入字段长度错误
    web_data_dic_str_len_error = "/html/body/div[10]/div[2]/div/div/div[2]/form/div[8]/div/div[2]"
    # 大数据管理-添加字典-输入为空
    web_data_dic_none = "/html/body/div[10]/div[2]/div/div/div[2]/form/div[9]/div/div/label[1]"
    # 大数据管理-添加字典-输入不为空
    web_data_dic_not_none = "/html/body/div[10]/div[2]/div/div/div[2]/form/div[9]/div/div/label[2]"
    # 大数据管理-添加字典-保存
    web_data_add_dic_save = "/html/body/div[10]/div[2]/div/div/div[3]/button[2]"
    # 大数据管理-添加字典-取消
    web_data_add_dic_cancel = "/html/body/div[10]/div[2]/div/div/div[3]/button[1]"
    # 大数据管理-创建成功的主题
    web_data_successful_theme = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[3]/div[1]/div/div[2]/table/tbody/tr/td[1]/div/span"
    # 大数据管理-创建成功的字典主题
    web_data_successful_dic_theme = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[3]/div[1]/div/div[2]/table/tbody/tr/td[1]/div"
    # 删除标准字典
    web_data_del_dic = web_data_successful_dic_theme[:77]+"td[10]/div/div/button[2]"
    # 确定删除字典
    web_data_del_dic_ok = "/html/body/div[11]/div[2]/div/div/div/div/div[3]/button[2]"
    # 修改标准字典
    web_data_dic_edit = web_data_successful_dic_theme[:77] + "td[10]/div/div/button[1]"
    # 删除字典主题
    web_data_del_dic_theme = web_data_successful_theme[:77]+"td[3]/div/div/button[2]"
    # 确定删除字典主题
    web_data_del_dic_theme_ok = "/html/body/div[11]/div[2]/div/div/div/div/div[3]/button[2]"
    # 数据标准字典-搜索输入框
    web_data_dic_search_input = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/input"
    # 数据标准字典-搜索框-搜索按钮
    web_data_dic_search_button = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/i"
    # 数据标准字典-创建成功的字典-class_name
    web_data_dic_succ_data = "ivu-table-row"
    # 数据标准字典-创建成功的字典-字段名称-class_name
    web_data_dic_succ_data_cell = "ivu-table-cell"

    # 大数据管理-大数据展示
    web_data_big_data_display = "//*[@id=\"app\"]/div/div[2]/div[1]/div/div[2]/ul/li[1]/div"
    # 大数据管理-大数据展示-平台统计-入口
    web_data_display_platform_statistics = "//*[@id=\"app\"]/div/div[2]/div[1]/div/div[2]/ul/li[4]/ul/li[4]"
    # 大数据管理-大数据展示-平台统计-界面
    web_data_display_platform_statistics_page = "//*[@id=\"app\"]/div/div[2]/div[2]/div"
    # 大数据管理-大数据展示-平台统计-注册用户信息
    web_data_display_platform_statistics_register_info = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div[2]"
    # 大数据管理-大数据展示-模板列表
    web_data_display_template_list = "//*[@id=\"app\"]/div/div[2]/div[1]/div/div[2]/ul/li[4]/ul/li[3]"
    # 大数据管理-大数据展示-数据集管理-入口
    web_data_display_data_list_management = "//*[@id=\"app\"]/div/div[2]/div[1]/div/div[2]/ul/li[1]/ul/li[4]"
    # 大数据管理-大数据展示-数据集管理-添加数据库
    web_data_display_add_sql = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/button"
    # 大数据管理-大数据展示-数据集管理-添加数据库-数据源名称
    web_data_display_add_sql_data_name = "/html/body/div[10]/div[2]/div/div/div[2]/form/div[1]/div/div/input"
    # 大数据管理-大数据展示-数据集管理-添加数据库-数据库地址
    web_data_display_add_sql_address = "/html/body/div[10]/div[2]/div/div/div[2]/form/div[2]/div/div/div[1]/div/input"
    # 大数据管理-大数据展示-数据集管理-添加数据库-数据库地址-端口号
    web_data_display_add_sql_port = "/html/body/div[10]/div[2]/div/div/div[2]/form/div[2]/div/div/div[2]/div/input"
    # 大数据管理-大数据展示-数据集管理-添加数据库-数据库名称
    web_data_display_add_sql_name = "/html/body/div[10]/div[2]/div/div/div[2]/form/div[3]/div/div/input"
    # 大数据管理-大数据展示-数据集管理-添加数据库-用户名
    web_data_display_add_sql_user = "/html/body/div[10]/div[2]/div/div/div[2]/form/div[4]/div/div/input"
    # 大数据管理-大数据展示-数据集管理-添加数据库-密码
    web_data_display_add_sql_password = "/html/body/div[10]/div[2]/div/div/div[2]/form/div[5]/div/div/input"
    # 大数据管理-大数据展示-数据集管理-添加数据库-取消
    web_data_display_add_sql_cancel = "/html/body/div[10]/div[2]/div/div/div[3]/button[1]"
    # 大数据管理-大数据展示-数据集管理-添加数据库-保存
    web_data_display_add_sql_save = "/html/body/div[10]/div[2]/div/div/div[3]/button[2]"
    # 大数据管理-大数据展示-数据集管理-添加数据库-更新
    web_data_display_add_sql_updata = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/button[1]"
    # 大数据管理-大数据展示-数据集管理-添加数据库-弹出错误提示
    web_data_display_add_sql_error = "/html/body/div[3]/p/div"
    # 大数据管理-大数据展示-数据集管理-添加数据库-弹出错误提示
    web_data_display_add_sql_close_error = "/html/body/div[3]/div[7]/div/button"
    # 大数据管理-大数据展示-数据集管理-添加数据库-输入错误
    web_data_display_add_sql_parameter_error = "ivu-form-item-error-tip"
    # 大数据管理-大数据展示-数据集管理-添加数据库-已创建成功的数据-class-name
    web_data_display_creat_successful_data = "ivu-checkbox-wrapper"
    # 大数据管理-大数据展示-数据集管理-添加数据库-已创建成功的数据-编辑按钮
    web_data_display_creat_successful_data_edit = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[1]/button[1]"
    # 大数据管理-大数据展示-数据集管理-添加数据库-已创建成功的数据-删除按钮
    web_data_display_creat_successful_data_delete = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[1]/button[2]"
    # 大数据管理-大数据展示-数据集管理-添加数据库-已创建成功的数据-确认删除
    web_data_display_creat_successful_data_confirm_delete = "/html/body/div[11]/div[2]/div/div/div/div/div[3]/button[2]"



    # 应用管理入口
    app_management_center = "//*[@id=\"app\"]/div/div[1]/div[2]/ul/li[3]"
    # 应用管理中心-应用分类
    app_classification = "//*[@id=\"app\"]/div/div[2]/div[1]/div/div[2]/ul/li[2]/ul/li[1]"
    # 应用管理中心-应用分类-添加分类
    app_add_classification = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[2]/div[2]/div/button"
    # 应用管理中心-应用分类-添加分类-所添加分类的名称
    app_add_classification_name = "/html/body/div[7]/div[2]/div/div/div[2]/form/div[1]/div/div/input"
    # 应用管理中心-应用分类-添加分类-所添加分类的图标
    app_add_classification_icon = "/html/body/div[7]/div[2]/div/div/div[2]/form/div[2]/div/div/input"
    # 应用管理中心-应用分类-添加分类-确定
    app_add_classification_ok = "/html/body/div[7]/div[2]/div/div/div[3]/button[2]"
    # 应用管理中心-应用分类-添加分类-取消
    app_add_classification_cancel = "/html/body/div[7]/div[2]/div/div/div[3]/button[1]"
    # 应用管理中心-所成功创建的应用分类-class name
    app_classification_succ_creat_data = "ivu-table-row"
    # 应用管理中心-应用分类-搜索分类输入框
    app_classification_search_input = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/input"
    # 应用管理中心-应用分类-搜索按钮
    app_classification_search_button = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/i"
    # 应用管理中心-应用分类-删除分类
    app_classification_del = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[3]/div[2]/div/div[2]/table/tbody/tr[1]/td[3]/div/div/button[2]"
    # 应用管理中心-应用分类-编辑分类
    app_classification_edit = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[3]/div[2]/div/div[2]/table/tbody/tr[1]/td[3]/div/div/button[1]"
    # 应用管理中心-应用分类-删除分类-确认删除
    app_classification_del_confim = "/html/body/div[8]/div[2]/div/div/div/div/div[3]/button[2]"
    # 应用管理中心-应用分类-添加分类-分类重复提示
    app_classification_repeat_prompt = "/html/body/div[3]/p/div"
    # 应用管理中心-应用分类-添加分类-关闭分类重复提示
    app_classification_close_repeat_prompt = "/html/body/div[3]/div[7]/div/button"

    # 应用管理中心-应用创建
    app_creat = "//*[@id=\"app\"]/div/div[2]/div[1]/div/div[2]/ul/li[1]/ul/li[3]"
    # 应用管理中心-上传图片栏
    app_upload_icon = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[3]/div/form/div[1]/div/div/div/div"
    # 应用管理中心-上传图片错误
    app_creat_icon_error = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[3]/div/form/div[1]/div/div[2]"
    # 应用管理中心-应用名称输入
    app_creat_name = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[3]/div/form/div[2]/div/div/div/div/input"
    # 应用管理中心-应用名称输入错误
    app_creat_name_error = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[3]/div/form/div[2]/div/div[2]"
    # 应用管理中心-应用创建-选择所属行业
    app_creat_industry = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[3]/div/form/div[3]/div/div[1]/div/div/div[1]/div/input"
    # 应用管理中心-应用创建-选择所属行业-选择第一个行业
    app_creat_industry_first = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[3]/div/form/div[3]/div/div[1]/div/div/div[2]/ul[2]/li[1]"
    # 应用管理中心-应用创建-选择付费方式-免费
    app_creat_pay_no_money = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[3]/div/form/div[4]/div/div/label[1]"
    # 应用管理中心-应用创建-选择付费方式-收费
    app_creat_pay_need_money = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[3]/div/form/div[4]/div/div/label[2]"
    # 应用管理中心-应用创建-输入产品负责人
    app_creat_product_owner = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[3]/div/form/div[5]/div/div/div/div/input"
    # 应用管理中心-应用创建-输入产品负责人联系方式
    app_creat_product_owner_phone_num = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[3]/div/form/div[6]/div/div/div/div/input"
    # 应用管理中心-应用创建-选择应用开发商
    app_creat_developer = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[3]/div/form/div[7]/div/div[1]/div/div/div[1]/div/input"
    # 应用管理中心-应用创建-选择第一个应用开发商
    app_creat_developer_first = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[3]/div/form/div[7]/div/div[1]/div/div/div[2]/ul[2]"
    # 应用管理中心-应用创建-应用连接
    app_creat_product_link = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[3]/div/form/div[8]/div/div[1]/div/div/input"
    # 应用管理中心-应用创建-应用连接不正确
    app_creat_product_link_not_true = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[3]/div/form/div[8]/div/div[2]"
    # 应用管理中心-应用创建-应用连接详情
    app_creat_product_link_details = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[3]/div/form/div[9]/div/div[1]/div/div/input"
    # 应用管理中心-应用创建-应用简介
    app_creat_product_details = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[3]/div/form/div[10]/div/div/div/div/textarea"
    # 应用管理中心-应用创建-保存
    app_creat_save = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[3]/div/form/div[12]/div/button"
    # 应用管理中心-应用分类-应用搜索输入
    app_classification_search_input = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/input"
    # 应用管理中心-应用分类-应用搜索按钮
    app_classification_search_button = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/i"
    # 应用管理中心-应用分类-已创建成功的-class_name-<tr>
    app_classification_search_result = "ivu-table-row"
    # 应用管理中心-应用分类-已创建成功的-class_name-<td>
    app_classification_search_td_result = "ivu-table-cell"
    # 应用管理中心-应用分类-已创建成功的-删除
    app_classification_search_result_del = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[3]/div[1]/div/div[2]/table/tbody/tr[1]/td[9]/div/div/button[3]"
    # 应用管理中心-应用分类-已创建成功的-确认删除
    app_classification_search_result_confirm_del = "/html/body/div[7]/div[2]/div/div/div/div/div[3]/button[2]"
    # 应用管理中心-应用分类-已创建成功的-编辑
    app_classification_search_result_edit = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[3]/div[1]/div/div[2]/table/tbody/tr[1]/td[9]/div/div/button[1]"
    # 应用管理中心-应用分类-编辑应用界面-保存按钮
    app_classification_edit_save = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[3]/div/form/div[14]/div/button"

    # 大数据管理-isv字典管理
    web_big_data_isv_dic_management = "//*[@id=\"app\"]/div/div[2]/div[1]/div/div[2]/ul/li[3]/div"
    # 大数据管理-isv字典上传
    web_isv_dic_upload = "//*[@id=\"app\"]/div/div[2]/div[1]/div/div[2]/ul/li[3]/ul/li[1]"
    # 大数据管理-isv字典上传-选择应用
    web_isv_dic_upload_select_app = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[2]/div/form/div[1]/div/div/div/div/div[1]"
    # 大数据管理-isv字典上传-选择应用-第一个应用
    web_isv_dic_upload_select_first_app = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[2]/div/form/div[1]/div/div/div/div/div[2]/ul[2]/li[1]"
    # 大数据管理-isv字典上传-选择isv文件
    web_isv_dic_upload_isv_file = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[2]/div/form/div[2]/div/div[1]/div/div/div/button"
    # 大数据管理-isv字典上传-选择isv文件-确定上传
    web_isv_dic_upload_isv_file_confirm = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[2]/div/form/div[3]/div/div/div/button"
    # 大数据管理-isv字段上传-选择非csv格式文件结果
    web_isv_dic_upload_not_isv_file_result = "/div/div[1]/div/div[2]"

    # 应用中心-isv管理
    app_center_isv_management = "//*[@id=\"app\"]/div/div[2]/div[1]/div/div[2]/ul/li[2]/div"
    # 应用中心-isv信息完善
    app_center_isv_info_complete = "//*[@id=\"app\"]/div/div[2]/div[1]/div/div[2]/ul/li[2]/ul"
    # 应用中心-isv信息完善-企业图标
    app_center_isv_enterprise_icon = "//*[@id=\"app\"]/div/div[2]/div[2]/div/form/div[1]/div[2]/div[1]/div/div/div/div"
    # 应用中心-isv信息完善-isv服务商名称
    app_center_isv_service_provider_name = "//*[@id=\"app\"]/div/div[2]/div[2]/div/form/div[1]/div[2]/div[2]/div/div/div/div/input"
    # 应用中心-isv信息完善-企业所属行业
    app_center_isv_enterprise_industry = "//*[@id=\"app\"]/div/div[2]/div[2]/div/form/div[1]/div[2]/div[3]/div/div/div/div/input"
    # 应用中心-isv信息完善-企业所在地区
    app_center_isv_enterprise_area = "//*[@id=\"app\"]/div/div[2]/div[2]/div/form/div[1]/div[2]/div[4]/div/div/div/div/input"
    # 应用中心-isv信息完善-上传企业主页banner
    app_center_isv_enterprise_banner = "//*[@id=\"app\"]/div/div[2]/div[2]/div/form/div[1]/div[2]/div[6]/div/div/div/button"
    # 应用中心-isv信息完善-企业服务电话
    app_center_isv_enterprise_phone = "//*[@id=\"app\"]/div/div[2]/div[2]/div/form/div[2]/div[2]/div[1]/div/div/div/div/input"
    # 应用中心-isv信息完善-企业服务电话-输入错误
    app_center_isv_enterprise_phone_error = "//*[@id=\"app\"]/div/div[2]/div[2]/div/form/div[2]/div[2]/div[1]/div/div[2]"
    # 应用中心-isv信息完善-企业邮箱
    app_center_isv_enterprise_mail = "//*[@id=\"app\"]/div/div[2]/div[2]/div/form/div[2]/div[2]/div[2]/div/div/div/div/input"
    # 应用中心-isv信息完善-企业邮箱输入错误
    app_center_isv_enterprise_mail_error = "//*[@id=\"app\"]/div/div[2]/div[2]/div/form/div[2]/div[2]/div[2]/div/div[2]"
    # 应用中心-isv信息完善-企业传真
    app_center_isv_enterprise_fax = "//*[@id=\"app\"]/div/div[2]/div[2]/div/form/div[2]/div[2]/div[3]/div/div/div/div/input"
    # 应用中心-isv信息完善-企业地址
    app_center_isv_enterprise_address = "//*[@id=\"app\"]/div/div[2]/div[2]/div/form/div[2]/div[2]/div[4]/div/div/div/div/input"
    # 应用中心-isv信息完善-企业法人
    app_center_isv_enterprise_legal_person = "//*[@id=\"app\"]/div/div[2]/div[2]/div/form/div[3]/div[2]/div[1]/div/div/div/div/input"
    # 应用中心-isv信息完善-企业性质
    app_center_isv_enterprise_nature = "//*[@id=\"app\"]/div/div[2]/div[2]/div/form/div[3]/div[2]/div[2]/div/div/div/div/input"
    # 应用中心-isv信息完善-注册资金
    app_center_isv_enterprise_registered_capital = "//*[@id=\"app\"]/div/div[2]/div[2]/div/form/div[3]/div[2]/div[3]/div/div/div/div/input"
    # 应用中心-isv信息完善-成立日期
    app_center_isv_enterprise_start_time = "//*[@id=\"app\"]/div/div[2]/div[2]/div/form/div[3]/div[2]/div[4]/div/div/div/div/div[1]/div/input"
    # 应用中心-isv信息完善-社会信用代码(税号)
    app_center_isv_enterprise_social_credit_code = "//*[@id=\"app\"]/div/div[2]/div[2]/div/form/div[3]/div[2]/div[5]/div/div/div/div/input"
    # 应用中心-isv信息完善-企业注册地址
    app_center_isv_enterprise_register_address = "//*[@id=\"app\"]/div/div[2]/div[2]/div/form/div[3]/div[2]/div[6]/div/div/div/div/input"
    # 应用中心-isv信息完善-企业经营范围
    app_center_isv_enterprise_business_scope = "//*[@id=\"app\"]/div/div[2]/div[2]/div/form/div[3]/div[2]/div[7]/div/div/div/div/textarea"
    # 应用中心-isv信息完善-保存
    app_center_isv_enterprise_info_save = "//*[@id=\"app\"]/div/div[2]/div[2]/div/form/div[4]/div/div/div/button"

    # 大数据管理-大数据展示-数据集显示-SQL语句输入框
    web_big_data_SQL_input = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/textarea"
    # 大数据管理-大数据展示-数据集显示-SQL语句执行按钮
    web_big_data_SQL_run_button = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/button[3]"
    # 大数据管理-大数据展示-数据集显示-数据集名称输入框
    web_big_data_SQL_list_name = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div/input"
    # 大数据管理-大数据展示-数据集显示-数据集创建按钮
    web_big_data_SQL_list_creat = "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/button[1]"
    # 大数据管理-大数据展示-数据集显示-数据集确认删除
    web_big_data_SQL_list_confirm_del = "//html/body/div[11]/div[2]/div/div/div/div/div[3]/button[2]"
    # 大数据管理-大数据展示-数据集显示-数据集验证不通过
    web_big_data_SQL_input_error = "/html/body/div[3]/p/div"


class ClassName:
    set_personal_info = "set-personal-info"
    multiple_btn_default = "multiple-btn default"
    desc = "desc"
    ivu_modal_header_inner = "ivu-modal-header-inner"
    department = "department"
    name_toleft = "name toleft"
    comment_card = "comment-card"
    tab_title = "tab-title"
    register_label = "register-label"
    ivu_modal_confirm_head_title = "ivu-modal-confirm-head-title"
    ivu_form_item_label = "ivu-form-item-label"
    list_wrap = "list-wrap"
    size = "size"
    ivu_page_item = "ivu-page-item"
    item_typeIcon_imgs = "item typeIcon imgs"
    title = "title"
    rowName = "rowName"
    attaName = "attaName"
    mail_active_title = "mail-active-title"
    tr_unread = "tr unread"
    mail_title_content = "mail-title-content"
    card = "card"
    ivu_menu_item = "ivu-menu-item"
    layout_text = "layout-text"
    ivu_btn = "ivu-btn"
    ivu_input = "ivu-input"
    data_item = "data-item"
    ivu_input_wrapper = "ivu-input-wrapper"
    database_list = "database-list"
    ivu_table_header = "ivu-table-header"
    ivu_table_cell = "ivu-table-cell"
    ivu_menu_submenu = "ivu-menu-submenu"
    ivu_modal_content = "ivu-modal-content"
    ivu_select_item = "ivu-select-item"
    ivu_row = "ivu-row"
    ivu_poptip_body_content_inner = "ivu-poptip-body-content-inner"
    sql_operate = "sql-operate"
    ivu_btn_warning = "ivu-btn ivu-btn-warning"
    ivu_reload_success = "ivu-btn ivu-btn-success"
    ivu_btn_primary = "ivu-btn ivu-btn-primary"
    btn_new_dept = "btn-new-dept"
    ivu_btn_ghost = "ivu-btn ivu-btn-ghost"
    html_render = "html-render"
    ivu_table_row = "ivu-table-row"
    search_icon = "ivu-icon ivu-icon-search ivu-input-icon ivu-input-icon-normal"
    ivu_icon_ios_arrow_down_menu_submenu_title_icon = "ivu-icon ivu-icon-ios-arrow-down ivu-menu-submenu-title-icon"
    menu_title = "menu-title"
    ivu_select_placeholder = "ivu-select-placeholder"
    ivu_select_item = "ivu-select-item"
    ivu_btn_large = "ivu-btn ivu-btn-primary ivu-btn-large"
    ivu_btn_error_small = "ivu-btn ivu-btn-error ivu-btn-small"
    ivu_btn_small = "ivu-btn ivu-btn-small"
    ivu_btn_ghost_small = "ivu-btn ivu-btn-ghost ivu-btn-small"
    ivu_btn_primary_small = "ivu-btn ivu-btn-primary ivu-btn-small"
    ivu_page_total = "ivu-page-total"
    ivu_page_mini = "ivu-page mini"
    ivu_select_selected_value = "ivu-select-selected-value"
    ivu_select_selection = "ivu-select-selection"
    ivu_select_input = "ivu-select-input"
    ivu_table_stripe = "ivu-table ivu-table-border ivu-table-stripe"
    btn_add_ivu_btn_info = "btnAdd ivu-btn ivu-btn-info"
    ivu_btn_error = "ivu-btn ivu-btn-error"
    ivu_btn_ghost = "ivu-btn ivu-btn-ghost"
    group_list = "group-list"
    group_list_ivu_row = "group-list ivu-row"
    group = "group"
    group_edit = "group-edit"
    edit_item = "edit-item"
    ivu_form_item_error_tip = "ivu-form-item-error-tip"
    iconitem = "iconitem"
    ivu_col_span_12 = "group-item ivu-col ivu-col-span-12"
    ivu_vtn_info_small = "ivu-btn ivu-btn-info ivu-btn-small"
    ivu_vtn_warn_small = "ivu-btn ivu-btn-warning ivu-btn-small"
    item_content = "item-content"
    item = "item"
    item_content_c = "item-content-c"
    ivu_btn_long = "ivu-btn ivu-btn-primary ivu-btn-long"
    ivu_modal_confirm_body = "ivu-modal-confirm-body"
    ivu_btn_text_large = "ivu-btn ivu-btn-text ivu-btn-large"
    ivu_poptip_rel = "ivu-poptip-rel"
    ivu_modal_confirm_footer = "ivu-modal-confirm-footer"
    ivu_menu = "ivu-menu"
    ivu_select_dropdown = "ivu-select-dropdown"
    ivu_select_dropdown_list = "ivu-select-dropdown-list"
    ivu_select_single = "ivu-select ivu-select-single"
    ivu_btn_success_small = "ivu-btn ivu-btn-success ivu-btn-small"
    ivu_btn_primary_ng_scope = "btn btn-primary ng-scope"
    btn_inverse_ng_scope = "btn btn-inverse ng-scope"
    btn_addClass_btn = "btn-addClass ivu-btn"
    sweet_alert_showsweetalert_visible = "sweet-alert showSweetAlert visible"
    confirm = "confirm"
    left = "left"
    qleditor_blank = "ql-editor ql-blank"
    ivu_radio = "ivu-radio"
    ivu_radio_wrapper_group_item = "ivu-radio-wrapper ivu-radio-group-item"
    ivu_btn_info = "ivu-btn ivu-btn-info"
    ivu_div_col_span_12 = "ivu-col ivu-col-span-12"
    router_link_exact_active = "router-link-exact-active router-active"
    cancel_btn = "cancel-btn"
    ivu_btn_verify = "ivu-btn btn-verify"
    ivu_checkbox_input = "ivu-checkbox-input"
    ivu_btn_long_register = "ivu-btn ivu-btn-long btn-register"
    user_info = "user-info"
    ivu_col_span_5 = "ivu-col ivu-col-span-5"
    ivu_col_span_2 = "ivu-col ivu-col-span-2"
    ivu_col_span_8 = "ivu-col ivu-col-span-8"
    ivu_col_offset_19 = "ivu-col ivu-col-offset-19"
    ivu_btn_checkCode = "ivu-btn btn-checkCode"
    avator = "avator"
    btn_update_btn = "btn-update ivu-btn"
    user_img_toleft = "user-img toleft"
    ivu_icon_log_out = "ivu-icon ivu-icon-log-out"
    ql_editor = "ql-editor"
    ivu_input_number_input = "ivu-input-number-input"
    ivu_page_next = "ivu-page-next"
    ivu_page_prev = "ivu-page-prev"
    ivu_upload_drag = "ivu-upload ivu-upload-drag"
    ivu_form_item_required = "ivu-form-item ivu-form-item-required"
    ivu_input_wrapper_type = "ivu-input-wrapper ivu-input-type"
    ivu_form_item_content = "ivu-form-item-content"
    ivu_menu_submenu_title = "ivu-menu-submenu-title"
    ivu_icon_ios_folder = "ivu-icon ivu-icon-ios-folder"
    center = "center"
    content = "content"
    wrap = "wrap"
    active = "active"
    more = "more"
    app_card = "app-card"
    app_icon = "app-icon"
    active_tit = "active-tit"
    rside_ivu_col_span_7 = "rside ivu-col ivu-col-span-7"
    ivu_table_body = "ivu-table-body"
    ivu_checkbox_wrapper = "ivu-checkbox-wrapper"
    ivu_selete_item_focus = "ivu-select-item ivu-select-item-focus"
    ivu_table_tip = "ivu-table-tip"
    ivu_tabs_tab_active_focused = "ivu-tabs-tab ivu-tabs-tab-active ivu-tabs-tab-focused"
    ivu_tabs_tabpane = "ivu-tabs-tabpane"
    ivu_tabs_tab = "ivu-tabs-tab"
    num = "num"
    user_menu = "user-menu"
    vue_grid_item_resizable = "vue-grid-item item vue-resizable"
    btn_span = "btn-span"
    btn_component = "btn-component"
    btn_text = "btn-text"
    textarea_render = "textarea-render"
    btn_chart = "btn-chart"
    ivu_dropdown_item = "ivu-dropdown-item"
    ivu_btn_default = "ivu-btn ivu-btn-default"
    no_html_text = "no-html-text"
    owned_app = "owned-app"
    ivu_breadcrumb_item_link = "ivu-breadcrumb-item-link"
    left = "left"
    mail_table = "mail-table"
    right = "right"
    no_data = "no-data"
    tpl_item = "tpl-item"
    fa_plus_circle = "fa fa-plus-circle"
    fa_trash_o = "fa fa-trash-o"
    btn_operator = "btn-operator"
    tpl_item_name = "tpl-item-name"
    full_screen_text = "full-screen-text"
    ivu_tooltip_rel = "ivu-tooltip-rel"
    nav_text_ivu_tabs_nav = "nav-text ivu-tabs-nav"
    task_item = "task-item"
    task_item_name = "task-item-name"
    task_status_done = "task-status-done"
    task_status_undone = "task-status-undone"
    btn_task_detail_ivu_btn = "btn-task-detail ivu-btn"
    ivu_menu_item_active_selected = "ivu-menu-item ivu-menu-item-active ivu-menu-item-selected"
    ivu_icon_plus_circled_icon_normal = "ivu-icon ivu-icon-plus-circled ivu-input-icon ivu-input-icon-normal"
    user_item = "user-item"
    name = "name"
    con = "con"
    ivu_checkbox_wrapper_group_item = "ivu-checkbox-wrapper ivu-checkbox-group-item"
    task_item_content = "task-item-content"
    task_item_detail = "task-item-detail"
    ivu_modal_header = "ivu-modal-header"
    task_copy = "task-copy"
    item_content_ivu_col_span_10 = "item-content ivu-col ivu-col-span-10"
    item_content_ivu_col_span_18 = "item-content ivu-col ivu-col-span-18"
    schedule_item_conent_ivu_row = "schedule-item-content ivu-row"
    schedule_item = "schedule-item"
    schedule_item_name_col_span_2 = "schedule-item-name ivu-col ivu-col-span-2"
    schedule_item_name_col_span_14 = "schedule-item-name ivu-col ivu-col-span-14"
    schedule_item_name_ivu_col_span_14 = "schedule-item-name schedule-icon ivu-col ivu-col-span-14"
    btn_schedule_detail_ivu_btn = "btn-schedule-detail ivu-btn"
    notice_toleft = "notice toleft"
    guide = "guide"
    search_friend = "search-friend"
    search_new_friend = "search-new-friend"
    friend = "friend"
    blue_btn = "blue-btn"
    status = "status"
    tips = "tips"
    letter_wrap = "letter-wrap"
    back_btn = "back-btn"
    white_btn = "white-btn"
    text = "text"
    new_friend = "new-friend"
    avator_add = "avator-add"
    new_friends = "new-friends"
    menu = "menu"
    blue_btn_toright = "blue-btn toright"
    contact_friends = "contact friends"
    ivu_icon_ios_circle_outline = "ivu-icon ivu-icon-ios-circle-outline"
    ivu_icon_ios_checkmark = "ivu-icon ivu-icon-ios-checkmark"
    click_name = "click-name"
    friends = "friends"
    toright = "toright"
    ivu_upload_input = "ivu-upload-input"
    tab_tit = "tab-tit"
    menu_title = "menu-title"
    label = "label"
    ivu_btn_checkCode_disabled = "ivu-btn btn-checkCode-disabled"
    app_more_list = "app-more-list"
    list_title = "list-title"
    white_small_btn_ivu_btn = "white-small-btn ivu-btn"
    ivu_checkbox_inner = "ivu-checkbox-inner"
    del_ivu_icon_android_close = "del-icon ivu-icon ivu-icon-android-close"
    tit = "tit"
    disable_btn_ivu_text = "disable-btn ivu-btn ivu-btn-text"
    ivu_page_item = "ivu-page-item"
    cke_wysiwyg_frame_reset = "cke_wysiwyg_frame cke_reset"
    btn_add_icon_lius_circled = "btn-add ivu-icon ivu-icon-plus-circled"
    td_content_sp = "td-content sp"
    center_star = "center star"
    opt_center = "opt center"
    ivu_icon_ios_star_outline = "ivu-icon ivu-icon-ios-star-outline"
    ivu_icon_ios_star = "ivu-icon ivu-icon-ios-star"
    ivu_tag_text_color_white = "ivu-tag-text ivu-tag-color-white"
    ivu_icon_checkmark_circled = "ivu-icon ivu-icon-checkmark-circled"
    ivu_icon_close_circled = "ivu-icon ivu-icon-close-circled"
    checkCodeInp_toleft_ivu_input_wrapper_type = "checkCodeInp toleft ivu-input-wrapper ivu-input-type"


class ID:
    outportUserDataBtn = "outportUserDataBtn"
    addRoleBtn = "addRoleBtn"
    deleteRoleGroupBtn = "deleteRoleGroupBtn"
    renameRoleGroupBtn = "renameRoleGroupBtn"
    outportRoleDataBtn = "outportRoleDataBtn"
    addUserToRoleBtn = "addUserToRoleBtn"
    delRoleBtn = "delRoleBtn"
    editRoleBtn = "editRoleBtn"
    setRoleRightsBtn = "setRoleRightsBtn"
    showAddRoleModal = "showAddRoleModal"
    showAddRoleGroupModalBtn = "showAddRoleGroupModalBtn"
    submitCommentBtn = "submitCommentBtn"
    addToMyAppBtn = "addToMyAppBtn"
    userInfo = "userInfo"
    getPhoneFormCodeBtn = "getPhoneFormCodeBtn"
    changePhoneBtn = "changePhoneBtn"
    pwdFormOkBtn = "pwdFormOkBtn"
    currentMore = "currentMore"
    currentRow = "currentRow"
    addFolderBtn = "addFolderBtn"
    handleSubmitBtn = "handleSubmitBtn"
    getRegisterCodeBtn = "getRegisterCodeBtn"
    registerBtn = "registerBtn"
    getUpdatePwdCodeBtn = "getUpdatePwdCodeBtn"
    checkUpdatePwdcodeBtn = "checkUpdatePwdcodeBtn"
    updatePasswordBtn = "updatePasswordBtn"
    panelMenu = "panelMenu"
    searchNewFriendBtn = "searchNewFriendBtn"
    addFriend = "addFriend"
    contactMenu = "contactMenu"
    openValidateModalBtn = "openValidateModalBtn"
    requestRejectBtn = "requestRejectBtn"
    requestAgreeBtn = "requestAgreeBtn"
    backBtn = "backBtn"
    friendReq = "friendReq"
    friendDetail = "friendDetail"
    createGroupBtn = "createGroupBtn"
    saveGroupBtn = "saveGroupBtn"
    showSelectPersonModelBtn = "showSelectPersonModelBtn"
    groupDetail = "groupDetail"
    deleteGroupBtn = "deleteGroupBtn"
    editGroupBtn = "editGroupBtn"
    taskBtn = "taskBtn"
    createTask = "createTask"
    toService = "toService"
    saveTaskBtn = "saveTaskBtn"
    viewTask1840 = "viewTask1840"
    viewTaskBtn1836 = "viewTaskBtn1836"
    deteleTaskBtn = "deteleTaskBtn"
    rewardTaskBtn = "rewardTaskBtn"
    editTaskBtn = "editTaskBtn"
    viewTask = "viewTask"
    setTaskFinishBtn = "setTaskFinishBtn"
    setTaskNotFinishBtn = "setTaskNotFinishBtn"
    SubmitAddMeetingBtn = "SubmitAddMeetingBtn"
    toAddScheduleBtn = "toAddScheduleBtn"
    submitAddScheduleBtn = "submitAddScheduleBtn"
    updateScheduleBtn = "updateScheduleBtn"
    deleteScheduleBtn = "deleteScheduleBtn"
    addMeetingBtn = "addMeetingBtn"
    SubmitAddMeetingBtn = "SubmitAddMeetingBtn"
    openCancelModelBtn = "openCancelModelBtn"
    addPersonBtn = "addPersonBtn"
    editMeetingBtn = "editMeetingBtn"
    cancelMeetingBtn = "cancelMeetingBtn"
    signMeetingBtn = "signMeetingBtn"
    attendBtn = "attendBtn"
    notAttendBtn = "notAttendBtn"
    attendModelOkBtn = "attendModelOkBtn"
    deleteMeetingBtn = "deleteMeetingBtn"
    agreement = "agreement"
    to = "to"
    cc = "cc"
    sendMailBtn = "sendMailBtn"
    saveMailBtn = "saveMailBtn"
    batchDelMailBtn = "batchDelMailBtn"
    batchRestoreMailBtn = "batchRestoreMailBtn"
    clearMailBtn = "clearMailBtn"
    mailReplayBtn = "mailReplayBtn"
    mailReplayAllBtn = "mailReplayAllBtn"
    mailForwardBtn = "mailForwardBtn"
    mailDeleteBtn = "mailDeleteBtn"
    diskBtn = "diskBtn"
    saveMailOkBtn = "saveMailOkBtn"
    saveMailCancelBtn = "saveMailCancelBtn"
    saveMailCloseBtn = "saveMailCloseBtn"
    mailReEditBtn = "mailReEditBtn"
    mailForwardBtn = "mailForwardBtn"
    mailDeleteBtn = "mailDeleteBtn"
    todoBtn = "todoBtn"
    getCodeFormCodeBtn = "getCodeFormCodeBtn"
    codeFormNextBtn = "codeFormNextBtn"
    toMarket = "toMarket"


class Interface_con:
    public_key = "https://api.cnhqd.net/userManager/userInfo/publickey"
    client_login = "https://api.cnhqd.net/userManager/userInfo/login"
    protal_login = "https://api.cnhqd.net/userManager/backendlogin/login"




