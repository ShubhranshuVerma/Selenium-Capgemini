# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from  selenium import webdriver
# import time
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
# driver=webdriver.Chrome(opts)
# driver.get("https://www.myntra.com/?utm_source=gh_hmedia_mash&utm_medium=hmedia_rev&utm_campaign=gh_hmedia_mash&gad_source=1")
# time.sleep(5)
# ac=ActionChains(driver)
#
# ac.send_keys(Keys.END).perform()
# #
# #_______________________________________________________________________________________________________________________

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import time
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get("https://www.linkedin.com/home")
# time.sleep(2)
#
# google_frame=driver.find_element('xpath','//iframe[@title="Sign in with Google Button"]')
# driver.switch_to.frame(google_frame)
# time.sleep(2)
#
# driver.find_element('xpath','//span[text()="Continue with Google"]').click()
# time.sleep(2)
#
# driver.switch_to.parent_frame()
# time.sleep(2)
#
# scroll_till=driver.find_element('xpath','//h2[contains(text(),"Join your colleagues, classmates, and friends on LinkedIn")]')
# ac=ActionChains(driver)
# ac.scroll_to_element(scroll_till).perform()
# time.sleep(2)
#
# youtube_frame=driver.find_element('xpath','//iframe[@title="Gayatri Iyer: In it to chase my dream | #InItTogether"]')
# driver.switch_to.frame(youtube_frame)
# time.sleep(2)
#
# driver.find_element("xpath", '//button[@class="ytp-large-play-button ytp-button"]').click()
