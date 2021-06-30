import yaml


def get_data():
    with open("/Users/yeahmobi/Desktop/work/python/wechart/wechart/data/Address_management_data/member_management.yaml", 'r') as f:
        datas = yaml.safe_load(f)
        #创建成员
        creat_member = datas['creat_member']
        ids = datas['ids']
        #获取成员
        get_user = datas['get_user']
        idsu = datas['idsu']
        #更新成员
        updata_user = datas['updata_user']
        idsup = datas['idsup']
        # 删除成员
        delete_user = datas['delete_user']
        idsde = datas['idsde']
        # 批量删除成员-useridlist参数为空
        batch_delete_user = datas['batch_delete_user']
        ids_batch_delete_user = datas['ids_batch_delete_user']
        #获取部门成员
        get_department_user = datas['get_department_user']
        ids_get_department_user = datas['ids_get_department_user']
        #获取部门成员详情
        get_department_userlist = datas['get_department_userlist']
        ids_get_department_userlist = datas['ids_get_department_userlist']
        #userid与openid互换
        convert_to_openid = datas['convert_to_openid']
        ids_convert_to_openid = datas['ids_convert_to_openid']
        #二次验证
        second_confirm = datas['second_confirm']
        ids_second_confirm = datas['ids_second_confirm']
        #邀请成员
        invite_user = datas['invite_user']
        ids_invite_user = datas['ids_invite_user']
        ## 获取加入企业二维码
        get_join_qrcode = datas['get_join_qrcode']
        ids_get_join_qrcode = datas['ids_get_join_qrcode']
        #获取企业活跃成员数
        get_active_stat = datas['get_active_stat']
        ids_get_active_stat = datas['ids_get_active_stat']



    return [creat_member,ids,  #0,1
            get_user,idsu, #2,3
            updata_user,idsup,#4,5
            delete_user,idsde,#6,7
            batch_delete_user,ids_batch_delete_user, #8,9
            get_department_user,ids_get_department_user,#10,11
            get_department_userlist,ids_get_department_userlist,#12,13
            convert_to_openid,ids_convert_to_openid,#14,15
            second_confirm,ids_second_confirm,#16,17
            invite_user,ids_invite_user,#18,19
            get_join_qrcode,ids_get_join_qrcode,#20,21
            get_active_stat,ids_get_active_stat]



