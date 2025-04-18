from selenium.webdriver.common.by import By
from utilities.logger import LogMaker
class LoginAdmin:

    TEXT_BOX_USERNAME_ID= "Email"
    TEXT_BOX_PASSWORD_ID = "Password"
    SUBMIT_BUTTON_XPATH= "//button[@type='submit']"
    LOG_OUT_LINK_TEXT = "Logout"

    def __init__(self,driver):
        self.driver= driver
        self.logger = LogMaker.custom_logger().getChild(self.__class__.__name__)

    def enter_username(self,username):
        self.driver.find_element(By.ID,self.TEXT_BOX_USERNAME_ID).clear()
        self.driver.find_element(By.ID,self.TEXT_BOX_USERNAME_ID).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.ID,self.TEXT_BOX_PASSWORD_ID).clear()
        self.driver.find_element(By.ID,self.TEXT_BOX_PASSWORD_ID).send_keys(password)

    def click_submit_button(self):
        self.driver.find_element(By.XPATH,self.SUBMIT_BUTTON_XPATH).click()

    def log_out_admin(self):
        self.driver.find_element(By.LINK_TEXT,self.LOG_OUT_LINK_TEXT).click()

