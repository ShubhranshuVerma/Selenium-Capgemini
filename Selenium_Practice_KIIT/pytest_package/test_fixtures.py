import pytest

#
# @pytest.fixture()
# def greet():
#     print("Good morning")
#
# def test_login(greet):
#     print("login executing")
#
# def test_logout(greet):
#     print("logout executing")

###############################################################################

# @pytest.fixture()
# def greet():
#     print("Good morning")
#
# def test_login(greet):
#     print("login executing")
#
# def test_signup():
#     print("signup executing")
#
# def test_logout(greet):
#     print("logout executing")

###############################################################################

# @pytest.fixture()
# def greet():
#     print("Good morning")
#     yield
#     print("Good evening")
#
# def test_login(greet):
#     print("login executing")
#
# def test_signup(greet):
#     print("signup executing")
#
# def test_logout(greet):
#     print("logout executing")
###############################################################################
#
# @pytest.fixture(autouse=True)
# def greet():
#     print("Good morning")
#     yield
#     print("Good evening")
#
# def test_login():
#     print("login executing")
#
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")

###############################################################################

# @pytest.fixture()
# def greet():
#     print("Good morning")
#     yield
#     print("Good evening")
# class TestSample:
#
#     def test_login(self, greet):
#         print("login executing")
#
#     def test_signup(self, greet):
#         print("signup executing")
#
#     def test_logout(self, greet):
#         print("logout executing")

###############################################################################

# @pytest.fixture(autouse=True)
# def greet():
#     print("Good morning")
#     yield
#     print("Good evening")
#
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

###############################################################################

# @pytest.fixture(autouse=True, scope='class')
# def greet():
#     print("Good morning")
#     yield
#     print("Good evening")
#
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

###############################################################################

# @pytest.fixture(autouse=True, scope='class')
# def greet():
#     print("Good morning")
#     yield
#     print("Good evening")
#
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
# class TestExample:
#
#     def test_gmail(self):
#         print("gmail executing")
#
#     def test_yahoo(self):
#         print("yahoo executing")
#
#     def test_reg(self):
#         print("reg executing")

###############################################################################

# @pytest.fixture(autouse=True, scope='module')
# def greet():
#     print("Good morning")
#     yield
#     print("Good evening")
#
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
# class TestExample:
#
#     def test_gmail(self):
#         print("gmail executing")
#
#     def test_yahoo(self):
#         print("yahoo executing")
#
#     def test_reg(self):
#         print("reg executing")

###############################################################################

# import time
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# @pytest.fixture(scope='class')
# def setup():
#     driver = webdriver.Chrome(opts)
#     driver.get("https://demowebshop.tricentis.com/")
#     time.sleep(2)
#     yield driver
#     driver.close()

# ## setup --> webdriver.Chrome(opts)
#
# class TestRegister:
#
#     def test_reg_link(self, setup):
#         setup.find_element('xpath', '//a[text()="Register"]').click()
#         time.sleep(1)
#
#     def test_gender_btn(self, setup):
#         setup.find_element('id', 'gender-male').click()
#
#     def test_fname(self, setup):
#         setup.find_element('id', 'FirstName').send_keys('Adithya')
#
#     def test_lname(self, setup):
#         setup.find_element('id', 'LastName').send_keys('Mohla')
#
#     def test_reg_email(self, setup):
#         setup.find_element('id', 'Email').send_keys('adi@gmail.com')
#
#     def test_reg_pwd(self, setup):
#         setup.find_element('id', 'Password').send_keys('adi@12345')
#
#     def test_confirm_pwd(self, setup):
#         setup.find_element('id', 'ConfirmPassword').send_keys('adi@12345')
#         time.sleep(2)
#
# class TestLogin:
#
#     def test_login_link(self, setup):
#         setup.find_element('xpath', '//a[text()="Log in"]').click()
#         time.sleep(1)
#
#     def test_login_email(self, setup):
#         setup.find_element('id', 'Email').send_keys('adi@gmail.com')
#
#     def test_login_pwd(self, setup):
#         setup.find_element('id', 'Password').send_keys('adi@12345')
#
#
#
#









































































































