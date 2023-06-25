from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Payment_page(Base):


    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g


    #Lokators
    button_finish = "//button[@id='finish']"

    #Getters

    def get_button_finish(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_finish)))

    #Actions


    def click_button_finish(self):
        self.get_button_finish().click()
        print("Click button_finish")


    # Methods
    def payment(self):
        self.get_current_url()
        self.click_button_finish()








