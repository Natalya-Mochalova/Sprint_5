from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions 


class TestLogout:    
    def test_successful_logout(self, driver, open_main_page, login):         
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_logout))
        driver.find_element(*Locators.button_logout).click() # Нажатие кнопки "Выйти"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_login_registration))

        assert driver.find_element(*Locators.button_login_registration)

