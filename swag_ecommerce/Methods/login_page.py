from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Locators.login_page_locators import Login
from selenium.webdriver.common.by import By



class LoginPage:
    def __init__(self, driver):
       self.driver = driver
       self.wait = WebDriverWait(self.driver, 10)
       self.user = 'standard_user'
       self.password = 'secret_sauce'


    def enter_username(self):
        username_input = self.wait.until(
            EC.visibility_of_element_located((By.ID, Login.username)))

        username_input.send_keys(self.user)

    def get_username_value(self):
        username_input = self.driver.find_element(By.ID,Login.username)
        return username_input.get_attribute("value")




    def enter_password(self):
        password_input = self.wait.until(
            EC.visibility_of_element_located((By.ID, Login.password)))

        password_input.send_keys(self.password)

    def get_password_value(self):
        password_input = self.driver.find_element(By.ID,Login.password)
        return password_input.get_attribute("value")




    def click_login(self):
        login_button = self.wait.until(
            EC.presence_of_element_located((By.ID, Login.login_button)))

        login_button.click()


