from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Locators.login_page_locators import Login
from selenium.webdriver.common.by import By



class ShoppingCart:
    def __init__(self, driver):
       self.driver = driver
       self.wait = WebDriverWait(self.driver, 10)

    def click_shopping_cart(self):
        shopping_cart = self.wait.until(
            EC.visibility_of_element_located((By.ID, Login.shopping_cart_button)))

        shopping_cart.click()

    def add_item_to_cart(self):
        add_item = self.wait.until(
            EC.visibility_of_element_located((By.ID, Login.add_item)))

        add_item.click()

    def user_can_add_item(self):
        cart_badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        return cart_badge.text


    def remove_item_from_cart(self):
        remove_item = self.wait.until(
            EC.presence_of_element_located((By.ID, Login.remove_item))
        )

        remove_item.click()

    def get_cart_count(self):
        badges = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        return int(badges[0].text) if badges else 0 #<Busca si hay elementos en la lista y sino, regresas cero>
