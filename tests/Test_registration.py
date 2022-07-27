# basic imports
import allure
from pytest import assume
from driver import Driver
import time
import os
from selenium.webdriver.support.select import Select

# pages Imports
from pages.MainPage import MainPage
from pages.RegistrationPage import RegistrationPage
from pages.VerifyPage import VerifyPage

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
VP = VerifyPage()


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

    @allure.title("click myself button")
    @allure.description("When we click create account button, We should choose account for Myself type")
    def test_click_for_myself_button(self):
        for_myself_button = MP.click_for_myself_button()
        with assume:
            assert for_myself_button.text == 'For myself'
        for_myself_button.click()

    @allure.title("enter our first name")
    @allure.description("We should enter our first name in the registration form")
    def test_input_first_name(self):
        first_name = RP.input_first_name()
        first_name_text = first_name.get_attribute('aria-label')
        with assume:
            assert first_name_text == 'First name'
        first_name_input = str(input('enter your name: '))
        first_name.send_keys(first_name_input)

    @allure.title("enter our last name")
    @allure.description("We should enter our last name in the registration form")
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
    @allure.title("enter password")
    @allure.description("We should enter password in the registration form")
    def test_input_password(self):
        passwd = RP.input_password()
        passwd_text = passwd.get_attribute('aria-label')
        with assume:
            assert passwd_text == 'Password'
        input_passwd = str(input('enter your passwd: '))
        passwd.send_keys(input_passwd)

    @allure.title("enter confirm password")
    @allure.description("We should re-enter password in the registration form")
    def test_confirm_input_password(self):
        passwd_conf = RP.input_confirm_password()
        passwd_text = passwd_conf.get_attribute('aria-label')
        with assume:
            assert passwd_text == 'Confirm'
        input_passwd = str(input('enter your passwd: '))
        passwd_conf.send_keys(input_passwd)

    @allure.title("click next button")
    @allure.description("When we enter our first and last names, the system should suggests our surname based on our first and last names, We should choose another one or let's leave it the same")
    def test_click_next_button(self):
        choose_username_version = str(input('Would you like your choice//type "yes" or "no": '))
        if choose_username_version.upper() == 'NO':
            choose_suggestion = int(input('choose one of them "1" or "2" or "3": '))
            if int(choose_suggestion) == 1:
                sug1 = RP.get_suggestions()[0]
                sug1.click()
                NextButton = RP.click_next_button()
                with assume:
                    assert NextButton.text == 'Next'
                NextButton.click()
            elif int(choose_suggestion) == 2:
                sug2 = RP.get_suggestions()[1]
                sug2.click()
                NextButton = RP.click_next_button()
                with assume:
                    assert NextButton.text == 'Next'
                NextButton.click()
            elif int(choose_suggestion) == 3:
                sug3 = RP.get_suggestions()[2]
                sug3.click()
                NextButton = RP.click_next_button()
                with assume:
                    assert NextButton.text == 'Next'
                NextButton.click()
                NextButton[0].click()
        elif choose_username_version.upper() == 'YES':
            NextButton = RP.click_next_button()
            with assume:
                assert NextButton.text == 'Next'
            NextButton.click()

    @allure.title("enter our mobile number")
    @allure.description("We should enter our mobile number,where system sends OTP code")
    def test_input_mobile_number(self):
        mobile_field = VP.input_mobile_number()
        mobile_number = int(input('choose your mobile number: '))
        mobile_field.send_keys(mobile_number)
        NextButton = VP.click_next_button()
        with assume:
            assert NextButton.text == 'Next'
        NextButton.click()

    @allure.title("We should enter verify code")
    @allure.description("when we enter our mobile number, we should enter OTP code")
    def test_input_verify_code(self):
        verification_code_field = VP.input_verify_code()
        verification_code = int(input('enter verification code: '))
        verification_code_field.send_keys(verification_code)
        verify_button = VP.click_verify_button()
        verify_button.click()
