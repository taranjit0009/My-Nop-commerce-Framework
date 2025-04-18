import time

from POM_Base.login import LoginAdmin
from utilities.read_properties import ReadConfig
from utilities.logger import LogMaker
logger = LogMaker.custom_logger(__name__)
class TestLoginAdmin:
    def test_login_admin(self,setup):
        self.driver = setup
        login = LoginAdmin(self.driver)
        self.driver.get(ReadConfig.get_url())
        logger.info("URL is successfully launched.")
        #Perform login steps
        login.enter_username(ReadConfig.get_username())
        login.enter_password(ReadConfig.get_password())
        login.click_submit_button()
        logger.info("User is Logged in.")

        time.sleep(2)
    def test_login(self,setup):
        self.driver=setup
        self.driver.get(ReadConfig.get_url())
        # Fetch and validate the login page title
        actual_title = self.driver.title
        assert actual_title == ReadConfig.get_expected_title(), print("expected title is not matched.")
        print("Expected title is matched.")

    def test_invalid_user(self,setup):
        self.driver = setup
        login=LoginAdmin(self.driver)
        self.driver.get(ReadConfig.get_url())
        login.enter_username(ReadConfig.get_invalid_username())
        login.enter_password(ReadConfig.get_password())
        login.click_submit_button()

    def test_only_call(self,login_admin):
        self.driver=login_admin



