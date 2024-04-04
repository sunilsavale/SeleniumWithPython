from selenium.webdriver.common.by import By

# Submit Button Page
# from PageObjects.SubmitFormPage import SubmitFormEle
#
#
# class TestSubmitButton:
#     def __init__(self, driver):
#         self.driver = driver
#
#     radio_button = (By.ID, 'inlineRadio1')
#     birth_day = (By.NAME, 'bday')
#     submit_button = (By.XPATH, "//input[contains(@value,'Submit')]")
#     alert_text = (By.XPATH, "//div[contains(@class,'alert alert-success')]")
#
#     def RadiOEle(self):
#         return self.driver.find_element(*TestSubmitButton.radio_button)
#
#     def BdayEle(self):
#         return self.driver.find_element(*TestSubmitButton.birth_day)
#
#     def SubmittButton(self):
#         return self.driver.find_element(*TestSubmitButton.submit_button)