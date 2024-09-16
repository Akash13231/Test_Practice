from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from BaseClass.baseclass import BaseClass


class Purchase(BaseClass):
    def __init__(self, driver):
         self.driver = driver

    purchase_obj = ((By.ID, 'country'), (By.LINK_TEXT, "India"), (By.LINK_TEXT, 'India'), (By.XPATH, "//div[@class='checkbox checkbox-primary']"), (By.XPATH, "//input[@type='submit']"))


    def purchase_page(self):
        self.driver.find_element(*Purchase.purchase_obj[0]).send_keys('ind')
        self.waitmechanism('India')
        self.driver.find_element(*Purchase.purchase_obj[2]).click()
        self.driver.find_element(*Purchase.purchase_obj[3]).click()
        return self.driver.find_element(*Purchase.purchase_obj[4])



