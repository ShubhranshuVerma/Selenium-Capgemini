"""Go to Facebook
Enter username & password
Wait for login button to be clickable
Click login
Validate login success"""

from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)
# driver.get("https://www.facebook.com")
# time.sleep(2)
# driver.find_element('xpath','//input[@id="_R_1h6kqsqppb6amH1_"]').send_keys("Shubhranshu")
# time.sleep(2)
# driver.find_element('xpath','//input[@id="_R_1hmkqsqppb6amH1_"]').send_keys("password")
# time.sleep(2)
#
# driver.find_element('xpath','//span[text()="Log in"]').click()
# time.sleep(2)
#
# current_url = driver.current_url
#
# if "login" not in current_url and "facebook.com" in current_url:
#     print("Login Successful")
# else:
#     print("Login Failed")

##-----------------------------------------------------------
"""
Go to myntra
search for puma 
select any option from the auto-suggestions and click on it
select the product(will open in new tab)
handle the new tab 
add product to cart"""
#
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.maximize_window()
#
# driver.get("https://www.myntra.com")
# time.sleep(5)
#
# wait = WebDriverWait(driver, 10)
# search_box = wait.until(EC.presence_of_element_located(('xpath', '//input[@placeholder="Search for products, brands and more"]')))
# search_box.send_keys("puma")
#
#
# suggestion = wait.until(EC.presence_of_element_located(
#     ('xpath', '//li[contains(@class,"desktop-suggestion")][2]')
# ))
# suggestion.click()
#
# product = wait.until(EC.presence_of_element_located(
#     ('xpath', '(//li[@class="product-base"])[1]')
# ))
# product.click()
#
# windows = driver.window_handles
# driver.switch_to.window(windows[1])
#
# shoe_size = wait.until(EC.element_to_be_clickable(
#     ('xpath','//p[text()="8"]')
# ))
# time.sleep(5)
# add_to_bag = wait.until(EC.element_to_be_clickable(
#     ('xpath', '//div[text()="ADD TO BAG"]')
# ))
# time.sleep(2)
#
# shoe_size.click()
# add_to_bag.click()
# time.sleep(5)


#print("Product added to cart successfully!")

##-----------------------------------------------------------
"""
Go to https://www.icici.bank.in/
click on accounts
click on apply(opens in new tab, handle it)
enter the details(fake data)
click on apply now
validate unsuccessfull message"""

# #ques 3
# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://www.icici.bank.in/")
# driver.maximize_window()
# time.sleep(2)
#
# driver.find_element("xpath", "//span[contains(text(),' Accounts')]").click()
# time.sleep(2)
#
# driver.find_element("xpath", '(//a[@data-itm="nli_savingsAccount_accounts_savingsAccount_productPageHeroBanner_1CTA_CMS_apply_CAMPAIGNS"])[2]').click()
# time.sleep(3)
#
# driver.switch_to.window(driver.window_handles[1])
#
# driver.find_element("xpath", '//input[@id="name"]').send_keys("hel")
# driver.find_element("xpath", '//input[@id="mobile_number"]').send_keys("9231313123")
#
# driver.find_element("xpath", "//button[contains(text(),'Apply')]").click()
# time.sleep(2)
#
# print("Validation message displayed")
#
# driver.close()

##-----------------------------------------------------------

"""Go to https://www.netmeds.com/
hover to medicines using ActionChains
click on order online
Go to order using prescription
upload some text file using file upload popup"""

# driver.maximize_window()
#
# driver.get("https://www.netmeds.com/")
# time.sleep(5)
#
# actions = ActionChains(driver)
# medicines = driver.find_element("xpath", "//a[contains(text(),'Medicine')]")
# actions.move_to_element(medicines).perform()
# time.sleep(2)
#
# driver.find_element("xpath", "(//a[contains(text(),'Order Online')])[1]").click()
# time.sleep(10)
#
# driver.find_element("xpath", "//button[text()=' Upload Prescription ']").click()
# time.sleep(3)




##-----------------------------------------------------------

"""Go to https://www.netmeds.com/
click on signin
enter your valid mobile number
click get otp
enter the otp and validate the succesfull login"""

# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
# wait = WebDriverWait(driver, 10)
#
# driver.get("https://www.netmeds.com/")
# driver.maximize_window()
#
# driver.find_element('xpath','//div[@class="position-relative profile-name"]').click()
# time.sleep(2)
#
# driver.find_element('xpath','//input[@name="mobile-number"]').send_keys("7388363695")
# time.sleep(2)
#
# driver.find_element('xpath','//button[contains(text(),"Get OTP")]').click()
# time.sleep(5)
#
# try:
#     wait.until(ec.visibility_of_element_located(('xpath', '//button[contains(text()," Get started ")]')))
#     print("Login Successful")
# except:
#     print("Login Failed")
#
# time.sleep(2)
#
# driver.quit()


##-----------------------------------------------------------

"""Go to https://www.irctc.co.in/nget/train-search
enter from, to, select the date, handle the dropdowns and click on search trains
try to book a train"""

# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get("https://www.irctc.co.in/nget/train-search")
# driver.maximize_window()
# time.sleep(2)
#
# driver.find_element('xpath','//input[@ aria-label="Enter From station. Input is Mandatory."]').send_keys("BBS")
# time.sleep(1)
# driver.find_element('xpath','//li[@ id="p-highlighted-option"]').click()
#
# driver.find_element('xpath','//input[@ aria-label="Enter To station. Input is Mandatory."]').send_keys("HYB")
# time.sleep(1)
# driver.find_element('xpath','//li[@ id="p-highlighted-option"]').click()
#
# driver.find_element('xpath','//input[@ class="ng-tns-c69-9 ui-inputtext ui-widget ui-state-default ui-corner-all ng-star-inserted"]').click()
# driver.find_element('xpath','(//td[@ class="ng-tns-c69-9 ng-star-inserted"])[20]').click()
# time.sleep(1)
#
# driver.find_element('xpath','//div[@ class="ng-tns-c76-10 ui-dropdown ui-widget ui-state-default ui-corner-all"]').click()
# time.sleep(1)
# driver.find_element('xpath','//li[@ aria-label="AC First Class (1A) "]').click()
#
# driver.find_element('xpath','//div[@ class="ng-tns-c76-11 ui-dropdown ui-widget ui-state-default ui-corner-all"]').click()
# time.sleep(1)
# driver.find_element('xpath','//li[@ aria-label="TATKAL"]').click()
#
# driver.find_element('xpath','//button[contains(text()," Search Trains ")]').click()

##-----------------------------------------------------------

"""Go to https://www.purplle.com/
hover to brands
search for lakme and click on it
scroll until the first item is visible
click on first product
Enter pincode and check if it is available"""
#
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# wait = WebDriverWait(driver, 10)
#
# driver.get("https://www.purplle.com/")
#
# brands = wait.until(EC.presence_of_element_located(
#     ('xpath', '//a[contains(text(),"BRANDS")]')
# ))
# ActionChains(driver).move_to_element(brands).perform()
#
# lakme = wait.until(EC.element_to_be_clickable(
#     ('xpath', '(//span[contains(text(),"Lakme")])[2]')
# ))
# lakme.click()
#
# first_product = wait.until(EC.presence_of_element_located(
#     ('xpath', '(//div[contains(@class,"product")])[1]')
# ))
#
# driver.execute_script("arguments[0].scrollIntoView();", first_product)
#
# first_product.click()
#
# windows = driver.window_handles
# driver.switch_to.window(windows[-1])
#
# pincode_box = wait.until(EC.presence_of_element_located(
#     ('xpath', '//input[@placeholder="Enter Pincode"]')
# ))
# pincode_box.send_keys("700001")   # Example Kolkata pincode
#
# check_btn = driver.find_element('xpath', '//button[contains(text(),"Check")]')
# check_btn.click()
#
# print("Pincode availability checked successfully!")

##-----------------------------------------------------------

"""Go to https://lifeinsurance.adityabirlacapital.com/
click on her insurance
enter the data using data driven testing"""

# from ddt.excel import excel_data
# data = excel_data()
# driver.get('https://lifeinsurance.adityabirlacapital.com/')
# driver.implicitly_wait(10)
# driver.find_element('xpath','(//a[text()="Her Insurance"])[2]').click()
# time.sleep(2)
# driver.find_element('id','firstName').send_keys(data['fname'])
# driver.find_element('id','lastName').send_keys(data['lname'])
# driver.find_element('id','email').send_keys(data['email'])
# driver.find_element('id','phonenumber').send_keys(data['ph'])

##-----------------------------------------------------------

"""Go to https://www.apollopharmacy.in/
click on find doctors
click on general physician
click on the first doctor available
select the date
select the time
click on continue"""

# driver.get("https://www.apollopharmacy.in/")
# driver.maximize_window()
#
# time.sleep(5) #close all popups manually
#
# driver.find_element('xpath','//a[text()="Find Doctors"]').click()
# time.sleep(2)
# driver.find_element('xpath','//p[text()="General Physician/ Internal Medicine"]').click()
# time.sleep(2)
# visit_doctor = WebDriverWait(driver,15).until(
#     EC.element_to_be_clickable(("xpath","//span[contains(text(),'Visit Doctor')]"))
# )
# visit_doctor.click()
# time.sleep(2)
# driver.find_element('xpath','//p[text()="19"]').click()
# time.sleep(2)
# driver.find_element('xpath','//div[text()="11:30 AM"]').click()
# time.sleep(2)
# driver.find_element('xpath','//span[text()="Continue"]').click()
# time.sleep(2)
#
# print("Appointment flow executed")

##-----------------------------------------------------------

"""Go to https://porter.in/
enter city
click on packers and movers
enter pickup location
enter drop location
enter phone num
enter shifting date
check the price
"""
# driver.get("https://porter.in/")
# driver.maximize_window()
# time.sleep(3)
#
# driver.find_element('xpath','//p[text()="City:"]').click()
# time.sleep(2)
# driver.find_element('xpath','//div[text()="bangalore"]').click()
# time.sleep(2)
#
# driver.find_element('xpath','//div[contains(text(),"Packers & Movers")]').click()
# time.sleep(3)
#
#
# driver.find_element('xpath','//input[@placeholder="Sending from"]').send_keys("Indiranagar")
# time.sleep(2)
# driver.find_element('xpath','(//div[contains(text(),"Indiranagar")])[1]').click()
# time.sleep(2)
#
# driver.find_element('xpath','//input[@placeholder="Sending to"]').send_keys("Whitefield")
# time.sleep(2)
# driver.find_element('xpath','(//div[contains(text(),"Whitefield")])[1]').click()
# time.sleep(2)
#
# driver.find_element('xpath','//input[@placeholder="Enter Contact Details"]').send_keys("9876543210")
# time.sleep(2)
#
# driver.find_element('xpath','//input[@value="18/03/2026"]').click()
# time.sleep(2)
# driver.find_element('xpath','//p[text()="19"]').click() #pass date you want to check for
# time.sleep(2)
# driver.find_element('xpath','(//div[text()="Check Price"])[1]').click()
#
# print("Price check executed")