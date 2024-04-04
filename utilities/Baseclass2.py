import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

"""I will call the fixture from conftest"""

@pytest.mark.usefixtures("setup")
class TestFormSubmission:
    # pass
    def GenDerSelect(self, xpath):
        wait = WebDriverWait(self.driver, 10)
        select_gender = wait.until(ec.presence_of_element_located(
            (By.XPATH, xpath)))
        Male_Gender = Select(select_gender)
        Male_Gender.select_by_visible_text('Male')