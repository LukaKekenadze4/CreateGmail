from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Driver:
    """
        this is the configuration of driver
    """
    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome("chromedriver")
    driver.maximize_window()
    # driver.set_window_size(1440, 768)
    driver.get("https://accounts.google.com/signin/v2/identifier?hl=en&continue=https%3A%2F%2Fmail.google.com&service=mail&ec=GAlAFw&flowName=GlifWebSignIn&flowEntry=AddSession")
    driver.implicitly_wait(10)
    print("Driver initialized. {a}".format(a=driver.title))
