from selenium.webdriver.common.by import By
from PageObjects.ConfirmPage import ConfirmPage
# Home Page Objects
""""
Card page related element will store here and will use by the inheritance method"""""

class CardPage:

    # we have to create the constructor to access the driver
    def __init__(self, driver):
        self.driver = driver

    """Card is class variable"""
    card = (By.XPATH, "//div[@class='card h-100']")
    addTocart = (By.XPATH, "(//button[@class='btn btn-info'])[4]")
    checkOutele = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    """ will bring the shop element in below given method """
    def cardItems(self):

        return self.driver.find_elements(*CardPage.card)

    def addTocardEle(self):
        return self.driver.find_element(*CardPage.addTocart)

    def CheckOutEle(self):
        self.driver.find_element(*CardPage.checkOutele).click()
        Confirm_Page = ConfirmPage(self.driver).ConfirmEle()
        return Confirm_Page
