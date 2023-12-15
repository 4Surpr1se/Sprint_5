import time

import fixture as fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


# driver = webdriver.Firefox()
# print(driver.title)
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.quite()


class Tester:
    firefox_driver = webdriver.Firefox()
    chrome_driver = webdriver.Chrome()

    def registration(self):
        self._registration_chrome()

    def _registration_chrome(self):
        self.chrome_driver.get("https://stellarburgers.nomoreparties.site/register")
        name_field, mail_field, pass_field = self.chrome_driver.find_elements(By.XPATH,
                                                                              "//input[@class='text input__textfield "
                                                                              "text_type_main-default']")
        name_field.send_keys('name')
        mail_field.send_keys('3213213yandex.ru')
        pass_field.send_keys('password')
        self.chrome_driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 "
                                                  "button_button_type_primary__1O7Bx "
                                                  "button_button_size_medium__3zxIa']").click()
        print(self.chrome_driver.page_source)
        assert "Некорректный пароль" in self.chrome_driver.page_source, 'ddsa'
        assert "Такой пользователь уже существует" in self.chrome_driver.page_source, 'dsadsa'
        # time.sleep(100)

    def _registration_firefox(self):
        pass


Tester().registration()
