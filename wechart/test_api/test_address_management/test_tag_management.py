import pytest
from wechart.api_page.Address_management.tag_management import TagManagement
from wechart.read_data.read_address_management.read_tag_management import read_create_tag, updata_tag_name, delete_tag, \
    get_tag_user, add_tag_user, delete_tag_user


class Test_Tag_Management():
    # 通讯录管理->标签管理
    def setup(self):
        self.main = TagManagement()

    def teardown(self):
        pass

    #创建标签接口-成功
    @pytest.mark.parametrize('tagname,tagid',read_create_tag()[0],ids=read_create_tag()[1])
    def test_create_tag(self,tagname,tagid):
        #删除标签
        self.main.delecte_tag(tagid)

        #新建标签
        result = self.main.create_tag(tagname,tagid)
        # print(result)
        assert result['errmsg'] == 'created'

    #创建标签接口-已存在的名称
    @pytest.mark.parametrize('tagname,tagid',read_create_tag()[2])
    def test_create_tag_fail1(self,tagname,tagid):
        #新建标签
        result = self.main.create_tag(tagname,tagid)
        print(result)
        assert result['errcode'] == 40071  #标签名字已经存在


    #创建标签接口-已存的ID
    @pytest.mark.parametrize('tagname,tagid',read_create_tag()[3])
    def test_create_tag_fail2(self,tagname,tagid):
        #新建标签
        result = self.main.create_tag(tagname,tagid)
        print(result)
        assert result['errcode'] == 40068  #标签ID未指定，或者指定的标签ID不存在

    #更新标签名字
    @pytest.mark.parametrize('tagid,tagname',updata_tag_name()[0],ids=updata_tag_name()[1])
    def test_update_tag_name(self,tagid,tagname):
        result = self.main.update_tag_name(tagid,tagname)
        print(result)
        assert result['errmsg'] == 'updated'

    #删除标签-已存在的标签
    @pytest.mark.parametrize('tagid',delete_tag()[0],ids=delete_tag()[1])
    def test_delete_tag(self,tagid):
        result = self.main.delecte_tag(tagid)
        print(result)
        assert result['errmsg'] == 'deleted'

    #获取标签成员
    @pytest.mark.parametrize('tagname,tagid',get_tag_user()[0],ids=get_tag_user()[1])
    def test_get_tag(self,tagname,tagid):
        #先创建标签
        self.main.create_tag(tagname,tagid)
        #再获取标签成员
        result = self.main.get_tag_user(tagid)
        print(result)
        assert result['errmsg'] == 'ok'

    #增加标签成员
    @pytest.mark.parametrize('tagid,userlist,partylist',add_tag_user()[0],ids=add_tag_user()[1])
    def test_add_tag_user(self,tagid,userlist,partylist):
        result = self.main.add_tag_user(tagid,userlist,partylist)
        print(result)
        assert result['errmsg'] =='ok'


    #删除标签成员
    @pytest.mark.parametrize("tagid,userlist,partylist",delete_tag_user()[0],ids=delete_tag_user()[1])
    def test_delete_tag_user(self,tagid,userlist,partylist):
        #先新增加标签成员
        self.main.add_tag_user(tagid,userlist,partylist)
        #再删除标签成员
        result = self.main.delete_tag_user(tagid,userlist,partylist)
        print(result)
        assert result['errmsg'] == 'deleted'

    #获取标签列表
    def test_get_tag_list(self):
        result = self.main.get_tag_list()
        print(result)
        assert result['errmsg'] == 'ok'




