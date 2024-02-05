import unittest, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    def test_1_sign_in_page_check(self):
        self.browser.get(self.url)
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
        

    def test_3_click_first_edit_button(self):
        expected_result = "Change contact"
        self.browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[7]/a[1]").click()
        actual_result = self.browser.title
        
        self.assertIn(expected_result, actual_result)
          
    def test_4_fill_new_name(self):
        expected_result = "Halo, admin"
        self.browser.find_element(By.NAME, "name").clear()
        self.browser.find_element(By.NAME, "name").send_keys("user baru")
        self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/form/input[5]").click()
        actual_result = self.browser.find_element(By.XPATH, "/html/body/div[1]/h2").text        
        self.assertIn(expected_result, actual_result)

    def test_5_check_updated_data(self):
        expected_result = "user baru"
        table = self.browser.find_element(By.ID,"employee")
        rows = table.find_elements(By.TAG_NAME, "tr")

        table_data = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME,"td")
            row_data = [cell.text for cell in cells]
            table_data.append(row_data)
        
        flat_table_data = [item for sublist in table_data for item in sublist]

        self.assertIn(expected_result, flat_table_data)
        

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')