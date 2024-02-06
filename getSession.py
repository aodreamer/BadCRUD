from selenium import webdriver
from selenium.webdriver.common.by import By
import os

def get_session():
    # Membuat instance browser (gunakan webdriver sesuai kebutuhan)
    option = webdriver.FirefoxOptions()
    option.add_argument('--headless')
    driver = webdriver.Firefox(options=option)

    try:
        # Melakukan login (sesuaikan dengan langkah login pada aplikasi Anda)
        try:
            url = os.environ['URL']
        except:
            url = "http://localhost/BadCRUD"

        driver.get(url)
        driver.find_element(By.NAME, "username").send_keys("admin")
        driver.find_element(By.NAME, "password").send_keys("nimda666!")
        driver.find_element(By.XPATH, "/html/body/form/button").click()

        # Mendapatkan nilai sesi (cookie)
        session_cookie = driver.get_cookie("PHPSESSID")["value"]
        print(f"Sesi Login: {session_cookie}")

        # Menyimpan nilai sesi ke dalam file
        with open("session_file.txt", "w") as file:
            file.write(session_cookie)

    finally:
        # Tutup browser
        driver.quit()

if __name__ == "__main__":
    get_session()
