from selenium.webdriver.common.by import By


class VerifyLocator:
    mobile_number_field_ID = (By.ID, 'phoneNumberId')
    next_button = (By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')
    verify_code_field = (By.XPATH, '//*[@id="code"]')
    verify_button = (By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/button/span')
