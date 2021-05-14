import requests
from wechart.Address_management.base_page import BasePage

"""
通讯录管理->成员管理
"""

class DepartmentManagement(BasePage):

    # def __init__(self):
    #     url = " https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww2347fac9c4a29960&corpsecret=ODMt674VxHnSwe_82JNrm75CWituEFsbSg9saVD57rs"
    #     r = requests.get(url)
    #     self.token = r.json()['access_token']


    #创建成员
    def create_member(self,userid:str,name:str,mobile:str,department:list,**kwargs):
        # url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}'
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        body = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department}
        body.update(kwargs)

        # r = self.r.post(url,json=body)
        r = self.req("post",url,json=body)
        return r.json()


    #读取成员
    def get_uesr(self,userid):
        # url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}'
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userid}'
        # r = self.r.get(url)
        r = self.req("get",url)
        return r.json()

    #更新成员
    def updata_user(self,userid,name,mobile,department:list,**kwargs):
        # url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}'
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        body = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department}
        body.update(kwargs)
        # r = self.r.post(url,json=body)
        r = self.req("post",url,json=body)
        return r.json()

    #删除成员
    def delete_user(self,userid):
        # url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}'
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={userid}'
        # r = self.r.get(url)
        r = self.req("get",url)
        return r.json()


