import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from base.base_class import Base
from menus.filters import Filters
from pages.cart_page import CartPage
from pages.main_page import MainPage
from menus.catalog_menu import CatalogMenu
from pages.order_page import OrderPage
from pages.products_page import ProductPage

options = Options()
prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
options.add_experimental_option("prefs", prefs)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--start-maximized")


def test_buy_processor_amd_ryzen_7_7700(set_up):
    total_cost_var = 0
    path = 'C:\\Users\\swert\\PycharmProjects\\resource\\chromedriver.exe'
    driver = webdriver.Chrome(service=Service(path), options=options)

    main = MainPage(driver)
    main.open_main_page()
    main.open_catalog()

    catalog = CatalogMenu(driver)
    catalog.open_catalog_processor()

    filters = Filters(driver)
    filters.move_filters_menu()
    filters.select_brand_processor_amd()
    filters.select_series_ryzen_7()
    filters.select_socket_am5()
    filters.select_generation_ryzen_7000()
    filters.select_apply_filters()

    product = ProductPage(driver)
    Base.assert_word(driver, product.get_main_word_page(), 'Процессоры')
    product.select_add_cart_product_1()
    Base.assert_word(driver, product.get_check_product_in_modal_window(), 'Процессор AMD Ryzen 7 7700, AM5, OEM [100-000000592]')
    product.click_get_buton_close_modal_window()

    main.select_cart()

    cart = CartPage(driver)
    cart.select_button_make_order_unauthorized()

    order = OrderPage(driver)
    order.entry_recipients_details()
    order.select_receipt_and_payment_delivery()

    order.check_place_an_order() #Не стал нажимать на кнопку чтобы не создался заказ
