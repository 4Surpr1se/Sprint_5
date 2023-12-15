from time import sleep

from selenium.webdriver.support.wait import WebDriverWait


class TestChromeKonstrukt:

    def test_konstrukt_chrome_driver_sauce_scroll(self, chromedriver_bulka_sauce_nachinka):
        chrome_driver, bulka, sauce, nachinka = chromedriver_bulka_sauce_nachinka

        sauce.click()
        WebDriverWait(chrome_driver, 5)
        sauce_class = sauce.get_attribute('class')

        chrome_driver.quit()

        assert sauce_class == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'

    def test_konstrukt_chrome_driver_nachinka_scroll(self, chromedriver_bulka_sauce_nachinka):
        chrome_driver, bulka, sauce, nachinka = chromedriver_bulka_sauce_nachinka

        nachinka.click()
        WebDriverWait(chrome_driver, 5)
        nachinka_class = nachinka.get_attribute('class')

        chrome_driver.quit()

        assert nachinka_class == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'

    def test_konstrukt_chrome_driver_bulka_scroll(self, chromedriver_bulka_sauce_nachinka):
        chrome_driver, bulka, sauce, nachinka = chromedriver_bulka_sauce_nachinka

        nachinka.click()
        WebDriverWait(chrome_driver, 5)
        bulka.click()
        WebDriverWait(chrome_driver, 5)
        bulka_class = bulka.get_attribute('class')

        chrome_driver.quit()

        assert bulka_class == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
