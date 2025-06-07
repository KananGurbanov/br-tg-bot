import time
from selenium.webdriver.common.by import By
from PIL import Image
import io
from app.constants.constants import TARGET_URL, TARGET_USERNAME, \
    TARGET_PASSWORD
from app.webdriver.webdriver import driver


class HD_Film_Cehennemi:

    def __init__(self):
        self._driver = driver

    def get_hd_film_cehennemi_screenshot(self):

        try:

            self._driver.get(TARGET_URL)

            time.sleep(2)

            login_button = self._driver.find_element(By.CSS_SELECTOR, "button.login[aria-label='Login']")

            login_button.click()

            time.sleep(2)

            username_input = driver.find_element(By.ID, "loginUsername")
            username_input.send_keys(TARGET_USERNAME)

            password_input = driver.find_element(By.ID, "loginPassword")
            password_input.send_keys(TARGET_PASSWORD)

            login_button = driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(), 'Giriş Yap')]")
            login_button.click()

            time.sleep(2)

            screenshot = self._driver.get_screenshot_as_png()

            image = Image.open(io.BytesIO(screenshot))
            return image


        except Exception as e:
            raise Exception(f"Error during hd film cehennemi: {e}")
        finally:
            self._driver.quit()