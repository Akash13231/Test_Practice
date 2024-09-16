import pytest

from selenium.webdriver.support.select import Select

from BaseClass.baseclass import BaseClass


from TestData.HomePageData import HomePageData
from pageobject.HomePage1 import HomePage1


class Test_FormFilling(BaseClass):


    def test_form_sublission(self, getData):
        log = self.getLogger()

        homepage1 = HomePage1(self.driver)
        homepage1.fill_name().send_keys(getData["firstname"])
        homepage1.fill_elail().send_keys(getData['email'])
        homepage1.check().click()
        sel= Select(homepage1.fill_gender())
        sel.select_by_visible_text(getData['gender'])
        homepage1.submit().click()


        alert_text = homepage1.sucess().text
        assert ('Success' in alert_text)
        log.info(alert_text)
        self.driver.refresh()


    #NOTE - Here fixture is given because we want to use it for specific for this class only

    # @pytest.fixture(params=[{'firstname': 'akash', 'email': 'abc@gmail.com', 'gender': 'Male'},
    #                         {'firstname': 'Tejashvini', 'email': 'abc@gmail.com', 'gender': 'Female'}])   #in this function test data is given in the test file
    # def getData(self, request):
    #     return request.param

    # @pytest.fixture(params = HomePageData.test_HomePage_data)  #this is used to store data into another file and imported here using the class name
    # def getData(self, request):
    #     return request.param

    @pytest.fixture(
        params=HomePageData.get_exceldata('testcase1'))
    def getData(self, request):
        return request.param