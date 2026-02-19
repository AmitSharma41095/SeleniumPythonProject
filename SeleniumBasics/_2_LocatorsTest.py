import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.CSS_SELECTOR,"input[name='name']:nth-child(2)").send_keys("Amit Sharma")
# (//label[text()='Name']//following::input[@name='name'])[1]
driver.find_element(By.CSS_SELECTOR,"input[name='email']").send_keys("amitsharma@gamail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("12345")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.ID,"inlineRadio2").click()
driver.find_element(By.XPATH,"//input[@value='Submit']").click()

successMsg = driver.find_element(By.CLASS_NAME,"alert-success").text
print(successMsg)

assert "Success" in successMsg

