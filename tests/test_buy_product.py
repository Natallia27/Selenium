import time

import pytest
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


# @pytest.mark.run(order=2)
def test_buy_product_1(set_group):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\natal\\PycharmProjects\\resource\\chromedriver.exe')
    driver_g = webdriver.Chrome(options=options, service=g)

    print('Start test 1')

    login = Login_page(driver_g)
    login.authorization()
    mp = Main_page(driver_g)
    mp.add_product_1()
    cp = Cart_page(driver_g)
    cp.product_confirm()

    ii = Client_info_page(driver_g)
    ii.input_client_info()

    pay = Payment_page(driver_g)
    pay.payment()

    f = Finish_page(driver_g)
    f.get_screenshot()
    #
    print('Finish test 1')
    # time.sleep(5)
    driver_g.quit()


# @pytest.mark.run(order=3)
def test_buy_product_2(set_group):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\natal\\PycharmProjects\\resource\\chromedriver.exe')
    driver_g = webdriver.Chrome(options=options, service=g)

    print('Start test 2 ')

    login = Login_page(driver_g)
    login.authorization()
    mp = Main_page(driver_g)
    mp.add_product_2()
    cp = Cart_page(driver_g)
    cp.product_confirm()

    print('Finish test 2')
    time.sleep(5)
    driver_g.quit()


# @pytest.mark.run(order=1)
def test_buy_product_3():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\natal\\PycharmProjects\\resource\\chromedriver.exe')
    driver_g = webdriver.Chrome(options=options, service=g)

    print('Start test 3')

    login = Login_page(driver_g)
    login.authorization()
    mp = Main_page(driver_g)
    mp.add_product_3()
    cp = Cart_page(driver_g)
    cp.product_confirm()

    print('Finish test 3')
    # time.sleep(5)
    driver_g.quit()


