import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PIL import Image
import io
from selenium.webdriver.support.wait import WebDriverWait
from app.constants.constants import GITLAB_URL, GITLAB_USERNAME, GITLAB_PASSWORD
from app.webdriver.webdriver import driver


def get_gitlab_screenshot():

    try:

        driver.uc_open_with_reconnect(GITLAB_URL, 4)
        driver.uc_gui_click_captcha()

        wait = WebDriverWait(driver, 5)

        try:
            checkbox = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ctp-checkbox-label")))
            driver.execute_script("arguments[0].click();", checkbox)
            print("Clicked Cloudflare checkbox!")
        except:
            print("Cloudflare checkbox not found, continuing...")



        wait.until(EC.presence_of_element_located((By.ID, "user_login")))
        print("Login page loaded!")

        username_field = driver.find_element(By.ID, 'user_login')
        password_field = driver.find_element(By.ID, 'user_password')
        login_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="sign-in-button"]')

        username_field.send_keys(GITLAB_USERNAME)
        password_field.send_keys(GITLAB_PASSWORD)
        login_button.click()

        time.sleep(5)

        screenshot = driver.get_screenshot_as_png()

        image = Image.open(io.BytesIO(screenshot))
        return image

    except Exception as e:
        raise Exception(f"Error during GitLab login and screenshot: {e}")
    finally:
        driver.quit()
