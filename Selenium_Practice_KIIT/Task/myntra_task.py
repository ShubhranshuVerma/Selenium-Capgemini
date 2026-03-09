'''
Adding two products to myntra cart.
Concepts used:
1.Mouse Hover
2.Multiple window handling
3.XPath

---Note--
Products change dynamically. So it is better to use dependent-independent Xpath.
However, for simplicity purpose I have just selected random element.
Might modify later on.
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
opts.add_argument("--disable-notifications")
driver = webdriver.Chrome(opts)

driver.get('https://www.myntra.com/?utm_source=dms_google&utm_medium=dms_searchbrand_cpc&utm_campaign=dms_google_searchbrand_cpc_Search_Brand_Myntra_Brand_India_BM_TROAS_SOK_New&gad_source=1&gad_campaignid=20443628324&gbraid=0AAAAADoxBh40-nUteBZ9urEw6d-2BJRZr&gclid=Cj0KCQiAk6rNBhCxARIsAN5mQLvvPvo4FH2Y_XcArEwxJ6-r6iDqhTbKIu3rpp6lGc86OQ8G1F9iEZsaAnECEALw_wcB')
time.sleep(2)

actions = ActionChains(driver)

men = driver.find_element('xpath', '(//a[text()="Men"])[1]')
actions.move_to_element(men).perform()
time.sleep(3)

tshirts = driver.find_element('xpath', "//a[text()='T-Shirts']")
actions.move_to_element(tshirts).click().perform()
time.sleep(3)

driver.find_element('xpath', '//img[@title="Park Avenue Men Geometric Print Polo Collar Slim Fit T-shirt"]').click()
time.sleep(1)

windows = driver.window_handles

# switch to new tab
driver.switch_to.window(windows[1])


driver.find_element('xpath', '//p[text()="M"]').click()
time.sleep(1)
driver.find_element('xpath', '//div[text()="ADD TO BAG"]').click()
time.sleep(1)
driver.find_element('xpath', '//span[@class="myntraweb-sprite desktop-iconBag sprites-headerBag"]').click()
time.sleep(3)

driver.back() #back to men page
time.sleep(1)

driver.close()  # closes products tab in men
driver.switch_to.window(windows[0])
time.sleep(1)

driver.back() #back to home page
time.sleep(4)

##adding product 2 to cart.

women = driver.find_element('xpath', '(//a[text()="Women"])[1]')
actions.move_to_element(women).perform()
time.sleep(3)
Tops = driver.find_element('xpath', "//a[text()='Tops']")
actions.move_to_element(Tops).click().perform()
time.sleep(3)
driver.find_element('xpath', '//img[@title="Burgstudio9 Sweetheart Neck Cotton Crop Regular Top"]').click()
time.sleep(1)

windows = driver.window_handles

# switch to new tab
driver.switch_to.window(windows[1])


driver.find_element('xpath', '//p[text()="M"]').click()
time.sleep(1)
driver.find_element('xpath', '//div[text()="ADD TO BAG"]').click()
time.sleep(1)
driver.find_element('xpath', '//span[@class="myntraweb-sprite desktop-iconBag sprites-headerBag"]').click()
time.sleep(3)

driver.back() #back to men page
time.sleep(1)

driver.close()  # closes products tab in men
driver.switch_to.window(windows[0])
time.sleep(1)

driver.back() #back to home page
time.sleep(1)