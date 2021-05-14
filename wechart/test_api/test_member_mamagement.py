from wechart.Address_management.member_management import DepartmentManagement
import pytest

class TestAddressManagement():

    def setup(self):
        self.main = DepartmentManagement()

    def teardown(self):
        pass

    @pytest.mark.parametrize("userid,name,mobile,department",[("zhangsan",'三儿','136787804403',[1])])
    def test_creat_member(self,userid,name,mobile,department):
        #清楚数据
        self.main.delete_user(userid)
        #添加成员
        result = self.main.create_member(userid,name,mobile,department)
        assert result.get('errmsg','创建失败') == 'created'

