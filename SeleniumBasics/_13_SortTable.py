from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
veggieList = driver.find_elements(By.XPATH,"//tbody//tr//td[1]")
OriginalVeggieList = []

for i in veggieList:
    OriginalVeggieList.append(i.text)

sortedVeggieList = OriginalVeggieList.copy()
OriginalVeggieList.sort()

print(OriginalVeggieList)
print(sortedVeggieList)

assert OriginalVeggieList == sortedVeggieList
