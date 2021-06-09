from wechart.api_page.Address_management.base_page import BasePage


'''
通讯录管理->部门管理
'''

class DepartmentManagement(BasePage):

    #创建部门
    def creat_department(self,name,name_en,parentid,order,id):
        url ='https://qyapi.weixin.qq.com/cgi-bin/department/create'
        body = {
            "name": name,
            "name_en": name_en,
            "parentid": parentid,
            "order": order,
            "id": id}
        r = self.req("post",url,json=body)
        return r.json()


    #更新部门
    def updata_department(self,id,name,name_en,parentid,order):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/update'
        body = {
           "id": id,
           "name": name,
           "name_en": name_en,
           "parentid": parentid,
           "order": order}
        r = self.req('post',url,json=body)
        return r.json()


    #删除部分
    def delete_department(self,id):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?id={id}'
        r = self.req("get",url)
        return r.json()


    #获取部门列表
    def get_department_list(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list?id=ID'
        r = self.req('get',url)
        return r.json()

a = DepartmentManagement().updata_department(2,"广州研发部门","RDGZ",1,1)
print(a)