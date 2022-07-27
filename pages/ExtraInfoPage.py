from pages.BasePage import BasePage as BP
from locators.ExtraInfoLocators import ExtraPageLocatros

EPL = ExtraPageLocatros()


class ExtraPage(BP):
    def check_mobile_number(self):
        mobile_number_field = BP.find_element(self, EPL.Mobile_number_ID)
        return mobile_number_field

    def input_recovery_mail(self):
        RecoveryMail_field = BP.find_element(self, EPL.recovery_mail_xpath)
        return RecoveryMail_field

    def input_day(self):
        Day = BP.find_element(self, EPL.day_input_id)
        return Day

    def input_year(self):
        Year = BP.find_element(self, EPL.year_input_id)
        return Year
