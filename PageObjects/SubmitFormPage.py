# SubmitForm Page Objects
""""
SubmitForm related element will store here and will use by the inheritance method"""""
from selenium.webdriver.common.by import By


class SubmitFormEle:

    # We have to create the constructor to access the driver
    def __init__(self, driver):
        self.driver = driver

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

    """ will bring the all web element in below given method """

    def NameEle(self):
        return self.driver.find_element(*SubmitFormEle.name_ele)

    def EmailEle(self):
        return self.driver.find_element(*SubmitFormEle.email_ele)

    def PasswordEle(self):
        return self.driver.find_element(*SubmitFormEle.password_ele)

    def IceCreamEle(self):
        return self.driver.find_element(*SubmitFormEle.ice_cream)

    def GenderEle(self):
        return self.driver.find_element(*SubmitFormEle.gender_ele)

    def RadiOEle(self):
        return self.driver.find_element(*SubmitFormEle.radio_button)

    def BdayEle(self):
        return self.driver.find_element(*SubmitFormEle.birth_day)

    def SubmittButton(self):
        return self.driver.find_element(*SubmitFormEle.submit_button)