import data
from driver_setup import  get_driver
from Methods.login_page import LoginPage
from Methods.cart_page import ShoppingCart
from Helpers.helpers import login
import time



class TestLoginAndCart:

    @classmethod
    def setup_class(cls):
        cls.driver = get_driver()
        cls.driver.get(data.URL)
        cls.login_page = LoginPage(cls.driver)
        cls.inventory = ShoppingCart(cls.driver)


    def test_valid_username(self):
        self.login_page.enter_valid_username()
        assert self.login_page.get_username_value() == 'standard_user'
        assert "Password is required" in self.login_page.message_container_error()

    def test_invalid_username(self):
        self.login_page.enter_invalid_username()

        assert self.login_page.get_username_value() == 'cat'
        assert (
            "Epic sadface: Username and password do not match any user in this service"
            in self.login_page.message_container_error()
)

    def test_valid_password(self):
        self.login_page.enter_valid_password()

        assert self.login_page.get_password_value() == 'secret_sauce'
        assert 'Username is required' in self.login_page.message_container_error()

    def test_invalid_password(self):
        self.login_page.enter_invalid_password()

        assert self.login_page.get_password_value() == 'fish'
        assert "Epic sadface: Username and password do not match any user in this service" in self.login_page.message_container_error()

    def test_click_login_button(self):
        login(self.login_page)

        assert "inventory" in self.driver.current_url

    def test_add_item(self):
        login(self.login_page)
        self.inventory.add_item_to_cart()

        assert self.inventory.user_can_add_item() == "1"


    def test_click_shopping_cart_button(self):
        login(self.login_page)
        self.inventory.click_shopping_cart()

        assert "cart" in self.driver.current_url

    def test_remove_item(self):
        login(self.login_page)
        self.inventory.add_item_to_cart()
        self.inventory.click_shopping_cart()
        self.inventory.remove_item_from_cart()

        assert self.inventory.get_cart_count() == 0



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()