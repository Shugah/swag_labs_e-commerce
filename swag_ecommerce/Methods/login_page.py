from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Locators.login_page_locators import Login
from selenium.webdriver.common.by import By



class LoginPage:
    def __init__(self, driver):
       self.driver = driver
       self.wait = WebDriverWait(self.driver, 10)
       self.user = 'standard_user'
       self.invalid_user = 'cat'
       self.password = 'secret_sauce'
       self.invalid_password = 'fish'


    def enter_valid_username(self):
        username_input = self.wait.until(
            EC.visibility_of_element_located((By.ID, Login.username)))

        username_input.send_keys(self.user)


    def enter_invalid_username(self):
        username_input = self.wait.until(
            EC.visibility_of_element_located((By.ID, Login.username)))
        username_input.send_keys(self.invalid_user)

        password_input = self.wait.until(
            EC.visibility_of_element_located((By.ID, Login.password)))
        password_input.send_keys(self.password)

        username_input_click = self.wait.until(
            EC.visibility_of_element_located((By.ID, Login.login_button)))
        username_input_click.click()


    def message_container_error(self):
        message_error= self.driver.find_element(By.CLASS_NAME, "error-message-container")
        return message_error.text


    def get_username_value(self):
        username_input = self.driver.find_element(By.ID,Login.username)
        return username_input.get_attribute("value")


    def enter_invalid_password(self):
        username_input = self.wait.until(
            EC.visibility_of_element_located((By.ID, Login.username)))
        username_input.send_keys(self.user)

        password_invalid_input = self.wait.until(
            EC.visibility_of_element_located((By.ID, Login.password)))
        password_invalid_input.send_keys(self.invalid_password)

        password_input_click = self.wait.until(
            EC.visibility_of_element_located((By.ID, Login.login_button)))
        password_input_click.click()



    def enter_valid_password(self):
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


