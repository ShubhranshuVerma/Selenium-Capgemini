from selenium import webdriver
import time
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

driver=webdriver.Chrome(opts)

driver.get("https://saucedemo.com/")
time.sleep(2)

driver.find_element('xpath','//input[@id="user-name"]').send_keys("standard_user")
time.sleep(2)

driver.find_element('xpath','//input[@id="password"]').send_keys("secret_sauce")
time.sleep(2)

driver.find_element('xpath','//input[@id="login-button"]').click()
time.sleep(2)

driver.find_element('xpath','//button[@id="add-to-cart-sauce-labs-backpack"]').click()
time.sleep(2)

driver.find_element('xpath','//a[@class="shopping_cart_link"]').click()
time.sleep(2)

driver.find_element('xpath','//button[@id="checkout"]').click()
time.sleep(2)

driver.find_element('xpath','//input[@id="first-name"]').send_keys("Shubhranshu")
time.sleep(2)

driver.find_element('xpath','//input[@id="last-name"]').send_keys("Verma")
time.sleep(2)

driver.find_element('xpath','//input[@id="postal-code"]').send_keys("751024")
time.sleep(2)

driver.find_element('xpath','//input[@id="continue"]').click()
time.sleep(2)

driver.find_element('xpath','//button[@id="finish"]').click()
time.sleep(2)

driver.find_element('xpath','//button[@id="back-to-products"]').click()
time.sleep(2)

driver.find_element('xpath','//button[@id="react-burger-menu-btn"]').click()
time.sleep(2)

driver.find_element('xpath','//a[@id="logout_sidebar_link"]').click()
time.sleep(2)

driver.close()
driver.quit()
