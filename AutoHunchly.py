import selenium
from selenium import webdriver
driver = webdriver.Chrome()
# Introduction
print("Welcome to AutoHunchly.")



# Iterate domains in txt file
# protocol = "https://"
# with open("domains.txt", "r") as domains:
#     domains_list = domains.read().splitlines()
#     for domain in domains_list:
#         hunchly_target = protocol + domain
#         driver.get(domain)


with open("domains.txt", "r") as file_input:
    domains_list = []
    for domain_raw in file_input:
        domain_target = "https://" + domain_raw.rstrip()
        domains_list.append(domain_target)
print(domains_list)

# domains = ["https://disney.com", "https://cnn.com"]
# for domain in domains:
#     driver.get(domain)
            
    #except:

    #driver.quit()
