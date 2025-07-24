from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json

# Setup driver for background use
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")

# Create driver
driver = webdriver.Chrome(options=chrome_options)

# Get school data
with open("schools.json", "r") as f:
    schools = json.load(f)

try:
    driver.get("")
except Exception as e:
    print("Exception:", e)
finally:
    driver.quit()