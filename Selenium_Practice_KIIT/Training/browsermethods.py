import time

from selenium import webdriver

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

driver=webdriver.Chrome(opts)

##To launch the application
driver.get("https://www.myntra.com/")

#Maximise
driver.maximize_window()
time.sleep(2)

#Minimise
driver.minimize_window()
time.sleep(2)

#Maximise
driver.maximize_window()
time.sleep(2)

#To go back
driver.back()
time.sleep(2)

#to go forward
driver.forward()
time.sleep(2)

#To refresh
driver.refresh()
time.sleep(2)

#Name
print(driver.name)

#currenturl
print(driver.current_url)

#Title
print(driver.title)

#screenshot
driver.save_screenshot("myntra.png")

driver.close()