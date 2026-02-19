import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/locatorspractice/")

driver.find_element(By.ID,"inputUsername").send_keys("Amit")
driver.find_element(By.NAME,"inputPassword").send_keys("Hello")
driver.find_element(By.CLASS_NAME,"signInBtn").click()
time.sleep(3)
errorMsg = driver.find_element(By.XPATH,"//p[@class='error']").text
print(errorMsg)

driver.find_element(By.LINK_TEXT,"Forgot your password?").click()

time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Name']").send_keys("Amit Sharma")
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Email']").send_keys("amit@test.com")
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Phone Number']").send_keys("9090909090")
driver.find_element(By.CLASS_NAME,"reset-pwd-btn").click()

time.sleep(3)
resetPasswordMessage = driver.find_element(By.CSS_SELECTOR,"p.infoMsg").text
print(resetPasswordMessage)
resetPassword = resetPasswordMessage.split("'")[1]

driver.find_element(By.XPATH,"//button[text()='Go to Login']").click()

time.sleep(3)
driver.find_element(By.ID,"inputUsername").send_keys("Amit")
driver.find_element(By.NAME,"inputPassword").send_keys(resetPassword)
driver.find_element(By.CLASS_NAME,"signInBtn").click()

time.sleep(3)
homeText = driver.find_element(By.CLASS_NAME,"login-container").text
print(homeText)
assert "Rahul Shetty" in homeText

driver.find_element(By.XPATH,"//button[text()='Log Out']").click()