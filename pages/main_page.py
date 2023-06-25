from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Main_page(Base):


    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g


    #Lokators
    product_1add = "//button[@id='add-to-cart-sauce-labs-backpack']"
    product_2add = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    product_3add = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    cart = "//div[@id='shopping_cart_container']"
    menu = "//button[@id='react-burger-menu-btn']"
    link_about = "//a[@id='about_sidebar_link']"

    #Getters

    def get_product_1add(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_1add)))

    def get_product_2add(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_2add)))

    def get_product_3add(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_3add)))

    def get_cart(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_menu(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu)))

    def get_link_about(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_about)))



    #Actions


    def click_product_1add(self):
        self.get_product_1add().click()
        print("Click button_product_1add")

    def click_product_2add(self):
        self.get_product_1add().click()
        print("Click button_product_2add")

    def click_product_3add(self):
        self.get_product_1add().click()
        print("Click button_product_3add")



    def click_cart(self):
        self.get_cart().click()
        print("Click button_cart")

    def click_menu(self):
        self.get_menu().click()
        print("Click menu")

    def click_link_about(self):
        self.get_link_about().click()
        print("Click link_about")

    # Methods
    def add_product_1(self):
        self.get_current_url()
        self.click_product_1add()
        self.click_cart()

    def add_product_2(self):
        self.get_current_url()
        self.click_product_2add()
        self.click_cart()

    def add_product_3(self):
        self.get_current_url()
        self.click_product_3add()
        self.click_cart()
    def select_menu_about(self):
        self.get_current_url()
        self.click_menu()
        self.click_link_about()
        self.get_assert_url("https://saucelabs.com/")



