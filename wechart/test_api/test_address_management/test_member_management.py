
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



