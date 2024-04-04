import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Launch the browser
# service_obj = Service("/Users/rahulshetty/documents/chromedriver")
# driver = webdriver.Chrome(service=service_obj)
#  //a[contains(@href,'shop')]    a[href*='shop']

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/angularpractice/")


driver.find_element(By.CSS_SELECTOR," a[href*='shop']").click()
products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")

for product in products :
        productName = product.find_element_by_xpath("div/h4/a").text
        if productName == "Blackberry":
            # Add item into cart
            product.find_element(By.XPATH, "div/button").click()
# add_cart  = driver.find_element(By.XPATH, "(//button[@class='btn btn-info'])[4]").click()

checkout_ele = driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']")
checkout_ele.click()
confirm_ele = driver.find_element(By.XPATH,"//button[@class='btn btn-success']")
confirm_ele.click()
country_ele = driver.find_element(By.ID,"country")
country_ele.send_keys("ind")
wait = WebDriverWait(driver,10)
india_ele = wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
india_ele.click()
checkBox = driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']")
checkBox.click()
purchase_ele = driver.find_element(By.CSS_SELECTOR,"[type='submit']")
purchase_ele.click()
successText = driver.find_element(By.CLASS_NAME,"alert-success").text
assert "Success! Thank you!" in successText
print(driver.title)
# Close the browser
driver.close()






















