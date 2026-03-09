import time

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# file1 = r'/Users/shubhranshuverma/PycharmProjects/Selenium_Practice_KIIT/Files/css_selector.html'
#
# driver.find_element('xpath', '//input[@id="singleFileInput"]').send_keys(file1)
# time.sleep(1)
# driver.find_element('xpath', '//button[text()="Upload Single File"]').click()

##############################################################################################

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# file1 = r'/Users/shubhranshuverma/PycharmProjects/Selenium_Practice_KIIT/Files/css_selector.html'
# file2 = r'/Users/shubhranshuverma/PycharmProjects/Selenium_Practice_KIIT/Files/demo.html'
# file3 = r'/Users/shubhranshuverma/PycharmProjects/Selenium_Practice_KIIT/Files/loading.html'
# file4 = r'/Users/shubhranshuverma/PycharmProjects/Selenium_Practice_KIIT/Files/progressbar.html'
#
# driver.find_element('xpath', '//input[@id="multipleFilesInput"]').send_keys(f'{file1}\n{file2}\n{file3}\n{file4}')
# time.sleep(1)
# driver.find_element('xpath', '//button[text()="Upload Multiple Files"]').click()

####################################################################################################

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(10)
#
# driver.get("https://demoqa.com/upload-download")
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Download"]').click()
# ## The file will be downloaded in the default downloads folder

##---------------------------------------------------------------------------

# ## Chrome
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# prefs = {
#     "download.default_directory": r'/Users/shubhranshuverma/PycharmProjects/Selenium_Practice_KIIT/Files',
#     "download.prompt_for_download":False,
#     "safebrowsing.enabled":True,
#     "plugins.always_open_pdf_externally":True
# }
#
# opts.add_experimental_option("prefs", prefs)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(10)
#
#
# driver.get("https://demoqa.com/upload-download")
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Download"]').click()

##---------------------------------------------------------------

## Firefox
# from selenium import webdriver
#
# opts = webdriver.FirefoxOptions()
#
# opts.set_preference("browser.download.folderList", 2)
# opts.set_preference("browser.download.dir", r'/Users/shubhranshuverma/PycharmProjects/Selenium_Practice_KIIT/locators')
#
# driver = webdriver.Firefox(opts)
# driver.implicitly_wait(10)
#
#
# driver.get("https://demoqa.com/upload-download")
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Download"]').click()























































































