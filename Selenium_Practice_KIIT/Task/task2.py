from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver = webdriver.Chrome(opts)

driver.get("https://www.ajio.com/")
time.sleep(2)

Men=driver.find_element('xpath','//span[text()="MEN"]')
ac=ActionChains(driver)
ac.move_to_element(Men).perform()
time.sleep(2)

Women=driver.find_element('xpath','//span[text()="WOMEN"]')
ac.move_to_element(Women).perform()
time.sleep(2)

Kids=driver.find_element('xpath','//span[text()="KIDS"]')
ac.move_to_element(Kids).perform()
time.sleep(2)

Beauty=driver.find_element('xpath','//span[text()="BEAUTY"]')
ac.move_to_element(Beauty).perform()
time.sleep(2)

Home_Kitchen=driver.find_element('xpath','//span[text()="Home & Kitchen"]')
ac.move_to_element(Home_Kitchen).perform()
time.sleep(2)

driver.find_element('xpath','//a[text()="Vases"]').click()
time.sleep(2)














