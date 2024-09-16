
from selenium.webdriver.common.by import By


from BaseClass.baseclass import BaseClass
from pageobject.HomePage import HomePage

from pageobject.checkoutpage2 import CheckOutPage2


#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    # def test_end2end(self):
    #
    #     self.driver.find_element(By.XPATH, "//a[text()='Shop']").click()
    #     self.driver.maximize_window()
    #     products = self.driver.find_elements(By.CLASS_NAME, 'card h-100')
    #
    #
    #
    #     for product in products:
    #         product_name = product.find_element(By.XPATH, "div/h4/a").text
    #         if product_name == 'Blackberry':
    #             product.find_element(By.XPATH, 'div/button').click()
    #             break
    #
    #     self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
    #     self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
    #
    #     self.driver.find_element(By.ID, 'country').send_keys('ind')
    #
    #     wait = WebDriverWait(self.driver, 7)
    #     wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
    #     self.driver.find_element(By.LINK_TEXT, 'India').click()
    #     self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    #     self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
    #
    #     text = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
    #     assert "Success! Thank you!" in text
    #     print(text)
    #     print('new test done')

    def test_end2end(self):
        log = self.getLogger()

        homepage = HomePage(self.driver)
        homepage.shopitem()
        checkout2 = CheckOutPage2(self.driver)
        checkout2.checkout2()

        text = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
        log.info(text)
        assert "Success! Thank you!" in text




