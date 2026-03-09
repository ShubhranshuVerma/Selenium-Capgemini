(2)
"""
Question 1 :

Write a script to:
Open https://www.demowebshop.tricentis.com
Navigate to Books
Add first book to cart
Click Shopping Cart
Verify the product is present in the cart.
"""
#from selenium import webdriver
# import time
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=opts)
# wait_obj = WebDriverWait(driver, 10)
# ac=ActionChains(driver)
# driver.get("https://demowebshop.tricentis.com")
# time.sleep(2)
#
# driver.find_element('xpath','//a[contains(text(),"Books")]').click()
# time.sleep(2)
#
# driver.find_element('xpath','(//input[@value="Add to cart"])[1]').click()
# time.sleep(2)
#
# driver.find_element('xpath','//span[text()="Shopping cart"]').click()
# time.sleep(2)
#
# try:
#     wait_obj.until(EC.presence_of_element_located(('xpath', '(//a[text()="Computing and Internet"])[2]')))
#     print("Valid ")
# except:
#     print("Invalid")

####################################################################################################################################################


'''
Question2:
Write a Selenium script to:
Open https://www.demowebshop.tricentis.com
Navigate to Electronics
Use XPath contains() to locate the Cell Phones category
Click it.
'''
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# opts.add_argument("--disable-notifications")
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
#
# wait = WebDriverWait(driver, 10)
#
# electronics = driver.find_element('xpath', '(//a[contains(text(),"Electronics")])[1]')
# wait.until(EC.element_to_be_clickable(electronics)).click()
# time.sleep(2)
#
# cellphones = driver.find_element('xpath', '(//a[contains(text(),"Cell phones")])[1]')
# wait.until(EC.element_to_be_clickable(cellphones)).click()
#

'''
Question 3 :
Write a Selenium script to:
Open https://the-internet.herokuapp.com/dynamic_loading/1
Click Start
Wait until the Hello World text appears
Print the text.
'''

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
#
# wait = WebDriverWait(driver, 10)
#
# start_btn = driver.find_element('xpath', '//button[text()="Start"]')
# wait.until(EC.element_to_be_clickable(start_btn)).click()
#
# hello_text = driver.find_element('xpath', '//div[@id="finish"]/h4')
# wait.until(EC.visibility_of(hello_text))
#
# print(hello_text.text)

'''
Question 4 :
Write a script to:
Open https://the-internet.herokuapp.com/dynamic_controls
Click Remove
Wait until Add button becomes clickable
Click Add
'''
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://the-internet.herokuapp.com/dynamic_controls")
#
# wait = WebDriverWait(driver, 10)
#
# remove_btn = driver.find_element('xpath', '//button[text()="Remove"]')
# remove_btn.click()
#
# wait.until(EC.presence_of_element_located(('xpath', '//button[text()="Add"]')))
# add_btn = driver.find_element('xpath', '//button[text()="Add"]')
#
# wait.until(EC.element_to_be_clickable(add_btn)).click()
#

'''
Question 5 :
Write a Selenium script to:
Open https://demoqa.com/select-menu
Select "Group 2, option 1" from the Select Value dropdown
Verify the selected value.
'''
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://demoqa.com/select-menu")
#
# wait = WebDriverWait(driver, 10)
#
# dropdown = driver.find_element('xpath', '//div[@id="withOptGroup"]')
# driver.execute_script("arguments[0].scrollIntoView();", dropdown)
#
# wait.until(EC.element_to_be_clickable(dropdown)).click()
#
# option = driver.find_element('xpath', '//div[text()="Group 2, option 1"]')
# wait.until(EC.element_to_be_clickable(option)).click()
#
# selected = driver.find_element('xpath', '//div[contains(@class,"singleValue")]')
# wait.until(EC.visibility_of(selected))
#
# print("Selected value:", selected.text)

"""
Question 6 :
Write a Selenium script to:
Open https://demoqa.com/select-menu
Scroll to Standard multi select
Select Volvo, Saab, and Opel
Print all selected options.
"""

