import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select



# Launch the Browser
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.get("https://rahulshettyacademy.com/angularpractice/")

# submiting form
name_ele = driver.find_element(By.NAME, 'name')
name_ele.send_keys("Sunil Patil")

email_ele = driver.find_element(By.NAME, 'email')
email_ele.send_keys("SunilSavale@gmail.com")

password_ele = driver.find_element(By.ID,'exampleInputPassword1')
password_ele.send_keys("Surat@2024")

ice_cream = driver.find_element(By.ID, 'exampleCheck1')
ice_cream.click()

gender_ele = driver.find_element(By.ID, 'exampleFormControlSelect1')
gender_ele.click()

select_gender = wait.until(ec.presence_of_element_located(
    (By.XPATH, "//select[@id='exampleFormControlSelect1']")))
Male_Gender = Select(select_gender)
Male_Gender.select_by_visible_text('Male')

radio_button = driver.find_element(By.ID, 'inlineRadio1')
radio_button.click()

birth_day = driver.find_element(By.NAME, 'bday')
birth_day.send_keys("01-01-1999")

submit_ele = driver.find_element(By.XPATH, "//input[contains(@value,'Submit')]")
submit_ele.click()

alert_text = driver.find_element(By.XPATH, "//div[contains(@class,'alert alert-success')]")
print(alert_text.text)

assert 'Success!' in alert_text.text


driver.quit()