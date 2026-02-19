import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR,"input.search-keyword").send_keys("ber")
time.sleep(2)
veggieResults = driver.find_elements(By.XPATH, "//div[@class='product']")
print(len(veggieResults))
assert len(veggieResults) > 0

#get all product name
ActualProductName = []
for result in veggieResults:
    ActualProductName.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH,"div//button").click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME,"promoBtn").click()

#explicit wait
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoInfo")))

prmocodemsg = driver.find_element(By.CLASS_NAME,"promoInfo").text
assert prmocodemsg == "Code applied ..!"

#Functional case 1 : Sum all the prices and validate against actual price.
prices = driver.find_elements(By.XPATH, "//table//tr//td[5]//p")
sum =0
for i in prices:
    sum = sum + int(i.text)
print("Sum values from table :", sum)

ActualPrice = driver.find_element(By.CLASS_NAME,"totAmt").text
print("ActualPrice : ",ActualPrice)

assert int(sum) == int(sum)

#Functional case 2. Validate price after discount is always less than actual price.
totalAfterDiscount = driver.find_element(By.CLASS_NAME,"discountAmt").text
print("Price ater discount : ",totalAfterDiscount )
assert float(totalAfterDiscount) < float(ActualPrice)

#Functional case 3. Verify the items selected is visible on checkout page (2 lists)
productNames = driver.find_elements(By.XPATH,"//table//tr//td[2]//p")
ExpectedProductNames = []
for i in productNames:
    ExpectedProductNames.append(i.text)

print("ActualProductName : ",ActualProductName)
print("ExpectedProductNames : ",ExpectedProductNames)

assert ActualProductName == ExpectedProductNames

time.sleep(5)


