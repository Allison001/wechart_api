from wechart.Address_management.base_page import BasePage


class DepartmentManagement(BasePage):

    def creat_department(self):
        url ='https://qyapi.weixin.qq.com/cgi-bin/department/create'
        body = {
            "name": "广州研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1,
            "id": 2}
        r = self.req("post",url,json=body)
        return r.json()