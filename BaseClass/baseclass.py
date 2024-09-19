import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import inspect
import logging

@pytest.mark.usefixtures("setup")
class BaseClass:
    def waitmechanism(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_all_elements_located((By.LINK_TEXT, text)))


    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler('C:/Users/abhosage/PycharmProjects/Testing/pythonProject2/pythonProject/reports/logfile.log')
        formater = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formater)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger