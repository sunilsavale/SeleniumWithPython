from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# Confirm Page Objects
""""
Confirm page related element will store here and will use by the inheritance method"""""

class ConfirmPage:

    """Confirm page element"""
    confirm_ele = (By.XPATH, "//button[@class='btn btn-success']")
    conuntry_ele = (By.ID, "country")
    india_ele = (By.LINK_TEXT, "India")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit_ele = (By.CSS_SELECTOR, "[type='submit']")

    def __init__(self, driver):
        self.driver = driver


    def ConfirmEle(self):
        self.driver.find_element(*ConfirmPage.confirm_ele).click()

    def CountryEle(self):
        return self.driver.find_element(*ConfirmPage.conuntry_ele)

    def IndiaEle(self):
        # wait = WebDriverWait(self.driver, 10)
        return self.driver.find_element(*ConfirmPage.india_ele)

    def CheckBoxEle(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def SubmitEle(self):
        return self.driver.find_element(*ConfirmPage.submit_ele)

