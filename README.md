## Финальный проект 5 спринта на тему "UI-тестирование". Тестирование сайта DOSKA

##### Тест 1: test_registration
Включает в себя тесты:
- test_successful_registration_with_valid_data (Регистрация пользователя)
- test_registration_email_is_incorrect_error_message (Регистрация пользователя c email не по маске)
- test_registration_existing_user_error_message (Регистрация уже существующего пользователя)

##### Тест 2: test_login
Включает в себя тест:
- test_successful_login_with_valid_data (Login пользователя)

##### Тест 3: test_logout
Включает в себя тест:
- test_successful_logout (Logout пользователя)

##### Тест 4: test_ad_creation
Включает в себя тесты:
- test_create_ad_unauthorized_user (Создание объявления неавторизованным пользователем)
- test_create_ad_authorized_user (Создание объявления авторизованным пользователем)

conftest.py - содержит фикстуры

data.py - содержит переменные для учетной записи (логин, пароль) и объявления

helpers.py - содержит вспомогательные функции

locators.py - содержит все локаторы 

urls.py - содержит используемые urls

