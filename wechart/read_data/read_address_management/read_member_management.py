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


    return [creat_member,ids,  #0,1
            get_user,idsu, #2,3
            updata_user,idsup,
            delete_user,idsde,
            batch_delete_user,ids_batch_delete_user, #8,9
            get_department_user,ids_get_department_user]



