# def test_login():
#     print("test_login")
# def test_logout():
#     print("test_logout")

# ####################################################################################

import time

# def login():
#     print("login executing")
#
# def logout():
#     print("logout executing")
#
# login()
# logout()
#
# ## works fine
# ## To execute a function, function call is mandatory
#
# ####################################################################################
#
# class Sample:
#
#     def login(self):
#         print("login executing")
#
#     def logout(self):
#         print("logout executing")
#
# s_obj = Sample()
# s_obj.login()
# s_obj.logout()


##############################################################################################

# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")


##############################################################################################

# class TestSample:
#
#     def login(self):
#         print("login executing")
#
#     def signup(self):
#         print("signup executing")
#
#     def logout(self):
#         print("logout executing")
#
##############################################################################################

# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# s = TestSample()
# s.test_login()
# s.test_signup()
# s.test_logout()

##############################################################################################

# class TestSample:
#
#     def __init__(self):
#         pass
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")

##############################################################################################

# import time
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
#
#
# class TestRegister:
#
#     def test_reg(self):
#         driver.find_element('xpath', '//a[text()="Register"]').click()
#         time.sleep(1)
#
#     def test_gender(self):
#         driver.find_element('id', 'gender-male').click()
#
#     def test_fname(self):
#         driver.find_element('id', 'FirstName').send_keys('Rohit')
#
#     def test_lname(self):
#         driver.find_element('id', 'LastName').send_keys('Shukla')
#
#     def test_reg_email(self):
#         driver.find_element('id', 'Email').send_keys('rohit@gmail.com')
#
#     def test_reg_pwd(self):
#         driver.find_element('id', 'Password').send_keys('rohit@12345')
#
#     def test_confirm_pwd(self):
#         driver.find_element('id', 'ConfirmPassword').send_keys('rohit@12345')
#
#
# class Testlogin:
#
#     def test_login(self):
#         driver.find_element('xpath', '//a[text()="Log in"]').click()
#         time.sleep(1)
#
#     def test_login_email(self):
#         driver.find_element('id', 'Email').send_keys('rohit@gmail.com')
#
#     def test_login_pwd(self):
#         driver.find_element('id', 'Password').send_keys('rohit@12345')


####################################################################################

# def test_login():
#     time.sleep(2)
#     print("login executing")
#
# def test_signup():
#     time.sleep(2)
#     print("signup executing")
#
# def test_reg():
#     time.sleep(2)
#     print("reg executing")
#
# def test_logout():
#     time.sleep(2)
#     print("logout executing")
