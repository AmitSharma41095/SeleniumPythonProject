import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()
alertPopUp = driver.switch_to.alert
print(alertPopUp.text)
alertPopUp.send_keys("Amit Sharma")
alertPopUp.accept()
# alertPopUp.dismiss()

assert "Amit" in driver.find_element(By.CSS_SELECTOR,"p#result").text
