from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PAS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, 'button')
    LOCATOR_ERR_LABEL = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    
class OperationsHelper(BasePage):
    def enter_login(self, text):
        logging.info(f'Sending {text} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear
        login_field.send_keys(text)
        
    def enter_pas(self, text):
        logging.info(f'Sending {text} to element {TestSearchLocators.LOCATOR_PAS_FIELD[1]}')
        pas_field = self.find_element(TestSearchLocators.LOCATOR_PAS_FIELD)
        pas_field.clear
        pas_field.send_keys(text)
        
    def click_login_btn(self):
        logging.info('Clicking login btn')
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()
    
    def get_err_text(self):
        err_field = self.find_element(TestSearchLocators.LOCATOR_ERR_LABEL, timer=3)
        text = err_field.text
        logging.info(f'Got text: {text} in error field: {TestSearchLocators.LOCATOR_ERR_LABEL[1]}')
        return text
    
    