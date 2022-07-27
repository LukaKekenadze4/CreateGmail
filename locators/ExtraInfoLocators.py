# Basic Imports
from selenium.webdriver.common.by import By


class ExtraPageLocatros:
    Mobile_number_ID = (By.ID, 'phoneNumberId')
    recovery_mail_xpath = (By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div[1]/div/div[1]/input')
    day_input_id = (By.ID, 'day')
    year_input_id = (By.ID, 'year')
    month_select_ID = (By.ID, 'month')
    gender_select_ID = (By.ID, 'gender')
    next_button_xpath = (By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')
