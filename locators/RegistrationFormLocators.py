# Basic Imports
from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    first_name_field_ID = (By.ID, 'firstName')
    last_name_field_ID = (By.ID, 'lastName')
    username_field_ID = (By.ID, 'username')
    password_field_xpath = (By.XPATH, '//*[@id="passwd"]/div[1]/div/div[1]/input')
    confirm_password_field_xpath = (By.XPATH, '//*[@id="confirm-passwd"]/div[1]/div/div[1]/input')
    checkBox_xpath = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[3]/div/div[1]/div/div/div[1]/div/input')
    suggestion1_xpath = (By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[2]/div/ul/li[2]/button')
    suggestion2_xpath = (By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[2]/div/ul/li[3]/button')
    suggestion3_xpath = (By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[2]/div/ul/li[4]/button')

    next_button_xpath = (By.XPATH, '//*[@id="accountDetailsNext"]/div/button/div[1]')
    next_button_text_xpath = (By.XPATH, '//*[@id="accountDetailsNext"]/div/button/span')
