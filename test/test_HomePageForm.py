import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# from utilities.Baseclass2 import TestFormSubmission
# from PageObjects.SubmitFormPage import SubmitFormEle
# from PageObjects.SubmitPageFormLastStep import TestSubmitButton
from PageObjects.HomePage import HomePage
from utilities.BaseClass import TestBaseClass
from TestData.TestData import FormPageTestData


class TestHomeForm(TestBaseClass):

    def test_HomePageFormSubmission(self, testData):

        logs = self.getLogger()


        """Entering a name"""

        name_ele = HomePage(self.driver).NameEle()
        name_ele.send_keys(testData["Sunil"])

        logs.info("Users Entered a Email ID")
        """Entering a email ID"""
        email_ele = HomePage(self.driver).EmailEle()
        email_ele.send_keys(testData["Mail"])

        """Entered a Password"""
        logs.info(" Users Entered a Password ID")
        password_ele = HomePage(self.driver).PasswordEle()
        password_ele.send_keys(testData["Passwaord"])

        """select the ice cream"""

        ice_cream = HomePage(self.driver).IceCreamEle()
        ice_cream.click()

        """click the gender element"""
        gender_ele = HomePage(self.driver).GenderEle()
        gender_ele.click()

        """select the gender"""
        # select_gender = wait.until(ec.presence_of_element_located(
        #     (By.XPATH, "//select[@id='exampleFormControlSelect1']")))
        # Male_Gender = Select(select_gender)
        # Male_Gender.select_by_visible_text('Male')
        self.GenDerSelect("//select[@id='exampleFormControlSelect1']")
        # self.GenDerSelect("//select[@id='exampleFormControlSelect1']")

        """click the radio button"""
        radio_button = HomePage(self.driver).RadiOEle()
        radio_button.click()

        """select the birth day date"""
        logs.info("Entered the BirthDate in field")
        birth_day = HomePage(self.driver).BdayEle()
        birth_day.send_keys(testData["BirthDate"])

        """submit the form"""
        submit_ele = HomePage(self.driver).SubmittButton()
        submit_ele.click()


        """print the text of successfull message"""
        alert_text = self.driver.find_element(By.XPATH, "//div[contains(@class,'alert alert-success')]").text
        print(alert_text)
        logs.info("Get the text of Page"+ alert_text)

        """putting assert method to validate"""
        assert 'Success!' in alert_text
        self.driver.refresh()

    # @pytest.fixture(params=[("Sunil Patil","SunilSaca@gmail.com", "01-02-1993" ),
    #                         ("Varsha Savake", "Test@gmail.com","21-06-2000")])
    @pytest.fixture(params=FormPageTestData.form_test_data)
    def testData(self, request):
        return request.param
