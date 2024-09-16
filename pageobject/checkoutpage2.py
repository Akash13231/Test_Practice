from selenium.webdriver.common.by import By

from pageobject.purchasepage import Purchase


class CheckOutPage2:

    def __init__(self, driver):
        self.driver = driver

    check_obj2 = (By.XPATH, "//button[@class='btn btn-success']")

    def checkout2(self):
        self.driver.find_element(*CheckOutPage2.check_obj2).click()
        purchase = Purchase(self.driver)
        return purchase.purchase_page().click()
