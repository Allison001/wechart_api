import yaml



#读取创建标签
def read_create_tag():
    with open("/Users/yeahmobi/Desktop/work/python/wechart/wechart/data/Address_management_data/tag_management.yaml") as f:
        a = yaml.safe_load(f)

        date = a['tag']
        ids = a["ids"]
        date_tag_have = a['tag_have']
        date_tag_id = a["tag_id_have"]


    return [date, #0
            ids, #1
            date_tag_have,#2
            date_tag_id]

#读取更新标签名字
def updata_tag_name():
    with open("/Users/yeahmobi/Desktop/work/python/wechart/wechart/data/Address_management_data/tag_management.yaml") as f:
        a = yaml.safe_load(f)

        #更新标签名字
        update_tag_name = a['update_tag_name']
        ids_update_tag = a['ids_update_tag']

    return [update_tag_name,ids_update_tag]

#删除标签
def delete_tag():
    with open("/Users/yeahmobi/Desktop/work/python/wechart/wechart/data/Address_management_data/tag_management.yaml") as f:
        a = yaml.safe_load(f)

        delete_tag = a['delete_tag']
        ids_delete_tag = a['ids_delete_tag']

    return [delete_tag,ids_delete_tag]

# 获取标签成员
def get_tag_user():
    with open("/Users/yeahmobi/Desktop/work/python/wechart/wechart/data/Address_management_data/tag_management.yaml") as f:
        a = yaml.safe_load(f)

        get_tag_user = a['get_tag_user']
        ids_get_tag_user = a['ids_get_tag_user']

    return [get_tag_user, ids_get_tag_user]


#增加标签成员
def add_tag_user():
    with open("/Users/yeahmobi/Desktop/work/python/wechart/wechart/data/Address_management_data/tag_management.yaml") as f:
        a = yaml.safe_load(f)

        add_tag_user = a['add_tag_user']
        ids_add_tag_user = a['ids_add_tag_user']

    return [add_tag_user,ids_add_tag_user]

#删除成员标签
def delete_tag_user():
    with open("/Users/yeahmobi/Desktop/work/python/wechart/wechart/data/Address_management_data/tag_management.yaml") as f:
        a = yaml.safe_load(f)

        delete_tag_user = a['delete_tag_user']
        ids_delete_tag_user = a['ids_add_tag_user']

    return [delete_tag_user,ids_delete_tag_user]


a = get_tag_user()
print(a)