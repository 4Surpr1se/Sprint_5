from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestChromeLogin:

    def _login_page_filler(self, chrome_driver):
        WebDriverWait(chrome_driver, 5).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))

        self.after_button_click_url = chrome_driver.current_url

        mail_field, pass_field = chrome_driver.find_elements(By.XPATH,
                                                             "//input[@class='text input__textfield "
                                                             "text_type_main-default']")

        mail_field.send_keys('231@mail.ru')
        pass_field.send_keys('postgres')

        chrome_driver.find_element(By.XPATH,
                                   "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx"
                                   " button_button_size_medium__3zxIa']").click()

        WebDriverWait(chrome_driver, 5).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

        return chrome_driver.current_url

    def test_login_chrome_driver_correct_login_to_account(self, chrome_driver):
        chrome_driver.get("https://stellarburgers.nomoreparties.site")
        chrome_driver.find_element(By.XPATH,
                                   "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx "
                                   "button_button_size_large__G21Vg']").click()

        self.after_login_url = self._login_page_filler(chrome_driver)

        chrome_driver.quit()

        assert self.after_button_click_url == 'https://stellarburgers.nomoreparties.site/login', \
            'было перехода по кнопке "Войти в аккаунт'
        assert self.after_login_url == 'https://stellarburgers.nomoreparties.site/', 'Не удалось войти'

    def test_login_chrome_driver_correct_personal_account(self, chrome_driver):
        chrome_driver.get("https://stellarburgers.nomoreparties.site")
        chrome_driver.find_element(By.XPATH,
                                   "//a[@href='/account']").click()

        self.after_login_url = self._login_page_filler(chrome_driver)
        chrome_driver.quit()

        assert self.after_button_click_url == 'https://stellarburgers.nomoreparties.site/login', \
            'Не было перехода по кнопке "Личный Кабинет" '
        assert self.after_login_url == 'https://stellarburgers.nomoreparties.site/', 'Не удалось войти'

    def test_login_chrome_driver_correct_login_in_register(self, chrome_driver):
        chrome_driver.get("https://stellarburgers.nomoreparties.site/register")
        chrome_driver.find_element(By.XPATH,
                                   "//a[@href='/login']").click()

        self.after_login_url = self._login_page_filler(chrome_driver)
        chrome_driver.quit()

        assert self.after_button_click_url == 'https://stellarburgers.nomoreparties.site/login', \
            'Не было перехода по кнопке "Войти" в форме регистрации'
        assert self.after_login_url == 'https://stellarburgers.nomoreparties.site/', 'Не удалось войти'

    def test_login_chrome_driver_correct_login_in_forgot_password(self, chrome_driver):
        chrome_driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        chrome_driver.find_element(By.XPATH,
                                   "//a[@href='/login']").click()

        self.after_login_url = self._login_page_filler(chrome_driver)

        chrome_driver.quit()

        assert self.after_button_click_url == 'https://stellarburgers.nomoreparties.site/login', \
            'Не было перехода по кнопке "Войти" в форме восстановления пароля'
        assert self.after_login_url == 'https://stellarburgers.nomoreparties.site/', 'Не удалось войти'
