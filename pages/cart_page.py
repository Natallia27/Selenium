from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger
import allure

class Cart_page(Base):


    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g


    #Lokators
    checkout = "//button[@id='checkout']"

    #Getters

    def button_checkout(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.checkout)))


    #Actions


    def click_button_checkout(self):
        self.button_checkout().click()
        print("Click button_checkout")

    # Methods
    def product_confirm(self):
        with allure.step("Product confirm"):
            Logger.add_start_step(method="product_confirm")
            self.get_current_url()
            self.click_button_checkout()
            Logger.add_end_step(url=self.driver_g.current_url, method="product_confirm")







