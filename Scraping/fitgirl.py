import time
from bs4 import BeautifulSoup
from fitgirl_list import url_list
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. INPUT DATA
# Note: I have replaced the specific links with a placeholder. 
# Ensure your target URLs comply with copyright laws.


print(f"Found {len(url_list)} links to process.")

# 3. SETUP EDGE DRIVER
# Use raw string (r'') for Windows paths to avoid escape character errors
edge_driver_path = r'D:/Programming/ML/Scraping/msedgedriver.exe'
user_data_dir = r"C:/Users/hp/EdgeAutomationProfile"

edge_options = Options()
edge_options.use_chromium = True
edge_options.add_argument(f"user-data-dir={user_data_dir}")
edge_options.add_experimental_option("detach", True) # Keeps browser open after script ends

# Initialize the Service
service = Service(executable_path=edge_driver_path)

try:
    # Initialize the Driver
    driver = webdriver.Edge(service=service, options=edge_options)
except Exception as e:
    print("Error initializing Edge. Is the profile currently in use by another window?")
    print(f"Details: {e}")
    exit()

# 4. ITERATION LOGIC
wait = WebDriverWait(driver, 15)
urls=url_list
# time.sleep(3000)
for url in urls:
    try:
        print(f"Opening: {url}")
        driver.get(url)

        # TARGET: Wait for button to be clickable
        download_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.link-button")))
        
        # Javascript Click (More robust against overlays)
        driver.execute_script("arguments[0].click();", download_btn)
        
        print(" -> Clicked Download")
        
        # CRITICAL: Wait for the download to actually register in the browser
        # before navigating to the next page.
        time.sleep(3) 

    except Exception as e:
        print(f" -> Failed to process {url}: {e}")

print("All links processed. Browser remains open.")