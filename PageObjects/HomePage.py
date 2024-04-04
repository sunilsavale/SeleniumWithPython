from selenium.webdriver.common.by import By
from PageObjects.CheckOutPage import CardPage
# Home Page Objects
""""
Home page related element will store here and will use by the inheritance method"""""

class HomePage:

    # we have to create the constructor to access the driver
    def __init__(self, driver):
        self.driver = driver

    """shop is class variable"""
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    """form related web elements"""
    name_ele = (By.NAME, 'name')
    email_ele = (By.NAME, 'email')
    password_ele = (By.ID, 'exampleInputPassword1')
    ice_cream = (By.ID, 'exampleCheck1')
    gender_ele = (By.ID, 'exampleFormControlSelect1')
    select_gender = (By.XPATH, "//select[@id='exampleFormControlSelect1']")

    radio_button = (By.ID, 'inlineRadio1')
    birth_day = (By.NAME, 'bday')
    submit_button = (By.XPATH, "//input[contains(@value,'Submit')]")
    alert_text = (By.XPATH, "//div[contains(@class,'alert alert-success')]")


    """ will bring the shop element in below given method """
    def shopItems(self):
        self. driver.find_element(*HomePage.shop).click()
        products = CardPage(self.driver).cardItems()
        return products

    def NameEle(self):
        return self.driver.find_element(*HomePage.name_ele)

    def EmailEle(self):
        return self.driver.find_element(*HomePage.email_ele)

    def PasswordEle(self):
        return self.driver.find_element(*HomePage.password_ele)

    def IceCreamEle(self):
        return self.driver.find_element(*HomePage.ice_cream)

    def GenderEle(self):
        return self.driver.find_element(*HomePage.gender_ele)

    def RadiOEle(self):
        return self.driver.find_element(*HomePage.radio_button)

    def BdayEle(self):
        return self.driver.find_element(*HomePage.birth_day)

    def SubmittButton(self):
        return self.driver.find_element(*HomePage.submit_button)