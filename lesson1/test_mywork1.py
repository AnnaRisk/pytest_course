from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
def test_valid_login():

    driver.get("https://www.saucedemo.com/")

    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()

    time.sleep(5)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"


def test_invalid_login():
    driver.get("https://www.saucedemo.com/")

    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username.send_keys("user")
    password.send_keys("user")
    login_button.click()
    time.sleep(3)
    error_message = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]").text
    # assertEqual(error_message, "Epic sadface: Username and password do not match any user in this service")

    # assert error_message.text == 'Epic sadface: Username and password do not match any user in this service'

    expected_error_message = 'Epic sadface: Username and password do not match any user in this service'
    assert error_message == expected_error_message


def test_cart():
    # Открытие веб-сайта
    driver.get("https://www.saucedemo.com/")

    # Логин на сайте (замените на актуальные логин и пароль)
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()

    # Добавление товара в корзину через каталог
    add_to_cart_buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    add_to_cart_buttons[0].click()

    time.sleep(3)

    title_item4 = driver.find_element(By.XPATH, '//*[@id="item_5_title_link"]/div').text
    print(title_item4)

    add_button = driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-fleece-jacket"]')
    add_button.click()

    time.sleep(5)

    text_in_cart = driver.find_element(By.XPATH, '//*[@id="item_5_title_link"]/div').text

    time.sleep(5)


    # # Переход в корзину
    cart_button = driver.find_element(By.CSS_SELECTOR, 'a[class="shopping_cart_link"]')
    cart_button.click()
    assert title_item4 == text_in_cart
    time.sleep(5)

    # # Удаление товара из корзины через корзину
    remove_buttons = driver.find_elements(By.CLASS_NAME, "btn_secondary")
    remove_buttons[0].click()

    time.sleep(5)

    # # Возвращение на главную страницу
    continue_shopping_button = driver.find_element(By.CSS_SELECTOR, "#continue-shopping")
    continue_shopping_button.click()
    time.sleep(5)



    # # Возвращение на главную страницу
    # continue_shopping_button = driver.find_element(By.CSS_SELECTOR, "#continue-shopping")
    # continue_shopping_button.click()

    # Добавление товара в корзину из карточки товара
    add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="item_0_title_link"]/div')
    add_to_cart_button.click()
    time.sleep(3)

    # add_to_cart_from_card = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-fleece-jacket")
    add_to_cart_from_card = driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-bike-light"]')
    add_to_cart_from_card.click()

    time.sleep(3)


    # Удаление товара из корзины через карточку товара
    remove_buttons2 = driver.find_elements(By.CSS_SELECTOR, 'button[data-test="remove-sauce-labs-bike-light"]')
    remove_buttons2[0].click()

    time.sleep(3)

    back_to_list = driver.find_elements(By.CSS_SELECTOR, 'button[data-test="back-to-products"]')
    back_to_list[0].click()


    # Завершение теста
    # driver.quit()

def test_order():
    # Открытие сайта
    driver.get("https://www.saucedemo.com/")

    # Вход на сайт с корректными данными
    username = "standard_user"
    password = "secret_sauce"

    # Заполнение полей логина и пароля
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)

    # Нажатие на кнопку "Login"
    driver.find_element(By.ID, "login-button").click()

    # Добавление товара в корзину (пример: первый товар)
    driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']").click()
    driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()

    # Переход в корзину
    driver.find_element(By.ID, "shopping_cart_container").click()

    # Оформление заказа
    driver.find_element(By.ID, "checkout").click()

    # Заполнение данных для оформления заказа
    first_name = "John"
    last_name = "Doe"
    postal_code = "12345"

    driver.find_element(By.ID, "first-name").send_keys(first_name)
    driver.find_element(By.ID, "last-name").send_keys(last_name)
    driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    # Нажатие на кнопку "Continue"
    driver.find_element(By.ID, "continue").click()

    # Подтверждение заказа
    driver.find_element(By.ID, "finish").click()

    # Проверка успешного оформления заказа (может варьироваться в зависимости от сайта)
    order_confirmation = driver.find_element(By.XPATH, '//*[@id="checkout_complete_container"]/h2').text
    assert "Thank you for your order!" in order_confirmation

    # Закрытие браузера
    # driver.quit()


def test_filter():
    # Открытие сайта
    driver.get("https://www.saucedemo.com/")

    # Вход на сайт с корректными данными
    username = "standard_user"
    password = "secret_sauce"

    # Заполнение полей логина и пароля
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)

    # Нажатие на кнопку "Login"
    driver.find_element(By.ID, "login-button").click()

    # Выбор фильтра A to Z
    sort_filter = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_filter.select_by_value("az")

    # Получение списка названий товаров
    product_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    product_names = [element.text for element in product_elements]

    # Проверка, что товары отсортированы в алфавитном порядке
    sorted_product_names = sorted(product_names)
    assert product_names == sorted_product_names, "Товары не отсортированы в алфавитном порядке"

    # Выбор фильтра Z to A
    sort_filter.select_by_value("za")


    # Выбор фильтра low to high
    # Поиск элемента после входа на сайт и перед выбором значения
    sort_filter = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_filter.select_by_value("lohi")



    # Выбор фильтра high to low
    # Поиск элемента после входа на сайт и перед выбором значения
    sort_filter = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_filter.select_by_value("hilo")


    # Закрытие браузера
    # driver.quit()


def test_menu():
    # Открытие сайта
    driver.get("https://www.saucedemo.com/")

    # Авторизация с корректными данными
    username = "standard_user"
    password = "secret_sauce"
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    # Открытие бургер-меню
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    menu_button.click()

    # Проверка кнопки "About" в меню
    about_button = driver.find_element(By.XPATH, '//*[@id="about_sidebar_link"]')
    time.sleep(3)
    about_button.click()
    time.sleep(3)
    # about_header = driver.find_element(By.CLASS_NAME, 'p[class="MuiTypography-root MuiTypography-body1 css-sere2z"]')
    about_header = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[1]/div/div[3]/p')
    assert about_header.text == "The world relies on your code. Test on thousands of different device, browser, and OS configurations–anywhere, any time."

    # Открытие сайта
    driver.get("https://www.saucedemo.com/")

    # Авторизация с корректными данными
    username = "standard_user"
    password = "secret_sauce"
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    # Открытие бургер-меню
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    menu_button.click()

    # Проверка кнопки "Reset App State" в меню
    reset_button = driver.find_element(By.ID, "reset_sidebar_link")
    reset_button.click()
    # reset_message = driver.find_element(By.CLASS_NAME, "subheader")
    # assert reset_message.text == "PRODUCTS", "Кнопка 'Reset App State' не работает"

    # Открытие сайта
    driver.get("https://www.saucedemo.com/")

    # Авторизация с корректными данными
    username = "standard_user"
    password = "secret_sauce"
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    # Открытие бургер-меню
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    menu_button.click()

    # Выход из системы
    logout_button = driver.find_element(By.ID, "logout_sidebar_link")
    logout_button.click()
    login_button = driver.find_element(By.ID, "login-button")
    assert login_button.is_displayed(), "Выход из системы не работает"

    # Завершение теста
    # driver.quit()