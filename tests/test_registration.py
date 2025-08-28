from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions 
import helpers
from urls import Urls
from data import Invalid_Data, Exist_User


class TestRegistrationPage:    
    def test_successful_registration_with_valid_data(self, driver, open_main_page):         
        email = helpers.generation_email()
        password = helpers.generation_password()
        driver.find_element(*Locators.button_login_registration).click() # Нажатие кнопки "Вход и регистрация"
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.button_no_account))
        driver.find_element(*Locators.button_no_account).click() # Нажатие кнопки "Нет аккаунта"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.input_email))
        driver.find_element(*Locators.input_email).send_keys(email)
        driver.find_element(*Locators.input_password).send_keys(password)
        driver.find_element(*Locators.input_confirm_password).send_keys(password)
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.button_create_account))
        driver.find_element(*Locators.button_create_account).click() # нажатие кнопки "Создать аккаунт"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.logo_avatar)).text
        
        assert (driver.current_url == Urls.url_registration) and (driver.find_element(*Locators.logo_avatar)) and (driver.find_element(*Locators.profile_name).text == 'User.')
    
    def test_registration_email_is_incorrect_error_message(self, driver, open_main_page):         
        driver.find_element(*Locators.button_login_registration).click() # Нажатие кнопки "Вход и регистрация"
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.button_no_account))
        driver.find_element(*Locators.button_no_account).click() # Нажатие кнопки "Нет аккаунта"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.input_email))
        driver.find_element(*Locators.input_email).send_keys(Invalid_Data.invalid_email)
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.button_create_account))
        driver.find_element(*Locators.button_create_account).click() # нажатие кнопки "Создать аккаунт"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.error_registration))
        
        assert driver.find_element(*Locators.error_registration) and driver.find_element(*Locators.error_field)
    
    def test_registration_existing_user_error_message(self, driver, open_main_page):         
        driver.find_element(*Locators.button_login_registration).click() # Нажатие кнопки "Вход и регистрация"
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.button_no_account))
        driver.find_element(*Locators.button_no_account).click() # Нажатие кнопки "Нет аккаунта"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.input_email))
        driver.find_element(*Locators.input_email).send_keys(Exist_User.email)
        driver.find_element(*Locators.input_password).send_keys(Exist_User.password)
        driver.find_element(*Locators.input_confirm_password).send_keys(Exist_User.password)
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.button_create_account))
        driver.find_element(*Locators.button_create_account).click() # нажатие кнопки "Создать аккаунт"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.error_registration))

        assert driver.find_element(*Locators.error_registration) and driver.find_element(*Locators.error_field)
        