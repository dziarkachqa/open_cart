from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# # Test that checks search input and cart button on main page.
def test_search_input_and_cart(browser, url):
    explicit_wait = WebDriverWait(browser, 3)
    browser.get(url)
    search_field = browser.find_element_by_css_selector(".input-lg")
    search_button = browser.find_element_by_css_selector(".input-group-btn")
    search_field.click()
    search_field.send_keys("Iphone")
    search_button.click()
    explicit_wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".button-group .fa-shopping-cart")))  # жду видимости элемента
    add_cart = browser.find_element_by_css_selector(".button-group .fa-shopping-cart")
    add_cart.click()
    open_cart = browser.find_element_by_css_selector(".btn-block .dropdown-toggle")
    open_cart.click()
    item_in_cart = browser.find_element_by_link_text("iPhone")
    item_in_cart.click()
    assert browser.title == "iPhone"


# Test Category Panel
# check Categories panel transforms when screen minimized,
# panel has the "hamburger" menu and it contains the same Categories
# as full screen has.
def test_category_panel(browser, url):
    explicit_wait = WebDriverWait(browser, 3)
    browser.get(url)
    # check how many product Categories Category panel contains
    product_categories = len(browser.find_elements_by_css_selector(".navbar-nav > li"))
    assert product_categories == 8
    browser.set_window_size(750, 820)
    # check hamburger menu is present
    explicit_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".fa-bars")))
    hamburger_menu_btn = browser.find_element_by_css_selector(".fa-bars")
    assert hamburger_menu_btn.is_displayed() == True
    hamburger_menu_btn.click()
    # check product Categories list dropped down
    product_categories_collapse = browser.find_element_by_css_selector(".navbar-collapse")
    assert product_categories_collapse.is_displayed() == True
    # check the word Categories is present
    panel_name = browser.find_element_by_css_selector(".visible-xs").text
    assert panel_name == "Categories"
