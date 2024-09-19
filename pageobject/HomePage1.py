from selenium.webdriver.common.by import By


class HomePage1():

    def __init__(self, driver):
        self.driver = driver

    name = (By.NAME, 'name')
    email = (By.NAME, 'email')
    passw = (By.ID, 'exampleInputPassword1')
    checkbox = (By.ID, 'exampleCheck1')
    gender = (By.ID,'exampleFormControlSelect1')
    submit_button = (By.XPATH, "//input[@value='Submit']")
    dob = (By.NAME, 'bday')
    succ = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def fill_name(self):
        return self.driver.find_element(*HomePage1.name)

    def fill_elail(self):
        return self.driver.find_element(*HomePage1.email)

    def fill_pass(self):
        return self.driver.find_element(*HomePage1.passw)

    def check(self):
        return self.driver.find_element(*HomePage1.checkbox)

    def fill_gender(self):
        return self.driver.find_element(*HomePage1.gender)

    def birth_date(self):
        return self.driver.find_element(*HomePage1.dob)

    def submit(self):
        return self.driver.find_element(*HomePage1.submit_button)

    def sucess(self):
        return self.driver.find_element(*HomePage1.succ)





