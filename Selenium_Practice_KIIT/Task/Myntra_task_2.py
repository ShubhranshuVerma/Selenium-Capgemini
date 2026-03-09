from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

opts=webdriver.ChromeOptions()
opts.add_argument("--disable-notifications")
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=opts)

driver.get("https://www.myntra.com/")