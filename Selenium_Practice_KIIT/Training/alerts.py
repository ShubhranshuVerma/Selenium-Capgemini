import time

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Confirmation Alert"]').click()       ## gives an alert
# time.sleep(2)
#
# ## switch the driver to the alert
# alert_obj = driver.switch_to.alert
#
# ## To accept the alert
# alert_obj.accept()
# time.sleep(2)
#
# ## To dismiss the alert
# driver.find_element('xpath', '//button[text()="Confirmation Alert"]').click()
# time.sleep(2)
# alert_obj.dismiss()

################################################################################################

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Simple Alert"]').click()
# time.sleep(2)
#
# ## switch the driver to the alert
# alert_obj = driver.switch_to.alert
#
# alert_obj.accept()
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Simple Alert"]').click()
# time.sleep(2)
# alert_obj.dismiss()

################################################################################################


# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Prompt Alert"]').click()
# time.sleep(2)
#
# ## switch the driver to the alert
# alert_obj = driver.switch_to.alert
#
# ## enter the data
# alert_obj.send_keys("Rohit")
#
# alert_obj.accept()

################################################################################################

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://the-internet.herokuapp.com/basic_auth')
#
# ## The above url will give a pop-up to enter the username and password.
# ## To enter the app, we need to give username and pwd.
# ## The pop-up is not inspectable. And we cant switch the driver to the alert

##------------------------------------------------------------------------------------

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')

################################################################################################

# from selenium import webdriver
#
# opt=webdriver.FirefoxOptions()
# opt.set_preference("dom.webnotifications.enabled", False)
# opt.set_preference("dom.push.enabled", False)
#
# driver=webdriver.Firefox(opt)
#
# driver.get("https://www.irctc.co.in/")



































