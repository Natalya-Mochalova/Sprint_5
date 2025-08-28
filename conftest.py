import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from urls import Urls
from data import Exist_User


@pytest.fixture # Создание драйвера
def driver():
    driver = webdriver.Chrome()
    yield driver 
    driver.quit()

@pytest.fixture # Открытие главной страницы
def open_main_page(driver):
    driver.get(Urls.url_main_page)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_login_registration))

@pytest.fixture # Login пользователя
def login(driver, open_main_page):         
    open_main_page
    driver.find_element(*Locators.button_login_registration).click() # Нажатие кнопки "Вход и регистрация"
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.input_email))
    driver.find_element(*Locators.input_email).send_keys(Exist_User.email)
    driver.find_element(*Locators.input_password).send_keys(Exist_User.password)
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.button_login))
    driver.find_element(*Locators.button_login).click() # Нажатие кнопки "Войти"