import yaml
from module import Site

with open("config.yaml") as f:
    cfg = yaml.safe_load(f)

# site = Site(testdata["address"])


def test_step1(site, login_field, pas_field, btn, err_label):
    # x_selector1 = """//*[@id="login"]/div[1]/label/input"""
    input1 = site.find_element("xpath", login_field)
    input1.send_keys("test")
    # x_selector2 = """//*[@id="login"]/div[2]/label/input"""
    input2 = site.find_element("xpath", pas_field)
    input2.send_keys("test")
    # btn_selector = "button"
    btn = site.find_element("xpath", btn)
    btn.click()
    # x_selector3 = """//*[@id="app"]/main/div/div/div[2]/h2"""
    err_lable = site.find_element("xpath", err_label)
    assert err_lable.text == "401"

def test_step2(site, login_field, pas_field, btn, blog_head):
    input1 = site.find_element("xpath", login_field)
    input1.send_keys(cfg["user"])
    input2 = site.find_element("xpath", pas_field)
    input2.send_keys(cfg["pas"])
    btn = site.find_element("xpath", btn)
    btn.click()
    login = site.find_element("xpath", blog_head)
    assert login.text == "Blog"