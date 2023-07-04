from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger
import allure

class Finish_page(Base):


    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g


    # Methods
    def finish(self):
        with allure.step("Finish"):
            Logger.add_start_step(method="finish")
            self.get_current_url()
            self.get_assert_url("https://www.saucedemo.com/checkout-complete.html")
            self.get_screenshot()
            Logger.add_end_step(url=self.driver_g.current_url, method="finish")








