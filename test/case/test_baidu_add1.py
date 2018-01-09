import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import Config, DRIVER_PATH
from utils.log_add import logger


class TestBaiDu(unittest.TestCase):
    URL = Config().get("URL")
    # base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    # driver_path = os.path.abspath(base_path + '\drivers\geckodriver.exe')

    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + "\chromedriver.exe")
        print(self.driver)
        self.driver.get(self.URL)

    def tearDown(self):
        self.driver.quit()

    def test_search_0(self):
        self.driver.find_element(*self.locator_kw).send_keys("python")
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            #print(link.text)
            logger.info(link.text)

    def test_search_2(self):
        self.driver.find_element(*self.locator_kw).send_keys("santiago")
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            #print(link.text)
            logger.info(link.text)


if __name__ == '__main__':
    unittest.main()