import yaml
from testpage import OperationsHelper
import time
import logging

with open("config.yaml") as f:
    cfg = yaml.safe_load(f)

def test_step1(browser):
    logging.info('Test1 starting')
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login('test')
    test_page.enter_pas('test')
    test_page.click_login_btn()
    assert test_page.get_err_text() == '401'

# def test_step2(site, login_field, pas_field, log_btn, blog_head,
#                new_post_btn, new_post_title, new_post_desc, new_post_content, new_post_confirm_btn, new_post_result):
#     input1 = site.find_element("xpath", login_field)
#     input1.send_keys(cfg["user"])
#     input2 = site.find_element("xpath", pas_field)
#     input2.send_keys(cfg["pas"])
#     log_btn = site.find_element("xpath", log_btn)
#     log_btn.click()
#     login = site.find_element("xpath", blog_head)
#     assert login.text == "Blog"

    # homework2

    # time.sleep(1)
    # title = 'Test#'
    # new_post_btn = site.find_element("xpath", new_post_btn)
    # new_post_btn.click()
    # new_post_title = site.find_element("xpath", new_post_title)
    # new_post_title.send_keys(title)
    # new_post_confirm_btn = site.find_element("xpath", new_post_confirm_btn)
    # new_post_confirm_btn.click()
    # time.sleep(1)
    # new_post_result = site.find_element("xpath", new_post_result)
    # assert new_post_result.text == title

    # homework3

def test_step2(browser):
    logging.info('Test2 starting')
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login(cfg['user'])
    test_page.enter_pas(cfg['pas'])
    test_page.click_login_btn()
    assert test_page.get_blog_header() == 'Blog'

def test_step3(browser):
    logging.info('Test3 starting')
    test_page = OperationsHelper(browser)
    # time.sleep(1)
    title = 'Test#'
    test_page.click_new_post_btn()
    test_page.enter_new_post_title(title)
    test_page.click_new_post_confirm_btn()
    time.sleep(1)
    assert test_page.get_new_post_header() == title

def test_step4(browser):
    logging.info('Test4 starting')
    test_page = OperationsHelper(browser)
    # time.sleep(1)
    text = 'Test#'
    email = 'test@test'
    test_page.click_contact_btn()
    test_page.enter_contact_name(text)
    # time.sleep(1)
    test_page.enter_contact_email(email)
    # time.sleep(1)
    test_page.enter_contact_content(text)
    time.sleep(1)
    test_page.click_contact_confirm_btn()
    msg = test_page.switch_to_alert()
    logging.info(f'Got alert message: {msg}')
    assert msg != None

    
    