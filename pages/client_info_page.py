from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Client_info_page(Base):


    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g


    #Lokators
    first_name = "//input[@id='first-name']"
    last_name = "//input[@id='last-name']"
    postal_code = "//input[@id='postal-code']"
    button_continue = "//input[@id='continue']"


    #Getters

    def get_first_name(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_postal_code(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.postal_code)))

    def get_button_continue(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_continue)))


    #Actions

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input first_name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input last_name")


    def input_postal_code(self, postal_code):
        self.get_postal_code().send_keys(postal_code)
        print("Input postal_code")

    def click_button_continue(self):
        self.get_button_continue().click()
        print("Click button_continue")


    # Methods
    def input_client_info(self):
        self.get_current_url()
        self.input_first_name("Nata")
        self.input_last_name("Ver")
        self.input_postal_code("493")
        self.click_button_continue()







