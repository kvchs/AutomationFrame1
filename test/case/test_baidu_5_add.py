import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH
from utils.log_add import logger
from utils.file_reader_add import ExcelReader
from utils.HTMLTestRunner_PY3 import HTMLTestRunner
from utils.mail_add import Email
from test.page.baidu_result_page import BaiDuMainPage, BaiDuResultPage


class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/baidu.xlsx'

    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def sub_setUp(self):
        self.page = BaiDuMainPage(browser_type='chrome').get(self.URL,maximize_window=True)

    def sub_tearDown(self):
        self.page.quit()

    def test_search(self):
        datas = ExcelReader(self.excel).data
        print(datas)
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.page.search(d["search"])
                time.sleep(3)
                self.page = BaiDuResultPage(self.page)
                links = self.page.result_links
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()


if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    print("open file")
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='从0搭建测试框架 灰蓝', description='修改html报告')
        runner.run(TestBaiDu('test_search'))
    e = Email(title='百度搜素测试报告',
              message='这是今天的测试报告，请查收！',
              receiver='149033**51@qq.com',
              server='smtp.163.com',
              sender='15680**8752@163.com',
              password='m***2de',
              path=report
              )
    e.send()
