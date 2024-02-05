import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import pytesseract
import time

class InvalidAllInputTest(unittest.TestCase):

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
        def ocr_image(image_path):
            image = Image.open(image_path)
            text = pytesseract.image_to_string(image)
            return text

        expected_result = "Please fil in this field"
        self.browser.find_element(By.XPATH, "/html/body/form/button").click()
        time.sleep(1)
        self.browser.save_screenshot('ss.png')
        time.sleep(1)


        actual_result = ocr_image("ss.png")
        self.assertIn(expected_result, actual_result)
    
    @classmethod
    def tearDownClass(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2,warnings='ignore') 