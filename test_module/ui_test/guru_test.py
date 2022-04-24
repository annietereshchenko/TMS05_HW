import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .email_service import get_random_email


class TestGuru:
    browser = None
    guru_url = 'https://demo.guru99.com/test/newtours/register.php'
    first_name = 'Anna'
    last_name = 'Tereshchenko'
    phone = '+375298951731'
    address = 'Platonova 2'
    city = 'Minsk'
    post_code = 220065
    username = 'Anna'
    password = '12345678'

    @pytest.fixture()
    def setUp(self):
        self.browser = webdriver.Chrome("C:/Users/Admin/PycharmProjects/TMS05_HW/chromedriver")
        self.browser.maximize_window()
        self.browser.get(self.guru_url)
        self.browser.implicitly_wait(10)
        yield
        self.browser.quit()

    def test_registration_check_welcome_msg(self, setUp):

        first_name = self.browser.find_element(by=By.NAME, value='firstName')
        last_name = self.browser.find_element(by=By.NAME, value='lastName')
        phone = self.browser.find_element(by=By.NAME, value='phone')
        email = self.browser.find_element(by=By.ID, value='userName')
        address = self.browser.find_element(by=By.NAME, value='address1')
        city = self.browser.find_element(by=By.NAME, value='city')
        state = self.browser.find_element(by=By.NAME, value='state')
        post_code = self.browser.find_element(by=By.NAME, value='postalCode')
        country_drop_down = self.browser.find_element(by=By.NAME, value='country')
        username = self.browser.find_element(by=By.ID, value='email')
        password = self.browser.find_element(by=By.NAME, value='password')
        confirm_password = self.browser.find_element(by=By.NAME, value='confirmPassword')
        submit_button = self.browser.find_element(by=By.NAME, value='submit')

        first_name.send_keys(self.first_name)
        last_name.send_keys(self.last_name)
        phone.send_keys(self.phone)
        email.send_keys(get_random_email())
        address.send_keys(self.address)
        city.send_keys(self.city)
        state.send_keys(self.city)
        post_code.send_keys(self.post_code)
        Select(country_drop_down).select_by_value('BELARUS')
        username.send_keys(self.username)
        password.send_keys(self.password)
        confirm_password.send_keys(self.password)
        submit_button.click()

        names_after_register = self.browser.find_element(by=By.XPATH, value='//b[contains(text(),"Dear")]')
        username_after_register = self.browser.find_element(by=By.XPATH, value='//b[contains(text(),"Note: Your")]')

        act_welcome_msg = names_after_register.text
        exp_welcome_msg = f'Dear {self.first_name} {self.last_name},'

        assert act_welcome_msg == exp_welcome_msg

        act_username = username_after_register.text
        exp_username = f'Note: Your user name is {self.username}.'

        assert act_username == exp_username
