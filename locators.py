from selenium.webdriver.common.by import By


class Locators:
    # Кнопки
    button_login_registration = (By.XPATH, ".//button[text()= 'Вход и регистрация']")
    button_no_account = (By.XPATH, ".//button[text()= 'Нет аккаунта']")
    button_create_account = (By.XPATH, ".//button[text()= 'Создать аккаунт']")
    button_login = (By.XPATH, ".//button[text()= 'Войти']")
    button_logout = (By.XPATH, ".//button[text()= 'Выйти']")
    button_cteate_ad = (By.XPATH, ".//button[text()= 'Разместить объявление']")
    button_avatar = (By.XPATH, ".//button[@class = 'circleSmall']")

    # Форма регистрации
    input_email = (By.NAME, "email")
    input_password = (By.NAME, "password")
    input_confirm_password = (By.NAME, "submitPassword")

    # Аватар и имя пользователя
    logo_avatar = (By.XPATH, "//h3[contains(@class, 'profileText name')]")
    profile_name = (By.XPATH, ".//h3[text()='User.']")

    #Ошибки валидации
    error_registration = (By.XPATH, ".//span[@class='input_span__yWPqB' and text()='Ошибка']")
    error_field = (By.XPATH,"//div[contains(@class, 'input_inputError__fLUP9')]")

    # Создание объявления
    popup_unauthorized = (By.XPATH, ".//h1[text()='Чтобы разместить объявление, авторизуйтесь']")
    input_name_ad = (By.XPATH, ".//input[@name='name']")
    input_description = (By.XPATH, ".//textarea[@name='description']")
    input_price = (By.XPATH, ".//input[@name='price']")
    dropdown_category = (By.XPATH, ".//input[@name='category']/following-sibling::button")
    dropdown_city = (By.XPATH, ".//input[@name='city']/following-sibling::button")
    select_category_book = (By.XPATH, ".//span[text()='Книги']")
    select_city_spb = (By.XPATH, ".//span[text()='Санкт-Петербург']")
    radio_button_ad = (By.CSS_SELECTOR, 'div.radioUnput_shell__Wtdwe input[value="Б/У"] + div.radioUnput_inputRegular__FbVbr')
    button_ad_publish = (By.XPATH, './/button[text() = "Опубликовать"]')
    button_apply = (By.XPATH, './/button[text() = "Применить"]')
    section_my_ads = (By.XPATH, "//h1[text()='Мои объявления']")
    last_ad = (By.XPATH, "//div[contains(@class, 'card')][.//h2[text()='Мастер и Маргарита']][last()]")
