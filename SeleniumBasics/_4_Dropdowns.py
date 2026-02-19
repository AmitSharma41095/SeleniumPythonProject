import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

#Static dropdown
dropdwon = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdwon.select_by_index(1)
time.sleep(5)

#auto suggestive dropdown
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("Ind")
time.sleep(3)

countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(countries))

for i in countries:
    if i.text == "Indonesia":
        i.click()
        break
time.sleep(5)

#Extracting text dynamically through script
# print(driver.find_element(By.ID,"autosuggest").text)    #blank output
print(driver.find_element(By.ID,"autosuggest").get_attribute("value"))

