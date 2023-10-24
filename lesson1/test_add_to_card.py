from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_add_item():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    title_item4 = driver.find_element(By.XPATH, '//*[@id="item_5_title_link"]/div').text
    print(title_item4)



    add_button = driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-fleece-jacket"]')
    add_button.click()

    time.sleep(5)

    cart_button = driver.find_element(By.CSS_SELECTOR,'a[class="shopping_cart_link"]')
    cart_button.click()

    text_in_cart = driver.find_element(By.XPATH, '//*[@id="item_5_title_link"]/div').text

    time.sleep(5)

    assert title_item4==text_in_cart