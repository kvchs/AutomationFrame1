'''
使用HTMLTestRunner想生成测试报告，尝试了很多次了，就是无法生成，在网上百度搜索发现是快捷键问题

工具：Pycharm

Ctrl+Shift+F10运行不会生成脚本

Alt+Shift+F10运行生成脚本
'''
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH
from utils.log_add import logger
from utils.file_reader_add import ExcelReader
from utils.HTMLTestRunner_PY3 import HTMLTestRunner
import os


class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/baidu.xlsx'

    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def sub_setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        self.driver.get(self.URL)

    def sub_tearDown(self):
        self.driver.quit()

    def test_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.driver.find_element(*self.locator_kw).send_keys(d['search'])
                self.driver.find_element(*self.locator_su).click()
                time.sleep(2)
                links = self.driver.find_elements(*self.locator_result)
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()


if __name__ == '__main__':
    # testunit = unittest.TestSuite()
    # testunit.addTest(TestBaiDu("test_search"))
    report = REPORT_PATH + '\\report.html'
    print(os.path.abspath(report)+'dddddddddd')
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(stream=f, verbosity=2, title='从0搭建测试框架', description='html报告')
        runner.run(TestBaiDu("test_search"))