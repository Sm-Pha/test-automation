import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_data import test_data


class DriverManager:
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def tearDown(self):
        if self.driver:
            print("Cleanup of test environment")
            self.driver.quit()

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Initialize WebDriverWait for convenience

    #presence_of_element_located
    @property
    def email_field(self):
        return self.wait.until(EC.presence_of_element_located((By.ID, 'email')))  


    @property
    def password_field(self):
        return self.wait.until(EC.presence_of_element_located((By.ID, 'pass')))  
   
    @property
    def fb_title(self):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img[alt="Facebook"]'))) 

    # The email address you entered isn't connected to an account. Create a new Facebook account.
    # The email address or mobile number you entered isn't connected to an account. Find your account and log in.
    # The password that you've entered is incorrect. Forgotten password?  
    @property
    def email_password_error_message(self):
        return self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, '_9ay7')))  


    #element_to_be_clickable
    @property
    def sign_in_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.NAME, 'login')))


class TestLogin(DriverManager, unittest.TestCase):
    def handle_login_failure(self, expected_result):
        login_page = LoginPage(self.driver)

        if expected_result != "pass":
            error_messages = {
                "https://www.facebook.com/login/web/?email=sumittra.testing%40gmail.com&is_from_lara=1": "Password fail attempt 1",
                "https://www.facebook.com/recover/initiate/?lara_product=www_first_password_failure": "Password fail attempt 2",
            }

            try:
                error_message = error_messages.get(self.driver.current_url)
                if error_message:
                    print(error_message)
                else:
                    error_message = login_page.email_password_error_message.text if login_page.email_password_error_message.is_displayed() else self.driver.current_url
                    print(error_message)
            except AssertionError as e:
                print(f"Assertion error: {e}")
            except Exception as e:  # Catch other unexpected exceptions
                print(f"An unexpected error occurred: {e}")

    def test_login(self):
        login_url = "https://www.facebook.com/" 
        self.driver.get(login_url)
        self.driver.set_page_load_timeout(30)  

        login_page = LoginPage(self.driver)

        for i in test_data:

            username = i["username"]
            password = i["password"]
            expected_result = i["expected_result"]
            print(f"Testing login with username: {username}, password: {password}")

            self.driver.get(login_url)
            self.driver.set_page_load_timeout(30)
            assert login_page.fb_title.is_displayed(), "fb_title is not found"




            print(self.driver.current_url)

            login_page.email_field.clear()
            login_page.password_field.clear()

            login_page.email_field.send_keys(username)
            login_page.password_field.send_keys(password)
            login_page.sign_in_button.click()

            print(self.driver.current_url)

            if expected_result == 'pass':
                print(self.driver.current_url)
            else:
                self.handle_login_failure(expected_result)



        self.driver.refresh() 









if __name__ == '__main__':
    unittest.main()
