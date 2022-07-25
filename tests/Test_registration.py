# basic imports
import allure
from pytest import assume
from driver import Driver
import time
import os

# pages Imports
from pages.MainPage import MainPage
from pages.RegistrationPage import RegistrationPage

# clear reports files(images/allure)
mypath = "reports/images"
mypath1 = "reports/allure"
for root, dirs, files in os.walk(mypath):
    for file in files:
        os.remove(os.path.join(root, file))

for root, dirs, files in os.walk(mypath1):
    for file in files:
        os.remove(os.path.join(root, file))
# Call Page
MP = MainPage()
RP = RegistrationPage()


# tests
@allure.feature('Create Gmail')
@allure.story("We should create gmail")
class Test_regisration:
    @allure.title("click login button")
    @allure.description("When we click registration button, the system should send login form")
    def test_click_create_account_button(self):
        create_button = MP.click_create_account_button()
        with assume:
            assert create_button.text == 'Create account'
        create_button.click()

    def test_click_for_myself_button(self):
        for_myself_button = MP.click_for_myself_button()
        with assume:
            assert for_myself_button.text == 'For myself'
        for_myself_button.click()

    def test_input_first_name(self):
        first_name = RP.input_first_name()
        first_name_text = first_name.get_attribute('aria-label')
        with assume:
            assert first_name_text == 'First name'
        first_name_input = str(input('enter your name: '))
        first_name.send_keys(first_name_input)

    def test_input_last_name(self):
        last_name = RP.input_last_name()
        first_name_text = last_name.get_attribute('aria-label')
        with assume:
            assert first_name_text == 'Last name'
        last_name_input = str(input('enter your last name: '))
        last_name.send_keys(last_name_input)

    # def test_input_username(self):
    #     username = RP.input_username()
    #     username_text = username.get_attribute('aria-label')
    #     with assume:
    #         assert username_text == 'Username'
    #     input_user = str(input('enter your username: '))
    #     username.send_keys(input_user)
    #     time.sleep(2)

    def test_input_password(self):
        passwd = RP.input_password()
        passwd_text = passwd.get_attribute('aria-label')
        with assume:
            assert passwd_text == 'Password'
        input_passwd = str(input('enter your passwd: '))
        passwd.send_keys(input_passwd)

    def test_confirm_input_password(self):
        passwd_conf = RP.input_confirm_password()
        passwd_text = passwd_conf.get_attribute('aria-label')
        with assume:
            assert passwd_text == 'Confirm'
        input_passwd = str(input('enter your passwd: '))
        passwd_conf.send_keys(input_passwd)

    def test_click_checkbox(self):
        check = RP.click_checkbox()
        check.click()


