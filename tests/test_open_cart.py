import time


# Test that checks availability of all links on top-bar in opencart.
def test_top_links(browser, url):
    browser.get(url)
    top_bar = len(browser.find_elements_by_css_selector("#top-links li"))
    assert top_bar == 7


# Test that checks availability of currency button in top panel
def test_currency_btn(browser, url):
    browser.get(url)
    browser.find_element_by_css_selector(".dropdown-toggle")


# Test that checks availability of all elements on admin login panel.
def test_admin_login(browser, url):
    browser.get(url + "admin")
    browser.find_element_by_css_selector("#input-username")
    browser.find_element_by_css_selector("#input-password")
    browser.find_element_by_link_text("Forgotten Password")
    browser.find_element_by_css_selector("button[type='submit']")


# Test that checks search input and cart button on main page.
def test_search_input_and_cart(browser, url):
    browser.get(url)
    search_field = browser.find_element_by_css_selector(".input-lg")
    search_button = browser.find_element_by_css_selector(".input-group-btn")
    search_field.click()
    search_field.send_keys("Iphone")
    search_button.click()
    add_cart = browser.find_element_by_css_selector(".button-group .fa-shopping-cart")
    time.sleep(1)
    add_cart.click()
    open_cart = browser.find_element_by_css_selector(".btn-block .dropdown-toggle")
    time.sleep(1)
    open_cart.click()
    item_in_cart = browser.find_element_by_link_text("iPhone")
    item_in_cart.click()
    assert browser.title == "iPhone"
