from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
import urllib.parse

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
    for indx, school in enumerate(schools):
        search_url = "https://www.24ur.com/iskanje?q=" + urllib.parse.quote_plus(school["name"])
        driver.get(search_url)

        article_elements = driver.find_elements(By.CSS_SELECTOR, "main.main div a.group")

        # Extract article links
        article_links = [element.get_attribute("href") for element in article_elements]
        
        # Save to school data
        school["articles"] = article_links
        schools[indx] = school
except Exception as e:
    print("Exception:", e)
finally:
    driver.quit()