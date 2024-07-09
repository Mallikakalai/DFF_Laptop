

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

##defined all the locators
## to locate the disappearing pop-up message used setTimeout debugger function to freeze the page and find the webelement locators
class web_page:
    def __init__(self, driver):
        self.driver = driver
        self.username_input=(By.NAME,"username")
        self.password_input=(By.NAME,"password")
        self.login_button=(By.CSS_SELECTOR,"button[type='Submit']")

    def open_page(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def login_page(self,username,password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.username_input)).send_keys(username)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.password_input)).send_keys(password)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.login_button)).click()
