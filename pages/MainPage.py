# Pages Imports
from pages.BasePage import BasePage as BP
from locators.MainPageLocators import MainPageLocators

# call page
MPL = MainPageLocators()


class MainPage(BP):
    def __init__(self):
        pass

    def click_create_account_button(self):
        create_button = BP.find_element(self, MPL.create_account_button_xpath)
        return create_button

    def click_for_myself_button(self):
        for_myself = BP.find_element(self, MPL.for_myself_button_xpath)
        return for_myself
