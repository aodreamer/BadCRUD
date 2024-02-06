from selenium import webdriver
import os

def get_session():
    # Membuat instance browser (gunakan webdriver sesuai kebutuhan)
    driver = webdriver.Chrome()

    try:
        # Melakukan login (sesuaikan dengan langkah login pada aplikasi Anda)
        driver.get("https://example.com/login")
        username_input = driver.find_element_by_id("username")
        password_input = driver.find_element_by_id("password")
        submit_button = driver.find_element_by_id("submit")

        username_input.send_keys("your_username")
        password_input.send_keys("your_password")
        submit_button.click()

        # Mendapatkan nilai sesi (cookie)
        session_cookie = driver.get_cookie("session_cookie_name")["value"]
        print(f"Sesi Login: {session_cookie}")

        # Menyimpan nilai sesi ke dalam file
        with open("session_file.txt", "w") as file:
            file.write(session_cookie)

    finally:
        # Tutup browser
        driver.quit()

if __name__ == "__main__":
    get_session()
