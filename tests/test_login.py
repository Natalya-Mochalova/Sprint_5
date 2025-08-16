from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions 
from data import Exist_User


class TestLoginPage:    
    def test_successful_login_with_valid_data(self, driver, open_main_page):         
        driver.find_element(*Locators.button_login_registration).click() # Нажатие кнопки "Вход и регистрация"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.input_email))
        driver.find_element(*Locators.input_email).send_keys(Exist_User.email)
        driver.find_element(*Locators.input_password).send_keys(Exist_User.password)
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.button_login))
        driver.find_element(*Locators.button_login).click() # Нажатие кнопки "Войти"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.logo_avatar)).text

        assert (driver.find_element(*Locators.logo_avatar)) and (driver.find_element(*Locators.profile_name).text == 'User.')
