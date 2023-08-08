from selenium.webdriver.common.by import By

class Locator:
    def __init__(self, by, value):
        self.by = by
        self.value = value

# Кнопка "Вконтакте"
locator_btn_vk = Locator(By.ID, "oidc_vk")

# Кнопка "Одноклассники"
locator_btn_ok = Locator(By.ID, "oidc_ok")

# Кнопка "Mail.ru"
locator_btn_mail = Locator(By.ID, "oidc_mail")

# Кнопка "Яндекс"
locator_btn_yandex = Locator(By.ID, "oidc_ya")

# Кнопка "Почта" в табе
locator_tab_email = Locator(By.ID, "t-btn-tab-mail")

# Кнока "Телефон" в табе
locator_tab_phone = Locator(By.ID, "t-btn-tab-phone")

# Кнопка "Логин" в табе
locator_tab_login = Locator(By.ID, "t-btn-tab-login")

# Кнопка "Лицевой счет" в табе
locator_tab_personal_acc = Locator(By.ID, "t-btn-tab-ls")

# Поле ввода почты, телефона, логина, ЛС
locator_field_username = Locator(By.ID, "username")

# Поле для ввода пароля
locator_field_pass = Locator(By.ID, "password")

# Кнопка "Войти"
locator_btn_login = Locator(By.ID, 'kc-login')

# Кнопка "Выйти"
locator_btn_logout = Locator(By.ID, "logout-btn")

# Сообщение об ошибке авторизации
locator_error_message = Locator(By.ID, "form-error-message")

# Гиперссылка "Пользовательское соглашение"
locator_user_agreement = Locator(By.CLASS_NAME, "rt-link rt-link--orange")

# Гиперссылка "Пользовательское соглашение" в подвале страницы
locator_user_agreement_footer = Locator(By.CLASS_NAME, "rt-footer-left__item-accent")

# Кнопка "Забыли пароль"
locator_btn_forgot_password = Locator(By.ID, "forgot_password")

# Восстановление пароля
locator_pass_recovery = Locator(By.XPATH, "//*[@id="page-right"]/div[1]/div[1]/h1[1]")

# Кнопка "Зарегистрироваться"
locator_btn_register = Locator(By.ID, "kc-register")

# Регистрация
locator_register = Locator(By.XPATH, "//*[@id="page-right"]/div[1]/div[1]/h1[1]")


