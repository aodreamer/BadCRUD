import unittest, os
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
class LogoutTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        option = webdriver.FirefoxOptions()
        option.add_argument('--headless')
        cls.browser = webdriver.Firefox(options=option)
        try:
            cls.url = os.environ['URL']
        except:
            cls.url = "http://localhost/BadCRUD"

    def testOrder(self):
        self.sign_in_page_check()
        self.fill_cred()
        self.click_createcontact()
        self.click_cancel()

    @pytest.mark.run(order=1)
    def sign_in_page_check(self):
        self.browser.get(self.url)
        expected_result = "Please sign in"        
        actual_result = self.browser.find_element(By.XPATH, "/html/body/form/h1").text
        self.assertIn(expected_result, actual_result)

    @pytest.mark.run(order=2)
    def fill_cred(self):           
        expected_result = "Halo, admin"
        self.browser.find_element(By.NAME, "username").send_keys("admin")
        self.browser.find_element(By.NAME, "password").send_keys("nimda666!")
        self.browser.find_element(By.XPATH, "/html/body/form/button").click()
        actual_result = self.browser.find_element(By.XPATH, "/html/body/div[1]/h2").text                
        self.assertIn(expected_result, actual_result)

    @pytest.mark.run(order=3)
    def click_createcontact(self):           
        expected_result = "Add new contact"
        self.browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/a").click()
        actual_result = self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/h5").text                
        self.assertIn(expected_result, actual_result)

    @pytest.mark.run(order=4)    
    def click_cancel(self):
        expected_result = "Halo, admin"
        self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/form/a").click()
        actual_result = self.browser.find_element(By.XPATH, "/html/body/div[1]/h2").text
        self.assertIn(expected_result, actual_result)
    
        

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')