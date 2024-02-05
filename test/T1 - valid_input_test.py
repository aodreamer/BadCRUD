import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class validInputTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        Chrome_options = webdriver.ChromeOptions()
        Chrome_options.add_argument('--headless')
        self.browser = webdriver.Chrome(options=Chrome_options)


    def test_1_sign_in_page_check(self):
        self.browser.get('http://localhost/BadCRUD/login.php')
        expected_result = "Please sign in"        
        actual_result = self.browser.find_element(By.XPATH, "/html/body/form/h1").text
        self.assertIn(expected_result, actual_result)

    def test_2_fill_cred(self):           
        expected_result = "Halo, admin"
        self.browser.find_element(By.NAME, "username").send_keys("admin")
        self.browser.find_element(By.NAME, "password").send_keys("nimda666!")
        self.browser.find_element(By.XPATH, "/html/body/form/button").click()
        actual_result = self.browser.find_element(By.XPATH, "/html/body/div[1]/h2").text                
        self.assertIn(expected_result, actual_result)

    def test_3_click_signout(self):           
        expected_result = "Please sign in"
        self.browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/a[3]").click()
        actual_result = self.browser.find_element(By.XPATH, "/html/body/form/h1").text                
        self.assertIn(expected_result, actual_result)
    
    @classmethod
    def tearDownClass(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2,warnings='ignore') 