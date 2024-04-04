# To Cofirm the text once successfull add the items
from selenium.webdriver.common.by import By

# Confirm Page Objects
""""
Success page related element will store here and will use by the inheritance method"""""

class SuccessPageClass:

    success_text = (By.CLASS_NAME, "alert-success")
    def __init__(self, driver):
        self.driver = driver

    def SuccessTextCapture(self):
        return self.driver.find_element(*SuccessPageClass.success_text)
