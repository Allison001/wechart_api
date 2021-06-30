from wechart.api_page.Address_management.base_page import BasePage

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

    #批量删除成员
    def batch_delete_user(self,useridlist):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/batchdelete'
        body = {"useridlist": useridlist}
        r = self.req('post',url,json=body)
        return r.json()

    #获取部门成员
    def get_department_user(self,department_id,fetch_child):
        '''
        :param department_id:  int 获取的部门id
        :param fetch_child: 是否递归获取子部门下面的成员：1-递归获取，0-只获取本部门
        :return:
        '''
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/simplelist?department_id={department_id}&fetch_child={fetch_child}'
        r = self.req('get',url)
        return r.json()

    #获取部门成员详情
    def get_department_userlist(self,department_id,fetch_child):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/list?department_id={department_id}&fetch_child={fetch_child}'
        r = self.req('get',url)
        return r.json()

    #userid与openid互换
    def convert_to_openid(self,userid):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/convert_to_openid'
        body = {"userid": userid}
        r = self.req('post',url,json=body)
        return r.json()


    #二次验证
    def second_confirm(self,userid):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/authsucc?userid={userid}'
        r = self.req('get',url)
        return r.json()

    #邀请成员
    def invite_user(self,user,party,tag):
        '''
        :param user: list 成员ID列表, 最多支持1000个。
        :param party: list 部门ID列表，最多支持100个。
        :param tag: list  标签ID列表，最多支持100个。
        :return:
        '''
        url = 'https://qyapi.weixin.qq.com/cgi-bin/batch/invite'
        body = {
               "user" : {user},
               "party" : {party},
               "tag" : {tag}}
        r = self.req('post',url,json=body)
        return r.json()


    #获取加入企业二维码
    def get_join_qrcode(self,size_type):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/corp/get_join_qrcode?size_type={size_type}'
        r = self.req('get',url)


    #获取企业活跃成员数
    def get_active_stat(self,date):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/get_active_stat'
        body ={"date": date}
        r = self.req('post',url,json=body)
        return r.json()



