import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from openpyxl import Workbook, load_workbook
from login_orangehrm import web_page    
from read_excel import ex_read

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

@pytest.fixture()
def read_test_data(file_path=r"C:\Users\sarit\OneDrive\Documents\user_input_file.xlsx",sheet_name='Sheet1'):
    global input_file
    input_file=ex_read(r"C:\Users\sarit\OneDrive\Documents\user_input_file.xlsx")
    return input_file.readdata()

@pytest.mark.parametrize('n', range(1,6))
def test_case1(driver,read_test_data,n):
    obj1=web_page(driver)
    obj1.open_page("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    obj1.login_page(read_test_data[n]["User Name"],read_test_data[n]["Password"])
    global input_file
    input_file.updatecellvalue(n+1,7,"pass")


# LOGIN_USERNAME = ["admin", "test1", "test2", "test3"]
# LOGIN_PASSWORD = ["test123", "Test@1234", "Test@1234", "Test@1234"]
# ###LOGIN_USERNAME = ["admin"]
# ###LOGIN_PASSWORD = ["test123"]
# lst = range(len(LOGIN_USERNAME))
# iteration_count = 2
# global output_data_set
# output_data_set = {}
# csv_file_name = 'SMx_WorFlow_Performance.csv'
#
# DEVICE_NAME = "Suresh-sandbox"
# Node = ['E3-2']
# ONT_SUBSCRIBERS = ['testSubA1', 'testSubB2', 'testSubC3', 'testSubD4', 'testSubE5', 'testSubF1', 'testSubG2',
#                    'testSubH3', 'testSubI4', 'testSubJ5']
# ONT_SUBSCRIBERS_SERVICES = ['VirtualtestSubA1ONT', 'VirtualtestSubB2ONT', 'VirtualtestSubC3ONT', 'VirtualtestSubD4ONT',
#                             'VirtualtestSubE5ONT', 'VirtualtestSubF1ONT', 'VirtualtestSubG2ONT', 'VirtualtestSubH3ONT',
#                             'VirtualtestSubI4ONT', 'VirtualtestSubJ5ONT']
#
#
# # Test Cases
# @pytest.mark.parametrize('n', lst)
# def test_work_flow(playwright: Playwright, n):
#     """Log into and then log out of SMx"""
#
#     global output_data_set
#     output_data_set[LOGIN_USERNAME[n]] = {}
#
#
