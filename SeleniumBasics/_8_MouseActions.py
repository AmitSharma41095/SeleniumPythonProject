import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()   #move to element
action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()   #right click
time.sleep(5)
