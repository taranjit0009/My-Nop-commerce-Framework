import pytest
from selenium import webdriver
from utilities.read_properties import ReadConfig
from POM_Base.login import LoginAdmin
from selenium.webdriver.chrome.options import Options
from utilities.logger import LogMaker
#Driver(uc=True)
def pytest_addoption(parser):
    parser.addoption( "--browser", action="store", default="chrome", help="Specify the browser:chrome or firefox or edge")
@pytest.fixture(scope="function")
def setup(request):
    browser=request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()

    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver=webdriver.Edge()
    else:
        raise ValueError("Unsupported Browser.")
    driver.maximize_window()
    yield driver
    driver.close()
    # Add a finalizer to close the browser after tests
    # def teardown():
    #     driver.close()  # Closes the browser window
        # Alternatively, use driver.quit() to quit the WebDriver entirely
    #request.addfinalizer(teardown)

@pytest.fixture(scope="function")
def login_admin(setup):
    driver = setup
    login = LoginAdmin(driver)
    driver.get(ReadConfig.get_url())
    #perfrom login steps
    login.enter_username(ReadConfig.get_username())
    login.enter_password(ReadConfig.get_password())
    login.click_submit_button()
    return driver # Return the WebDriver instance for further use