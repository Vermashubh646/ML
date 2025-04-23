import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service


# List of 60 Indian historical places
places = [
    "Taj Mahal",
    "Red Fort",
    "Qutub Minar",
    "India Gate",
    "Hawa Mahal",
    "Amer Fort",
    "City Palace Jaipur",
    "Gateway of India",
    "Victoria Memorial",
    "Mysore Palace",
    "Charminar",
    "Golconda Fort",
    "Fatehpur Sikri",
    "Sanchi Stupa",
    "Konark Sun Temple",
    "Ajanta Caves",
    "Ellora Caves",
    "Brihadeeswarar Temple",
    "Meenakshi Temple",
    "Gol Gumbaz",
    "Rani ki Vav",
    "Chittorgarh Fort",
    "Jaisalmer Fort",
    "Nalanda University Ruins",
    "Mahabalipuram",
    "Shaniwar Wada",
    "Bibi Ka Maqbara",
    "Laxmi Vilas Palace",
    "Udaipur City Palace",
    "Kumbhalgarh Fort",
    "Jaigarh Fort",
    "Hampi",
    "Vittala Temple",
    "Badami Cave Temples",
    "Elephanta Caves",
    "Udayagiri Caves",
    "Humayun's Tomb",
    "Akbar's Tomb",
    "Jama Masjid Delhi",
    "Mehrauli Archaeological Park",
    "Qutb Complex",
    "Sarnath",
    "Ajmer Sharif Dargah",
    "Mehrangarh Fort",
    "Ranthambore Fort",
    "Agra Fort",
    "Chunar Fort",
    "Rohtas Fort",
    "Gwalior Fort",
    "Orchha Fort",
    "Daulatabad Fort",
    "Bhangarh Fort",
    "Sree Padmanabhaswamy Temple",
    "Raghunath Temple, Ayodhya",
    "Rani Mahal Jodhpur",
    "Dilwara Temples",
    "Chand Baori",
    "Bodh Gaya Mahabodhi Temple",
    "Gangaikonda Cholapuram",
    "Kanchi Kailasanath Temple"
]

# Path to your msedgedriver executable, adjust as needed
edgedriver_path = r'D:/Programming/ML/Scraping/msedgedriver.exe'

# Set up Edge options to use a dedicated user profile for automation.
options = webdriver.EdgeOptions()
# Instead of using your main Edge profile, consider using a separate profile folder:
options.add_argument(r"user-data-dir=C:/Users/hp/EdgeAutomationProfile")

# Optional: Add arguments to help avoid the "DevToolsActivePort" error.
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Repeat the search process 15 times
for i in range(60):
    # Select a random place from the list and remove it to avoid repetition.
    query = random.choice(places)
    places.remove(query)
    print(f"Search {i+1}: {query}")

    # Initialize the Edge driver with the specified options
    service = Service(edgedriver_path)
    driver = webdriver.Edge(service=service, options=options)
    
    # Open Bing
    driver.get("https://www.bing.com")
    time.sleep(5)  # wait for the page to load
    
    try:
        # Locate the search box by its name attribute ("q" for Bing)
        search_box = driver.find_element(By.NAME, "q")
        
        
        print(f"Search {i+1}: {query}")
        
        # Enter the query and submit it
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)  # wait for search results to load
    except Exception as e:
        print(f"An error occurred during search {i+1}: {e}")
    finally:
        # Close the browser window
        driver.quit()
