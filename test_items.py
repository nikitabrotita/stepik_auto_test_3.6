import pytest
from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestMainPage1():
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("start test")
        browser.get(link)
        time.sleep(30)
        add_to_basket = browser.find_element_by_css_selector(".btn-primary")
        assert add_to_basket, 'кнопка добавления в корзину не существует'
        print("finish test")
