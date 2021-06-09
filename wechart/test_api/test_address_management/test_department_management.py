import pytest

from wechart.api_page.Address_management.department_management import DepartmentManagement
from wechart.read_data.read_address_management.read_department_management import get_department_data

#测试通讯录管理->部门管理
class TestDepartMentManagement():

    def setup(self):
        self.dpm = DepartmentManagement()
    def teardown(self):
        pass

    #创建部门接口
    @pytest.mark.parametrize("name,name_en,parentid,order,id",get_department_data()[0],ids=get_department_data()[1])
    def test_creat_department(self,name,name_en,parentid,order,id):
        #清除部门数据
        self.dpm.delete_department(id)

        #创建部门
        result = self.dpm.creat_department(name,name_en,parentid,order,id)
        assert result.get('errmsg','创建失败') == 'created'


    #更新部门接口
    @pytest.mark.parametrize("id,name,name_en,parentid,order",get_department_data()[2],ids=get_department_data()[3])
    def test_updata_department(self,id,name,name_en,parentid,order):
        result = self.dpm.updata_department(id,name,name_en,parentid,order)
        assert result.get("errmsg","更新失败") =='updated'

    #删除部门接口
    @pytest.mark.parametrize("id",get_department_data()[4],ids=get_department_data()[5])
    def test_delete_department(self,id):
        result = self.dpm.delete_department(id)
        # print(result)
        result1 = result["errcode"]
        print(result1)

        if result1 == 60006:
            print('部门下存在子部门')
        elif result1 == 0:
            assert result.get("errmsg",'删除失败') == 'deleted'
            print('删除成功')


    #获取部门列表接口
    def test_get_department_list(self):
        result = self.dpm.get_department_list()
        print(result)
        assert result.get("errmsg","获取失败") == 'ok'




