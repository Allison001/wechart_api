
from wechart.api_page.Address_management.member_management import DepartmentManagement

import pytest

from wechart.read_data.read_address_management.read_member_management import get_data

#测试通讯录管理->成员管理
class TestAddressManagement():

    def setup(self):
        self.main = DepartmentManagement()

    def teardown(self):
        pass

    #添加成员
    @pytest.mark.parametrize("userid,name,mobile,department",get_data()[0],ids=get_data()[1])
    def test_creat_member(self,userid,name,mobile,department):
        #清除数据
        self.main.delete_user(userid)
        #添加成员
        result = self.main.create_member(userid,name,mobile,department)
        assert result.get('errmsg','创建失败') == 'created'

    #读取成员
    @pytest.mark.parametrize('userid,name',get_data()[2],ids=get_data()[3])
    def test_get_user(self,userid,name):
        #直接读取成员
        result = self.main.get_uesr(userid)
        print(result)
        assert result.get('name','读取成员错误') == name

    #更新成员
    @pytest.mark.parametrize('userid,name,mobile,department,position',get_data()[4],ids=get_data()[5])
    def test_updata_user(self,userid,name,mobile,department,position):
        #读取成员是否存在
        result = self.main.get_uesr(userid)
        assert result.get('errmsg','成员不存在') =='ok'

        #更新成员
        result1 = self.main.updata_user(userid,name,mobile,department,position=position)
        print(result1)
        assert result1.get("errmsg",'更新失败') == 'updated'


    #删除成员
    @pytest.mark.parametrize("userid",get_data()[6],ids=get_data()[7])
    def test_delete_user(self,userid):
        #查询成员是否存在
        result1 = self.main.get_uesr(userid)
        assert result1.get("errmsg",'成员不存在') == 'ok'
        #删除成员
        result = self.main.delete_user(userid)
        assert result.get("errmsg",'删除失败') == 'deleted'


    # 批量删除成员---删除的useridlist参数为空
    @pytest.mark.parametrize('userid,name,mobile,department,useridlist,expect',get_data()[8],ids=get_data()[9])
    def test_batch_delete_user(self,userid,name,mobile,department,useridlist,expect):
        #一、先创建成员
        a = self.main.create_member(userid,name,mobile,department)
        print(a)
        #二、再删除成员
        result = self.main.batch_delete_user(useridlist)
        print(result)
        assert result['errcode'] == expect

    # 获取部门成员
    @pytest.mark.parametrize('department_id,fetch_child,ecpect',get_data()[10],ids=get_data()[11])
    def test_get_department_user(self,department_id,fetch_child,ecpect):
        result = self.main.get_department_user(department_id,fetch_child)
        assert result['errmsg'] == ecpect
        print(result)

    # 获取部门成员详情
    @pytest.mark.parametrize('department_id,fetch_child,expect',get_data()[12],ids=get_data()[13])
    def test_get_department_userlist(self,department_id,fetch_child,expect):
        result = self.main.get_department_userlist(department_id,fetch_child)
        print(result)
        assert result['errmsg'] == expect

    # userid与openid互换
    @pytest.mark.parametrize("userid,expect",get_data()[14],ids=get_data()[15])
    def test_convert_to_openid(self,userid,expect):
        result = self.main.convert_to_openid(userid)
        print(result)
        assert result['errcode'] == expect

    # 二次验证
    @pytest.mark.parametrize('userid,expect',get_data()[16],ids=get_data()[17])
    def test_second_confirm(self,userid,expect):
        result = self.main.second_confirm(userid)
        print(result)
        assert result['errcode'] == expect

    # 邀请成员
    @pytest.mark.parametrize('user,party,tag,expect',get_data()[18],ids=get_data()[19])
    def test_invite_user(self,user,party,tag,expect):
        result = self.main.invite_user(user,party,tag)
        print(result)
        assert result['errcode'] == expect

    # 获取加入企业二维码
    @pytest.mark.parametrize('size_type,expect',get_data()[20],ids=get_data()[21])
    def test_get_join_qrcode(self,size_type,expect):
        result = self.main.get_join_qrcode(size_type)
        print(result)
        assert result['errcode'] == expect

    # 获取企业活跃成员数
    @pytest.mark.parametrize('date,expect',get_data()[22],ids=get_data()[23])
    def test_get_active_stat(self,date,expect):
        result = self.main.get_active_stat(date)
        print(result)
        assert result['errcode'] == expect


