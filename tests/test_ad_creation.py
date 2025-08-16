from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions 
from data import Ad


class TestAdCreation:
    def test_create_ad_unauthorized_user(self, driver, open_main_page):
        driver.find_element(*Locators.button_cteate_ad).click() # Нажатие кнопки "Разместить объявление"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.popup_unauthorized))
        
        assert driver.find_element(*Locators.popup_unauthorized)
    
    def test_create_ad_authorized_user(self, driver, open_main_page, login):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.logo_avatar)).text
        driver.find_element(*Locators.button_cteate_ad).click() # Нажатие кнопки "Разместить объявление"
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.input_name_ad))
        driver.find_element(*Locators.input_name_ad).send_keys(Ad.name)
        driver.find_element(*Locators.input_description).send_keys(Ad.description)
        driver.find_element(*Locators.input_price).send_keys(Ad.price)   
        driver.find_element(*Locators.dropdown_category).click()  # раскрытие списка категории
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.select_category_book))
        driver.find_element(*Locators.select_category_book).click() # Нажатие на категорию "Книги"
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.dropdown_city))
        driver.find_element(*Locators.dropdown_city).click()  # раскрытие списка городов
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.select_city_spb))
        driver.find_element(*Locators.select_city_spb).click() # Нажатие на город "Санкт-Петербург"
        driver.find_element(*Locators.radio_button_ad).click() # Выбор кнопки "Б/У"
        driver.find_element(*Locators.button_ad_publish).click() # Нажатие кнопки "Опубликовать"
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(Locators.button_apply)).text
        driver.find_element(*Locators.button_avatar).click() # Нажатие кнопки аватар
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.section_my_ads))
        element = driver.find_element(*Locators.section_my_ads)
        driver.execute_script("arguments[0].scrollIntoView();", element) # Скролл до блока "Мои объявления"

        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.last_ad)).is_displayed
