

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import logging
import inspect
"""I will call the fixture from conftest"""
@pytest.mark.usefixtures("setup")
class TestBaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logsfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.INFO)
        return logger

    # def GetLoggerDetaila(self):
    #     loggerName = inspect.stack()[1][3]
    #     # logger = logging.getLogger(__name__)
    #     logger = logging.getLogger(loggerName)
    #     fileHandle = logging.FileHandler('D://Restart_Selenium with Python//FrameworkPythonSelenium//Logs//Logifile.log')
    #
    #     """Store in variabel to make connection between filehandler and Formatter Method"""
    #     Logging_formate = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
    #     logger.addHandler(fileHandle)
    #     fileHandle.setFormatter(Logging_formate)
    #
    #     # logger.setLevel(logging.INFO)
    #     logger.setLevel(logging.DEBUG)
    #     # logger.debug('To print the debug message')
    #     # logger.info('To print the information related to test cases')
    #     # logger.warning('To give a warning message to particular test case')
    #     # logger.error('To print assertion error')
    #     # logger.critical("To critical test cases")
    #
    #     """We have to set level"""
    #     return logger

    def VerifyingEle(self, text):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.LINK_TEXT, text)))
        element.click()

    def GenDerSelect(self, xpath):
        wait = WebDriverWait(self.driver, 10)
        select_gender = wait.until(ec.presence_of_element_located(
            (By.XPATH, xpath)))
        Male_Gender = Select(select_gender)
        Male_Gender.select_by_visible_text('Male')