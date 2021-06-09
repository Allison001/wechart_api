import yaml


def get_department_data():
    with open("/Users/yeahmobi/Desktop/work/python/wechart/wechart/data/Address_management_data/department_management.yaml",'r') as f:
        datas = yaml.safe_load(f)

        data_creat = datas['creat_department']
        ids_creat = datas['idscreat']

        updata_department = datas['updata_department']
        ids_up = datas['ids_up']

        delete_data = datas['delete_data']
        ids_dele = datas['ids_delete']

        return [data_creat,ids_creat,updata_department,ids_up,delete_data,ids_dele]

# a = get_department_data()[0]
# print(a)