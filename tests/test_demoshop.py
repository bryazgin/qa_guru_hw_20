import requests
from selene import browser, have, be


def test_add_fiction_book_to_cart_from_catalog():
    result = requests.post('https://demowebshop.tricentis.com/login',
                           data={"Email": "test@emails.com", "Password": 12345678},
                           allow_redirects=False
                           )
    auth_cookie = result.cookies.get("NOPCOMMERCE.AUTH")
    add_result = requests.post('https://demowebshop.tricentis.com/addproducttocart/catalog/45/1/1',
                               cookies={"NOPCOMMERCE.AUTH": auth_cookie}
                               )
    assert add_result.status_code == 200

    browser.open('https://demowebshop.tricentis.com')
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": auth_cookie})
    browser.open('https://demowebshop.tricentis.com/cart')

    browser.element('.account').should(have.exact_text('test@emails.com'))
    browser.element('.cart-item-row').should(have.text('Fiction'))
    # падает, если в корзине уже есть другой товар. На подумать


def test_add_shoes_to_cart_from_detail():
    result = requests.post('https://demowebshop.tricentis.com/login',
                           data={"Email": "test@emails.com", "Password": 12345678},
                           allow_redirects=False
                           )
    auth_cookie = result.cookies.get("NOPCOMMERCE.AUTH")
    add_result = requests.post('https://demowebshop.tricentis.com/addproducttocart/details/28/1',
                               cookies={"NOPCOMMERCE.AUTH": auth_cookie},
                               data={"product_attribute_28_7_10": 26,
                                     "product_attribute_28_1_11": 29,
                                     "addtocart_28.EnteredQuantity": 1
                                     }
                               )
    assert add_result.status_code == 200

    browser.open('https://demowebshop.tricentis.com')
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": auth_cookie})
    browser.open('https://demowebshop.tricentis.com/cart')

    browser.element('.account').should(have.exact_text('test@emails.com'))
    browser.element('.cart-item-row').should(have.text('Blue and green Sneaker'))
    # добавить проверку размера

    # падает, если в корзине уже есть другой товар. На подумать
