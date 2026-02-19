from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_ifr") #frameId, name, webelement
print(driver.find_element(By.ID,"tinymce").text)

driver.switch_to.default_content()