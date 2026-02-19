import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for i in checkboxes:
    if i.get_attribute("value") == "option2":
        i.click()
        assert i.is_selected()
        break

# print(driver.find_element(By.CSS_SELECTOR,"input[value='option2']").is_selected())
# assert driver.find_element(By.CSS_SELECTOR,"input[value='option2']").is_selected()

radio = driver.find_elements(By.XPATH,"//input[@class='radioButton']")
for i in radio:
    if i.get_attribute("value") == "radio2":
        i.click()
        assert i.is_selected()
        break
time.sleep(5)