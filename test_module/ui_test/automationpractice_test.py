import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .email_service import get_random_email
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAP:
    browser = None
    ap_home_url = 'http://automationpractice.com/index.php'
    first_name = 'Anna'
    last_name = 'Tereshchenko'
    phone = '+375298951731'
    address1 = 'Platonova 2'
    address2 = 'Minsk Office'
    city = 'Minsk'
    post_code = 12345
    username = 'Anna'
    password = '123456789'
    company = 'Akveo'
    addition_info = 'Some additional information'
    home_phone = '80173444444'
    address_alias = 'My address'
    test_email = get_random_email()

    @pytest.fixture()
    def setUp(self):
        self.browser = webdriver.Chrome("C:/Users/Admin/PycharmProjects/TMS05_HW/chromedriver")
        self.browser.maximize_window()
        self.browser.get(self.ap_home_url)
        self.browser.implicitly_wait(10)
        yield
        self.browser.quit()

    def test_registration(self, setUp):

        sign_in_button = self.browser.find_element(by=By.CLASS_NAME, value='login')
        sign_in_button.click()

        WebDriverWait(self.browser, 10).until(
            EC.title_is('Login - My Store'))

        email_for_registration = self.browser.find_element(by=By.ID, value='email_create')
        create_an_account_button = self.browser.find_element(by=By.ID, value='SubmitCreate')

        email_for_registration.send_keys(self.test_email)
        create_an_account_button.click()

        WebDriverWait(self.browser, 10).until(
            EC.visibility_of(self.browser.find_element(By.ID, 'id_gender2')))

        gender_radio_button = self.browser.find_element(by=By.ID, value='id_gender2')
        first_name = self.browser.find_element(by=By.ID, value='customer_firstname')
        last_name = self.browser.find_element(by=By.ID, value='customer_lastname')
        entered_email = self.browser.find_element(by=By.ID, value='email')
        password = self.browser.find_element(by=By.ID, value='passwd')
        day_of_birth = self.browser.find_element(by=By.ID, value='days')
        month_of_birth = self.browser.find_element(by=By.ID, value='months')
        year_of_birth = self.browser.find_element(by=By.ID, value='years')
        newsletters_checkbox = self.browser.find_element(by=By.ID, value='newsletter')
        special_offers_checkbox = self.browser.find_element(by=By.ID, value='optin')
        entered_first_name = self.browser.find_element(by=By.ID, value='firstname')
        entered_last_name = self.browser.find_element(by=By.ID, value='lastname')
        company = self.browser.find_element(by=By.ID, value='company')
        address1 = self.browser.find_element(by=By.ID, value='address1')
        address2 = self.browser.find_element(by=By.ID, value='address2')
        city = self.browser.find_element(by=By.ID, value='city')
        state = self.browser.find_element(by=By.ID, value='id_state')
        postcode = self.browser.find_element(by=By.ID, value='postcode')
        country = self.browser.find_element(by=By.ID, value='id_country')
        addition_info = self.browser.find_element(by=By.ID, value='other')
        home_phone = self.browser.find_element(by=By.ID, value='phone')
        mobile_phone = self.browser.find_element(by=By.ID, value='phone_mobile')
        address_alias = self.browser.find_element(by=By.ID, value='alias')
        register_button = self.browser.find_element(by=By.ID, value='submitAccount')

        assert gender_radio_button.is_displayed()

        gender_radio_button.click()
        first_name.send_keys(self.first_name)
        last_name.send_keys(self.last_name)

        if entered_email.get_attribute('value') != '':
            assert self.test_email == entered_email.get_attribute('value')
        else:
            entered_email.send_keys(self.test_email)

        password.send_keys(self.password)
        Select(day_of_birth).select_by_value('4')
        Select(month_of_birth).select_by_value('1')
        Select(year_of_birth).select_by_value('1994')
        newsletters_checkbox.click()
        assert newsletters_checkbox.is_selected()
        special_offers_checkbox.click()
        assert newsletters_checkbox.is_selected()

        if entered_first_name.get_attribute('value') != '':
            assert self.first_name == entered_first_name.get_attribute('value')
        else:
            entered_first_name.send_keys(self.first_name)
        if entered_last_name.get_attribute('value') != '':
            assert self.last_name == entered_last_name.get_attribute('value')
        else:
            entered_last_name.send_keys(self.last_name)

        company.send_keys(self.company)
        address1.send_keys(self.address1)
        address2.send_keys(self.address2)
        city.send_keys(self.city)
        Select(state).select_by_value('33')
        postcode.send_keys(self.post_code)
        Select(country).select_by_value('21')
        addition_info.send_keys(self.addition_info)
        home_phone.send_keys(self.home_phone)
        mobile_phone.send_keys(self.phone)
        address_alias.send_keys(self.address_alias)
        register_button.click()

        WebDriverWait(self.browser, 10).until(
            EC.title_is('My account - My Store'))

        sign_out_button = self.browser.find_element(by=By.CLASS_NAME, value='logout')
        account_icon = self.browser.find_element(by=By.CLASS_NAME, value='account')

        assert sign_out_button.is_displayed()
        assert account_icon.is_displayed()
        assert account_icon.text == f'{self.first_name} {self.last_name}'

    def test_login(self, setUp):

        sign_in_button = self.browser.find_element(by=By.CLASS_NAME, value='login')
        sign_in_button.click()

        WebDriverWait(self.browser, 10).until(
            EC.title_is('Login - My Store'))

        email = self.browser.find_element(by=By.ID, value='email')
        password = self.browser.find_element(by=By.ID, value='passwd')
        signin_button = self.browser.find_element(by=By.ID, value='SubmitLogin')

        email.send_keys(self.test_email)
        password.send_keys(self.password)
        signin_button.click()

        WebDriverWait(self.browser, 10).until(
            EC.title_is('My account - My Store'))

        sign_out_button = self.browser.find_element(by=By.CLASS_NAME, value='logout')
        account_icon = self.browser.find_element(by=By.CLASS_NAME, value='account')

        assert sign_out_button.is_displayed()
        assert account_icon.is_displayed()
        assert account_icon.text == f'{self.first_name} {self.last_name}'
