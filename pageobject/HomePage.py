from selenium.webdriver.common.by import By

from pageobject.checkoutpage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    obj= (By.XPATH, "//a[text()='Shop']")


    def shopitem(self):
       self.driver.find_element(*HomePage.obj).click()
       checkout = CheckOutPage(self.driver)
       return checkout.checkout().click()


