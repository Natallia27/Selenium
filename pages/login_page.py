from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Login_page(Base):

    url = 'https://www.saucedemo.com/'

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g


    #Lokators
    user_name = "//input[@id='user-name']"
    password = "//*[@id='password']"
    button_login = "//*[@id='login-button']"
    main_word = "//span[@class='title']"


    #Getters

    def get_user_name(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_button_login(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))

    def get_main_word(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    #Actions

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user_name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input user_name")

    def click_button_login(self):
        self.get_button_login().click()
        print("Click button_login")

    # Methods
    def authorization(self):
        self.driver_g.get(self.url)
        self.driver_g.maximize_window()
        self.get_current_url()
        self.input_user_name("standard_user")
        self.input_password("secret_sauce")
        self.click_button_login()
        self.get_assert_word(self.get_main_word(), 'Products')







