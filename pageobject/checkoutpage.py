from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self,driver):
        self.driver = driver

    check_obj = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    products_obj = (By.CLASS_NAME, 'card h-100')
    product_name = (By.XPATH, "div/h4/a")
    product_obj = (By.XPATH, 'div/button')


    def checkout(self):
        products = self.driver.find_elements(*CheckOutPage.products_obj)

        for product in products:
            product_name = product.find_element(*CheckOutPage.product_name).text
            if product_name == 'Blackberry':
                product.find_element(*CheckOutPage.product_obj).click()
                break
        return  self.driver.find_element(*CheckOutPage.check_obj)