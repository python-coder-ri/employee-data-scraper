
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Setup WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Load the site
driver.get("https://datatables.net/examples/data_sources/ajax.html")

# Wait for the table to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "example")))

# Wait a bit more to ensure AJAX content is fully loaded
time.sleep(2)

data = []

# Get the total number of pages (optional – hardcoded to 6 here)
for page in range(6):   # Pages 0 to 5
    # Wait for table rows to be present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#example tbody tr")))
    time.sleep(1)  # Let content render fully

    # Get current page rows
    rows = driver.find_elements(By.CSS_SELECTOR, "#example tbody tr")
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        data.append([col.text for col in cols])   


# Create DataFrame
df = pd.DataFrame(data, columns=["Name", "Position", "Office", "Extn.", "Start date", "Salary"])

# Save to Excel
df.to_excel(r"D:\Python\New_folder\datatable_export_all_pages.xlsx", index=False)

driver.quit()
print("✅ All pages scraped and saved!")

