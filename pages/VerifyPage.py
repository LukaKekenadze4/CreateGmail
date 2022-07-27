from locators.VerifyPageLocators import VerifyLocator
from pages.BasePage import BasePage as BP

VFL = VerifyLocator()


class VerifyPage(BP):
    def __init__(self):
        pass

    def input_mobile_number(self):
        number_field = BP.find_element(self, VFL.mobile_number_field_ID)
        return number_field

    def click_next_button(self):
        next_button = BP.find_element(self, VFL.next_button)
        return next_button

    def input_verify_code(self):
        verification_field = BP.find_element(self, VFL.verify_code_field)
        return verification_field

    def click_verify_button(self):
        verify_button = BP.find_element(self, VFL.verify_button)
        return verify_button