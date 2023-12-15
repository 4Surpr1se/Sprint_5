# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.quite()
from datetime import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestChromeRegistration:
    # todo переход на регистрацию
    def test_registration_chrome_driver_correct_registration(self, chromedriver_name_mail_pass_fields):
        chrome_driver, name_field, mail_field, pass_field = chromedriver_name_mail_pass_fields
        name_field.send_keys('name')
        mail_field.send_keys('dsaddsada13123@yandex.ru')
        pass_field.send_keys('password')
        chrome_driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 "
                                             "button_button_type_primary__1O7Bx "
                                             "button_button_size_medium__3zxIa']").click()
        # print(chrome_driver.page_source)
        WebDriverWait(chrome_driver, 5).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))
        # sleep(20)
        chrome_driver_current_url = chrome_driver.current_url
        # chrome_driver_page_source = chrome_driver.page_source
        chrome_driver.quit()
        # assert "Некорректный пароль" in chrome_driver.page_source, 'Некорректный пароль'
        assert chrome_driver_current_url == 'https://stellarburgers.nomoreparties.site/login', 'Нет Редиректа'
        # assert "Такой пользователь уже существует" in chrome_driver_page_source, 'Такой пользователь уже существует'

    def test_registration_chrome_driver_wrong_password(self, chromedriver_name_mail_pass_fields):
        chrome_driver, name_field, mail_field, pass_field = chromedriver_name_mail_pass_fields
        name_field.send_keys('name')
        mail_field.send_keys('mai3132sdals333231s31s323ca1das@yandex.ru')
        pass_field.send_keys('3')
        chrome_driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 "
                                             "button_button_type_primary__1O7Bx "
                                             "button_button_size_medium__3zxIa']").click()

        chrome_driver_page_source = chrome_driver.page_source
        chrome_driver.quit()
        assert "Некорректный пароль" in chrome_driver_page_source, 'Некорректный пароль'


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

        chrome_driver.close()

        assert self.after_button_click_url == 'https://stellarburgers.nomoreparties.site/login', \
            'было перехода по кнопке "Войти в аккаунт'
        assert self.after_login_url == 'https://stellarburgers.nomoreparties.site/', 'Не удалось войти'

    def test_login_chrome_driver_correct_personal_account(self, chrome_driver):
        chrome_driver.get("https://stellarburgers.nomoreparties.site")
        chrome_driver.find_element(By.XPATH,
                                   "//a[@href='/account']").click()

        self.after_login_url = self._login_page_filler(chrome_driver)
        chrome_driver.close()

        assert self.after_button_click_url == 'https://stellarburgers.nomoreparties.site/login', \
            'Не было перехода по кнопке "Личный Кабинет" '
        assert self.after_login_url == 'https://stellarburgers.nomoreparties.site/', 'Не удалось войти'

    def test_login_chrome_driver_correct_login_in_register(self, chrome_driver):
        chrome_driver.get("https://stellarburgers.nomoreparties.site/register")
        chrome_driver.find_element(By.XPATH,
                                   "//a[@href='/login']").click()

        self.after_login_url = self._login_page_filler(chrome_driver)
        chrome_driver.close()

        assert self.after_button_click_url == 'https://stellarburgers.nomoreparties.site/login', \
            'Не было перехода по кнопке "Войти" в форме регистрации'
        assert self.after_login_url == 'https://stellarburgers.nomoreparties.site/', 'Не удалось войти'

    def test_login_chrome_driver_correct_login_in_forgot_password(self, chrome_driver):
        chrome_driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        chrome_driver.find_element(By.XPATH,
                                   "//a[@href='/login']").click()

        self.after_login_url = self._login_page_filler(chrome_driver)
        chrome_driver.close()

        assert self.after_button_click_url == 'https://stellarburgers.nomoreparties.site/login', \
            'Не было перехода по кнопке "Войти" в форме восстановления пароля'
        assert self.after_login_url == 'https://stellarburgers.nomoreparties.site/', 'Не удалось войти'


class TestChromeAccount:

    def test_account_chrome_driver_correct_personal_account(self, chromedriver_logged_in):
        chromedriver_logged_in.find_element(By.XPATH,
                                            "//a[@href='/account']").click()

        WebDriverWait(chromedriver_logged_in, 5).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))

        current_url = chromedriver_logged_in.current_url

        assert current_url == 'https://stellarburgers.nomoreparties.site/account/profile', 'Не удалось войти в аккаунт через кнопку "личный кабинет" '

    def test_account_chrome_driver_correct_konstruct_redirect(self, chromedriver_logged_in):
        chromedriver_logged_in.get("https://stellarburgers.nomoreparties.site/account")

        konstruct, logo = chromedriver_logged_in.find_elements(By.XPATH,
                                                               "//a[@href='/']")
        konstruct.click()

        WebDriverWait(chromedriver_logged_in, 5).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

        after_konstruct_url = chromedriver_logged_in.current_url
        print('\n', after_konstruct_url, '\n')

        logo.click()

        WebDriverWait(chromedriver_logged_in, 5).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

        after_logo_url = chromedriver_logged_in.current_url
        print('\n', after_konstruct_url, '\n')
        chromedriver_logged_in.quit()
        assert after_konstruct_url == 'https://stellarburgers.nomoreparties.site/', 'Кнопка Конструктор не сработала'

        assert after_logo_url == 'https://stellarburgers.nomoreparties.site/', 'Кнопка лого не сработала'

    def test_account_chrome_driver_correct_log_out(self, chromedriver_logged_in):
        chromedriver_logged_in.get('https://stellarburgers.nomoreparties.site/account')
        WebDriverWait(chromedriver_logged_in, 5).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
        chromedriver_logged_in.find_element(By.XPATH,
                                            "//button[@class='Account_button__14Yp3 text text_type_main-medium "
                                            "text_color_inactive']").click()
        WebDriverWait(chromedriver_logged_in, 5).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))
        current_url = chromedriver_logged_in.current_url

        assert current_url == 'https://stellarburgers.nomoreparties.site/login', 'Выход не удался, ну дела'


class TestChromeKonstrukt:

    def test_1_kon(self, chrome_driver: webdriver.Chrome()):
        chrome_driver.get("https://stellarburgers.nomoreparties.site/")
        bulka, sauce, nachinka = chrome_driver.find_elements(By.XPATH,
                                                             "//div[contains(@style,'display: flex')]//div")
        # bulka.getAttribute(//xpath@class)
        # bulka.find_element(By.TAG_NAME('span')).click()
        sauce.click()
        sleep(5)
        sauce_class = sauce.get_attribute('class')
        print('\n', sauce_class, '\n')
        assert sauce_class == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
