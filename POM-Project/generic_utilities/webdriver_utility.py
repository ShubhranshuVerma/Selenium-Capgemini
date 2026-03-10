class WebDriverUtility:
    def __init__(self,driver):
        self.driver = driver
    def  click(self,varname):
        self.driver.find_element(*varname).click()
    def send_keys(self,varname,data):
        self.driver.find_element(*varname).send_keys(data)