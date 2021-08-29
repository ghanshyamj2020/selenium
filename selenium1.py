from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.get("http://35.223.153.197:4444/wd/hub")
print(driver.title)
print(driver.current_url)
driver.close()
