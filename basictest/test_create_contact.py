import unittest, os
from selenium import webdriver
from selenium.webdriver.common.by import By

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

    def test_3_click_createcontact(self):           
        expected_result = "Add new contact"
        self.browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/a").click()
        actual_result = self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/h5").text                
        self.assertIn(expected_result, actual_result)
    
    def test_4_fill_contactdata(self):
        expected_result = "Halo, admin"
        self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/form/input[1]").send_keys("nael")
        self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/form/input[2]").send_keys("nael@gmail.com")
        self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/form/input[3]").send_keys("087123456789")
        self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/form/input[4]").send_keys("CEO PT SINARMAS")
        self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/form/input[5]").click()
        actual_result = self.browser.find_element(By.XPATH, "/html/body/div[1]/h2").text
        self.assertIn(expected_result, actual_result)
    
    def test_5_check_data_inputed(self):
        expected_result = "nael"
        self.browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[3]/div[2]/div/ul/li[4]/a").click()
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