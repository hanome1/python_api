from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PAS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, 'button')
    LOCATOR_ERR_LABEL = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_BLOG_HEADER = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_NEW_POST_BTN = (By.XPATH, """//*[@id="create-btn"]""")
    LOCATOR_NEW_POST_FIELD = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_NEW_POST_CONFIRM_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button""")
    LOCATOR_NEW_POST_HEADER = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_CONTACT_BTN = (By.XPATH, '''//*[@id="app"]/main/nav/ul/li[2]/a''')
    LOCATOR_YOUR_NAME_FIELD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_YOUR_EMAIL_FIELD = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_YOUR_CONTENT_FIELD = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_CONFIRM_BTN = (By.CSS_SELECTOR, 'button')
    
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
        
    def click_login_btn(self,):
        logging.info('Clicking login btn')
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()
    
    def get_err_text(self):
        err_field = self.find_element(TestSearchLocators.LOCATOR_ERR_LABEL, timer=3)
        text = err_field.text
        logging.info(f'Got text: {text} in error field: {TestSearchLocators.LOCATOR_ERR_LABEL[1]}')
        return text
    
    def get_blog_header(self):
        blog_header = self.find_element(TestSearchLocators.LOCATOR_BLOG_HEADER, timer=3)
        text = blog_header.text
        logging.info(f'Got text: {text} in blog header: {TestSearchLocators.LOCATOR_BLOG_HEADER[1]}')
        return text
    
    def click_new_post_btn(self):
        logging.info('Clicking new post btn')
        self.find_element(TestSearchLocators.LOCATOR_NEW_POST_BTN).click()

    def enter_new_post_title(self, text):
        logging.info(f'Sending {text} to element {TestSearchLocators.LOCATOR_NEW_POST_FIELD[1]}')
        new_post_title_field = self.find_element(TestSearchLocators.LOCATOR_NEW_POST_FIELD)
        new_post_title_field.clear
        new_post_title_field.send_keys(text)

    def click_new_post_confirm_btn(self):
        logging.info('Clicking new post confirm btn')
        self.find_element(TestSearchLocators.LOCATOR_NEW_POST_CONFIRM_BTN).click()

    def get_new_post_header(self):
        new_post_header = self.find_element(TestSearchLocators.LOCATOR_NEW_POST_HEADER, timer=3)
        text = new_post_header.text
        logging.info(f'Got text: {text} in new post header: {TestSearchLocators.LOCATOR_NEW_POST_HEADER[1]}')
        return text
    
    def click_contact_btn(self):
        logging.info('Clicking contact us btn')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()

    def click_contact_confirm_btn(self):
        logging.info('Clicking contact us confirm btn')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_CONFIRM_BTN).click()

    def enter_contact_name(self, text):
        logging.info(f'Sending {text} to element {TestSearchLocators.LOCATOR_YOUR_NAME_FIELD[1]}')
        contact_name_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_NAME_FIELD)
        contact_name_field.clear
        contact_name_field.send_keys(text)

    def enter_contact_email(self, text):
        logging.info(f'Sending {text} to element {TestSearchLocators.LOCATOR_YOUR_EMAIL_FIELD[1]}')
        contact_email_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_EMAIL_FIELD)
        contact_email_field.clear
        contact_email_field.send_keys(text)

    def enter_contact_content(self, text):
        logging.info(f'Sending {text} to element {TestSearchLocators.LOCATOR_YOUR_CONTENT_FIELD[1]}')
        contact_content_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_CONTENT_FIELD)
        contact_content_field.clear
        contact_content_field.send_keys(text)

    def get_contact_alert_text(self):
        blog_header = self.find_element(TestSearchLocators.LOCATOR_BLOG_HEADER, timer=3)
        text = blog_header.text
        logging.info(f'Got text: {text} in blog header: {TestSearchLocators.LOCATOR_BLOG_HEADER[1]}')
        return text
    

    