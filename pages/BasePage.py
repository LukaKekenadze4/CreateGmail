from selenium.webdriver.common.by import By

from driver import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(Driver):
    """
        this is the base page which waits for the element and checks if the element is visible
    """

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator: object, time_out: object = 10) -> object:
        try:
            wait = WebDriverWait(self.driver, time_out)
            element = wait.until(EC.visibility_of_element_located((locator)))
            return element
        except Exception:
            raise Exception(
                'Element by "{0}" with the value "{1}" cannot be found.'.format(
                    locator[0], locator[1]
                )
            )

    def find_elements(self, locator, time_out=10):
        try:
            wait = WebDriverWait(self.driver, time_out)
            print(":::")
            wait.until(EC.visibility_of_element_located((locator)))
            print(":::::")

            elements = self.driver.find_elements(locator)
            return elements
        except Exception:
            raise Exception(
                'Elements by "{0}" with the value "{1}" cannot be found.'.format(
                    locator[0], locator[1]
                )
            )

    def find_children(self, parent):
        children = parent.find_element(By.XPATH, ".//*")
        return children
