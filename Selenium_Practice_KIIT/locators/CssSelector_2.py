# # from selenium import webdriver
# # import time
# #
# # from selenium.webdriver.common.by import By
# #
# # opts = webdriver.ChromeOptions()
# # opts.add_experimental_option("detach", True)
# #
# # driver = webdriver.Chrome(opts)
# #
# # driver.get("https://www.saucedemo.com/")
# # time.sleep(2)
# # driver.find_element('css selector', 'input[placeholder="Username"]').send_keys("standard_user")
# # time.sleep(2)
# # driver.find_element('css selector','input[placeholder="Password"]').send_keys("secret_sauce")
# # time.sleep(2)
# # driver.find_element('css selector', 'input[data-test="login-button"]').click()
# # time.sleep(2)
#
# ########################################################################################################
# #
# # from selenium import webdriver
# # import time
# #
# # opts = webdriver.ChromeOptions()
# # opts.add_experimental_option("detach", True)
# #
# # driver = webdriver.Chrome(opts)
# #
# # driver.get("https://demowebshop.tricentis.com/")
# # driver.find_element('css selector', 'a[class="ico-register"]').click()
# # time.sleep(2)
# # driver.find_element('css selector', 'input[id="gender-male"]').click()
# # time.sleep(2)
# # driver.find_element('css selector','input[name="FirstName"]').send_keys("Shubhranshu")
# # time.sleep(2)
# # driver.find_element('css selector', 'input[name="LastName"]').send_keys("Verma")
# # time.sleep(2)
# # driver.find_element('css selector', 'input[name="Email"]').send_keys("shubhranshu@gmail.com")
# # time.sleep(2)
# # driver.find_element('css selector', 'input[id="Password"]').send_keys("123456")
# # time.sleep(2)
# # driver.find_element('css selector', 'input[id="ConfirmPassword"]').send_keys("123456")
# # time.sleep(2)
# # driver.find_element('css selector', 'input[name="register-button"]').click()
# # time.sleep(2)
# """

# import time
#
# ## Eg1
#
# # from selenium import webdriver
# #
# # opts = webdriver.ChromeOptions()
# # opts.add_experimental_option("detach", True)
# #
# # driver = webdriver.Chrome(opts)
# #
# # driver.get("https://www.saucedemo.com/")
# # time.sleep(2)
# #
# # driver.find_element("css selector", 'input[placeholder="Username"]').send_keys("standard_user")
# # time.sleep(1)
# # driver.find_element("css selector", 'input[placeholder="Password"]').send_keys('secret_sauce')
# # time.sleep(1)
# # driver.find_element('css selector', 'input[value="Login"]').click()
# # time.sleep(3)
# # driver.find_element('css selector', 'button[id="react-burger-menu-btn"]').click()
# # time.sleep(2)
# # driver.find_element('css selector', 'a[id="logout_sidebar_link"]').click()
#
#
# ############################################################################
#
# ## EG2
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://in.indeed.com/')
# time.sleep(2)
# driver.find_element('css selector', 'input[id="text-input-what"]').send_keys('software engineer')
# time.sleep(1)
# driver.find_element('css selector', 'input[id="text-input-where"]').send_keys('Bengaluru')
# time.sleep(1)
# driver.find_element('css selector', 'button[type="submit"]').click()
#
# ############################################################################
#
# ## Eg3
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
# driver.find_element('css selector', 'input[type="text"]').send_keys("Ram")
# time.sleep(1)
# driver.find_element('css selector', 'input[type="text"]').send_keys('ram@gmail.com')
#
# #####################################################################
