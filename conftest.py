import pytest
from selenium import webdriver


# Как сделать чтобы можно было передавать параметры в pytest. браузер стал параметром. copy function from google.
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests")
    parser.addoption("--driver_folder", action="store", default="C:\\selenium", help="Folder with stored drivers")
    parser.addoption("--url", action="store", default="https://demo.opencart.com/",
                     help="url to run tests")  # to call in terminal


@pytest.fixture
def url(request):
    return request.config.getoption("--url")  # save url to fixture


@pytest.fixture
def browser(request):
    browser_option = request.config.getoption("--browser")
    driver_folder = request.config.getoption("--driver_folder")

    if browser_option == "chrome":
        driver = webdriver.Chrome(executable_path="{}\\chromedriver.exe".format(driver_folder))
    elif browser_option == "firefox":
        driver = webdriver.Firefox(executable_path="{}\\geckodriver.exe".format(driver_folder))
    elif browser_option == "edge":
        driver = webdriver.Edge(executable_path="{}\\msedgedriver.exe".format(driver_folder))
    else:
        raise ValueError("This driver: {} is not supported".format(browser_option))

    driver.maximize_window()
    request.addfinalizer(driver.quit)
    return driver
