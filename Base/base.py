from utilities.read_properties import ReadConfig
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

class Base:
    @staticmethod
    def provide_url(self,url=ReadConfig.get_url()):
        return url

    @staticmethod
    def wait_for_visibility_of_element(driver,timeout,element):
        wait = WebDriverWait(driver,timeout)
        wait.until(EC.visibility_of_element_located(element))

    @staticmethod
    def wait_for_presence_of_element(driver,timeout,element):
        wait=WebDriverWait(driver,timeout)
        wait.until(EC.presence_of_element_located(element))

        """
        lamda
        fibonaci
        factoerial - itrative,
        kaskem
        recursion
        high order function and its usages
        guise game proggram via while loop
        git
        pr create 
        """
