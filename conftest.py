import pytest
from selenium import webdriver

# Как сделать чтобы можно было передавать параметры в pytest. браузер стал параметром. copy function from google.
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests")
    parser.addoption("--driver_folder", action="store", default="C:\\selenium", help="Folder with stored drivers")
    parser.addoption("--url",action="store", default="https://demo.opencart.com/", help="url to run tests" ) # to call in terminal


@pytest.fixture
def url(request):
    return request.config.getoption("--url") # save url to fixture

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




# И как забрать параметр. возвращаемся к примеру в гугле и копируем как забрать параметр и всталляю
# копируем самую последнюю часть из фикстуры из того же примера на гугле
# @pytest.fixture
# def cmdopt(request):
#     return request.config.getoption("--cmdopt")


# @pytest.fixture
# def chrome_browser(request):
#     # создать обьект driver и зафиксировать его
#     driver = webdriver.Chrome(executable_path="C:\\selenium\\chromedriver.exe")
#     # добавить finalizer
#     request.addfinalizer(driver.close)  # не ставить()  в концу ф-ции driver.close. Она вызовется только тогда
#     # когда код дойдет до нужного места.Когда код внутри всей ф_ции выполниться он дернет метод
#     return driver
#
#
# @pytest.fixture
# def firefox_browser(request):
#     driver = webdriver.Firefox(executable_path="C:\\selenium\\geckodriver.exe")
#     request.addfinalizer(driver.close)
#     return driver
#
#
# @pytest.fixture
# def edge_browser(request):
#     driver = webdriver.Edge(executable_path="C:\\selenium\\msedgedriver.exe")
#     request.addfinalizer(driver.close)
#     return driver
