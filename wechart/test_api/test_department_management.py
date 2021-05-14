from wechart.Address_management.department_management import DepartmentManagement


class TestDepartMentManagement():

    def setup(self):
        self.dpm = DepartmentManagement()
    def teardown(self):
        pass

    def test_creat_department(self):
        result = self.dpm.creat_department()
        assert result.get('errmsg','创建失败') == 'created'