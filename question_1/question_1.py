from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

url = "https://www.olx.in/items/q-car-cover"
driver.get(url)
time.sleep(5)

soup = BeautifulSoup(driver.page_source, 'html.parser')

main_box=soup.find("div",class_="_2CyHG")
main_list=main_box.find("ul", class_="_266Ly _10aCo")
list_items=main_list.find_all("li",class_="_1DNjI")


driver.quit()
with open("output.txt", "w", encoding="utf-8") as file:
    for item in list_items:
        cost_tag = item.find("span", class_="_2Ks63")
        item_name_tag = item.find("span", class_="_2poNJ")
        location_tag = item.find("span", class_="_2VQu4")

        cost = cost_tag.text.strip() if cost_tag else "N/A"
        item_name = item_name_tag.text.strip() if item_name_tag else "N/A"
        location = location_tag.text.strip() if location_tag else "N/A"

        file.write(f"Item Name: {item_name}\n")
        file.write(f"Cost: {cost}\n")
        file.write(f"Location: {location}\n")
        file.write("\n\n")

