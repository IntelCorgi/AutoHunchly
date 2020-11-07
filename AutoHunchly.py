import selenium
import time
import random
from selenium import webdriver

# Enforces Chrome running in incognito mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options = chrome_options)

# Introduction
print("Welcome to AutoHunchly.")

# Iterate through input file and assemble domains into a Selenium-friendly format.
with open("domains.txt", "r") as file_input:
    domains_list = []
    for domain_raw in file_input:
        domain_complete = "https://" + domain_raw.rstrip()
        domains_list.append(domain_complete)
   
    # Use selenium to make requests
    for domain_target in domains_list:
        driver.get(domain_target)
        # Print update as domains are archived
        domain_update = domain_target.replace("https://www.", "")
        print(f"Archiving {domain_update} ...")
        # Random sleep
        time.sleep(random.uniform(10, 20))

# Notification that the archiving is complete and shut down the driver
print("Archiving complete! Check your Hunchly case.")
driver.quit()