# from selenium import webdriver
# import time
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=opts)
# wait_obj = WebDriverWait(driver, 10)
# ac=ActionChains(driver)
# driver.get("https://demoqa.com/select-menu")
# time.sleep(2)
#
# element=driver.find_element('xpath','//b[text()="Standard multi select"]')
# ac.scroll_to_element(element).perform()
# time.sleep(2)
#
#
# listbox = driver.find_element('xpath', '//select[@id="cars"]')
# select_obj = Select(listbox)
#
# select_obj.select_by_visible_text("Volvo")
# time.sleep(1)
# select_obj.select_by_visible_text("Saab")
# time.sleep(1)
# select_obj.select_by_visible_text("Opel")
# time.sleep(1)
#
# all_options = select_obj.all_selected_options
#
# for ele in all_options:
#     print(ele.text)

####################################################################################################################################################

"""
Question 7 :

Write a Selenium script to:
Open https://demoqa.com/menu/
Hover over Main Item 2
Hover over SUB SUB LIST
Click Sub Sub Item 1
"""

# from selenium import webdriver
# import time
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=opts)
# wait_obj = WebDriverWait(driver, 10)
# ac=ActionChains(driver)
# driver.get("https://demoqa.com/menu/")
# time.sleep(15)
#
# ele1=driver.find_element('xpath','//a[text()="Main Item 2"]')
# ac.move_to_element(ele1).perform()
# time.sleep(2)
# ele2=driver.find_element('xpath','//a[text()="SUB SUB LIST »"]')
# ac.move_to_element(ele2).perform()
# time.sleep(2)
# driver.find_element('xpath','//a[text()="Sub Sub Item 1"]').click()

####################################################################################################################################################

"""
Question 8 :
Write a Selenium script to:
Open https://demoqa.com/droppable
Drag Drag me element
Drop it on Drop here
Verify text changes to Dropped!
"""
# from selenium import webdriver
# import time
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=opts)
# wait_obj = WebDriverWait(driver, 10)
# ac=ActionChains(driver)
# driver.get("https://demoqa.com/droppable")
# time.sleep(15)
#
#
# draggable_ele = driver.find_element('xpath', '//div[text()="Drag Me"]')
# droppable_ele = driver.find_element('xpath', '//p[text()="Drop Here"]')
#
# ac.drag_and_drop(draggable_ele, droppable_ele).perform()

####################################################################################################################################################

"""
Question 9 :
Write a Selenium script to:
Open https://the-internet.herokuapp.com/javascript_alerts
Click JS Confirm
Accept the alert
Verify result text shows You clicked: Ok
"""

# from selenium import webdriver
# import time
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=opts)
# wait_obj = WebDriverWait(driver, 10)
# ac=ActionChains(driver)
#
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# time.sleep(5)
#
# driver.find_element('xpath','//button[text()="Click for JS Confirm"]').click()
# time.sleep
# alert_obj = driver.switch_to.alert
#
# alert_obj.accept()
# time.sleep(2)
#
# try:
#     wait_obj.until(EC.presence_of_element_located(('xpath', '//p[text()="You clicked: Ok"]')))
#     print("Clicked OK ")
# except:
#     print("Invalid")

"""
Question 10 :
Write a Selenium script to:
Open https://the-internet.herokuapp.com/upload
Upload a file from local system
Click Upload
Verify uploaded file name."""

# from selenium import webdriver
# import time
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://the-internet.herokuapp.com/upload")
# time.sleep(2)
#
# file = r'/Users/shubhranshuverma/Desktop/b.txt'
#
# driver.find_element('xpath', '//input[@id="file-upload"]').send_keys(file)
# time.sleep(1)
# driver.find_element('xpath', '//input[@id="file-submit"]').click()

'''
Write a Selenium script that:
Open https://demowebshop.tricentis.com
Navigate to Books
Add all books priced below $20 to cart

'''
from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

driver.get("https://demowebshop.tricentis.com")
driver.find_element('xpath', '//a[contains(text(),"Books")]').click()
time.sleep(2)
books = driver.find_elements('xpath', '//div[@class="item-box"]')

for book in books:
    price = book.find_element('xpath', './/span[@class="price actual-price"]').text
    price = float(price.replace("$", ""))

    if price < 20:
        try:
            button = book.find_element('xpath', './/input[@value="Add to cart"]')
            button.click()
            print("Added book with price:", price)
            time.sleep(1)
        except:
            pass