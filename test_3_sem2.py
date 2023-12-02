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

def test_step2(site, login_field, pas_field, log_btn, blog_head,
               new_post_btn, new_post_title, new_post_desc, new_post_content, new_post_confirm_btn, new_post_result):
    input1 = site.find_element("xpath", login_field)
    input1.send_keys(cfg["user"])
    input2 = site.find_element("xpath", pas_field)
    input2.send_keys(cfg["pas"])
    log_btn = site.find_element("xpath", log_btn)
    log_btn.click()
    login = site.find_element("xpath", blog_head)
    assert login.text == "Blog"

    # homework2

    time.sleep(1)
    title = 'Test#'
    new_post_btn = site.find_element("xpath", new_post_btn)
    new_post_btn.click()
    new_post_title = site.find_element("xpath", new_post_title)
    new_post_title.send_keys(title)
    new_post_confirm_btn = site.find_element("xpath", new_post_confirm_btn)
    new_post_confirm_btn.click()
    time.sleep(1)
    new_post_result = site.find_element("xpath", new_post_result)
    assert new_post_result.text == title