import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.client_info_page import Client_info_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.cart_page import Cart_page
from pages.payment_page import Payment_page
import allure

@allure.description("Test link about")
def test_link_about(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\natal\\PycharmProjects\\resource\\chromedriver.exe')
    driver_g = webdriver.Chrome(options=options, service=g)

    print('Start test')

    login = Login_page(driver_g)
    login.authorization()

    mp = Main_page(driver_g)
    mp.select_menu_about()


    print("Finish test")
    # time.sleep(5)
    driver_g.quit()



