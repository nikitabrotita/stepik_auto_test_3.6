import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_basket_link_on_the_main_page(self, browser):
    print("start test")
    browser.get(link)
    sleep(30)
    add_to_basket = browser.find_element_by_css_selector(".btn-primary")
    print("finish test")
    assert add_to_basket, 'кнопка добавления товара не существует'
