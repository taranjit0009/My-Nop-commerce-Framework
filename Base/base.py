from utilities.read_properties import ReadConfig
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

class Base:
    @staticmethod
    def provide_url(self,url=ReadConfig.get_url()):
        return url

    @staticmethod
    def wait_for_visibilty_of_element(driver,timeout,element):
        wait = WebDriverWait(driver,timeout)
        wait.until(EC.visibility_of_element_located(element))

    @staticmethod
    def wait_for_prasence_of_element(driver,timeout,element):
        wait=WebDriverWait(driver,timeout)
        wait.until(EC.presence_of_element_located(element))
