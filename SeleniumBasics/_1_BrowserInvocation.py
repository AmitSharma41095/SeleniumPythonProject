from selenium import webdriver

driver = webdriver.Chrome()
# fire = webdriver.Firefox()
# webdriver.Edge()
# webdriver.Ie()
driver.maximize_window()
driver.get("https://www.google.com/")
print("Title of page : ",driver.title)
print("Current page URL : ", driver.current_url)

# driver.close()
# driver.quit()
# driver.forward()
# driver.back()
# driver.refresh()
# driver.maximize_window()
# driver.minimize_window()

# fire = webdriver.Firefox()
# webdriver.Edge()
# webdriver.Ie()
