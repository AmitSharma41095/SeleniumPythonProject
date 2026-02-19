from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT,"Click Here").click()
window = driver.window_handles

driver.switch_to.window(window[1]) #switch to child window
print(driver.find_element(By.TAG_NAME,"h3").text)

#switch back to parent window
driver.switch_to.window(window[0]) #switch to parent window
print(driver.find_element(By.TAG_NAME,"h3").text)

