from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import random
import string


class TestChromeRegistration:

    def _random_char(self, char_num):
        return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

    def random_email(self, char_num):
        return self._random_char(char_num) + '@yandex.ru'

    def random_password(self, char_num):
        return self._random_char(char_num)

    # todo переход на регистрацию
    def test_registration_chrome_driver_correct_registration(self, chromedriver_name_mail_pass_fields):
        chrome_driver, name_field, mail_field, pass_field = chromedriver_name_mail_pass_fields
        name_field.send_keys('name')
        mail_field.send_keys(self.random_email(7))
        pass_field.send_keys(self.random_password(7))
        chrome_driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 "
                                             "button_button_type_primary__1O7Bx "
                                             "button_button_size_medium__3zxIa']").click()

        WebDriverWait(chrome_driver, 5).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))
        chrome_driver_current_url = chrome_driver.current_url

        chrome_driver.quit()
        assert chrome_driver_current_url == 'https://stellarburgers.nomoreparties.site/login', 'Нет Редиректа'

    def test_registration_chrome_driver_wrong_password(self, chromedriver_name_mail_pass_fields):
        chrome_driver, name_field, mail_field, pass_field = chromedriver_name_mail_pass_fields
        name_field.send_keys('name')
        mail_field.send_keys(self.random_email(7))
        pass_field.send_keys(self.random_password(3))
        chrome_driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 "
                                             "button_button_type_primary__1O7Bx "
                                             "button_button_size_medium__3zxIa']").click()

        chrome_driver_page_source = chrome_driver.page_source
        chrome_driver.quit()
        assert "Некорректный пароль" in chrome_driver_page_source, 'Некорректный пароль'


