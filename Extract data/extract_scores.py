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

try:
    driver.get("https://www.almamater.si/lestvicasol-srednjesole-s181")

    # Extract data
    data = []
    rows = driver.find_elements(By.CSS_SELECTOR, "tbody tr")
    for row in rows:
        row_items = row.find_elements(By.CSS_SELECTOR, "td div")

        if not len(row_items) >= 3:
            continue

        data.append({
            "name": " ".join( str( row_items[1].text ).strip().split() ),
            "result": float(row_items[2].text.replace(",", "."))
        })

    # Save data
    with open("schools.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False))
except Exception as e:
    print("Exception:", e)
finally:
    driver.quit()