from wechart.api_page.Address_management.base_page import BasePage


class TagManagement(BasePage):
    #通讯录管理->标签管理

    #创建标签
    def create_tag(self,tagname:str,tagid:int):
        url ='https://qyapi.weixin.qq.com/cgi-bin/tag/create'
        body = {
           "tagname": tagname,
           "tagid": tagid
        }
        r = self.req("post",url,json=body)
        return r.json()


    #更新标签名字
    def update_tag_name(self,tagid,tagname):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/update'
        body = {
           "tagid": tagid,
           "tagname": tagname}
        r = self.req("post",url,json=body)
        return r.json()

    #删除标签
    def delecte_tag(self,tagid):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/tag/delete?tagid={tagid}'
        r = self.req("get",url)
        return r.json()

    # 获取标签成员
    def get_tag_user(self,tagid):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/tag/get?tagid={tagid}'
        r = self.req("get",url)
        return r.json()

    # 增加标签成员
    def add_tag_user(self,tagid,userlist,partylist):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers'
        body = {
               "tagid": tagid,
               "userlist":userlist,
               "partylist": partylist
            }
        r = self.req("post",url,json=body)
        return r.json()

    # 删除标签成员
    def delete_tag_user(self,tagid,userlist:list,partylist:list):
        '''
        :param tagid: int  标签ID
        :param userlist: list 企业成员ID列表
        :param partylist: list  企业部门ID列表
        :return:
        '''
        url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers'
        body = {
               "tagid": tagid,
               "userlist":userlist,
               "partylist": partylist
            }
        r = self.req("post",url,json=body)
        return r.json()

    # 获取标签列表
    def get_tag_list(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/list'
        r = self.req("get",url)
        return r.json()

A = TagManagement().get_tag_list()
print(A)

