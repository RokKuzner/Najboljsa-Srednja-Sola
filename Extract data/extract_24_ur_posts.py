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
    # Extract articles
    for indx, school in enumerate(schools):
        search_url = "https://www.24ur.com/iskanje?q=" + urllib.parse.quote_plus(school["name"])
        driver.get(search_url)

        article_elements = driver.find_elements(By.CSS_SELECTOR, "main.main div a.group")
        
        # Extract actual article content
        articles:list[str] = []
        for article_link in [article_element.get_attribute("href") for article_element in article_elements]:
            if not article_link:
                continue

            driver.get(article_link)

            content_elements = driver.find_elements(By.CSS_SELECTOR, "article p")[:-1] # Skip the last element, sice it is allways a non-content-realted warning

            content = " ".join( [content_element.text.strip() for content_element in content_elements] )
            if content: articles.append(content)

        # Save content to school data
        school["articles"] = articles
        schools[indx] = school

    # Save data
    with open("schools.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(schools, ensure_ascii=False))

except Exception as e:
    print("Exception:", e)
finally:
    driver.quit()