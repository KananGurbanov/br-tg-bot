from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import tempfile

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=1920,1080")
# chrome_options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

# chrome_service = Service("/usr/bin/chromedriver")  # Explicit chromedriver path

driver = webdriver.Chrome( options=chrome_options)
