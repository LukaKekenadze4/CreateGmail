# Basic Imports
from selenium.webdriver.common.by import By

# Pages Imports
from pages.BasePage import BasePage as BP
from locators.RegistrationFormLocators import RegistrationPageLocators

# call page
RPL = RegistrationPageLocators()


class RegistrationPage(BP):
    def __init__(self):
        pass

    def input_first_name(self):
        FirstName = BP.find_element(self, RPL.first_name_field_ID)
        return FirstName

    def input_last_name(self):
        LastName = BP.find_element(self, RPL.last_name_field_ID)
        return LastName

    def input_username(self):
        UserName = BP.find_element(self, RPL.username_field_ID)
        return UserName

    def input_password(self):
        Password = BP.find_element(self, RPL.password_field_xpath)
        return Password

    def input_confirm_password(self):
        ConfirmPassword = BP.find_element(self, RPL.confirm_password_field_xpath)
        return ConfirmPassword

    def click_checkbox(self):
        CheckBox = BP.find_element(self, RPL.checkBox_xpath)
        return CheckBox

    def get_suggestions(self):
        suggestions = BP.find_element(self, RPL.suggestions_xpath)
        return suggestions



