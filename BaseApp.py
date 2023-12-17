from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


class BasePage:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.base_url = "https://test-stand.gb.ru/"

    def find_element(self, locator, timer=10):
        return WebDriverWait(self.driver, timer).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        return element.value_of_css_property(property)

    def go_to_site(self):
        return self.driver.get(self.base_url)
    
    def switch_to_alert(self): 
        alert = WebDriverWait(self.driver, timeout=3).until(EC.alert_is_present())
        msg = alert.text
        # logging.warning(f'{msg=}')
        alert.accept()
        return msg
