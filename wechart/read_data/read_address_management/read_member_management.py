import yaml


def get_data():
    with open("/Users/yeahmobi/Desktop/work/python/wechart/wechart/data/Address_management_data/member_management.yaml", 'r') as f:
        datas = yaml.safe_load(f)

        creat_member = datas['creat_member']
        ids = datas['ids']

        get_user = datas['get_user']
        idsu = datas['idsu']

        updata_user = datas['updata_user']
        idsup = datas['idsup']

        delete_user = datas['delete_user']
        idsde = datas['idsde']

    return [creat_member,ids,get_user,idsu,updata_user,idsup,delete_user,idsde]
