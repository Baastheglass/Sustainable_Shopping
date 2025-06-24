from email.mime import image
import requests
from googlesearch import search
from bs4 import BeautifulSoup
import random
import sys
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class Product:
    def __init__(self, name, img_link, price):
        self.name = name
        self.img_link = img_link
        self.price = price
    def set_name(self, name):
        self.name = name
    def set_img_link(self, img_link):
        self.img_link = img_link    
    def set_price(self, price):
        self.price = price
              

def daraz(linky):
    print(linky)
    print("Daraz site detected")
    driver = uc.Chrome()
    driver.get(linky)
    #waiting until DOM has loaded fully
    WebDriverWait(driver, 30).until(lambda d: d.execute_script("return document.readyState") == "complete")
    links = driver.find_elements(By.TAG_NAME, "a")
    product_links = []
    for link in links:
        # print(link.get_attribute("href"))
        # print(type(link.get_attribute("href")))
        if(link.get_attribute("href") != None):
            if '/products/' in link.get_attribute("href"):
                product_links.append(link.get_attribute("href"))
    product_links = list(set(product_links))  # Remove duplicates
    #print("Product links found: ", product_links)
    for link in product_links:
        print(link)
        response = requests.get(link, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        #print(soup)
        relevant_image_links = []
        images = soup.find_all("img")
        #print(images)
        for img in images:
            if(img.get("src") and img.get("alt") and "720x720" in img.get("src")):
                print(img.get("src")) #accurately getting product image link
                relevant_image_links.append(img.get("src"))
        driver.get(link)
        spans = driver.find_elements(By.TAG_NAME, "span")
        WebDriverWait(driver, 30).until(lambda d: d.execute_script("return document.readyState") == "complete")
        prices = []
        for span in spans:
            if("notranslate" in span.get_attribute("class") and "pdp-price_type_deleted" not in span.get_attribute("class")):
                print("Price found: ", span.get_attribute("innerText")) #accurately getting product price
                prices.append(span.get_attribute("innerText"))
        product_name = driver.find_element(By.CLASS_NAME, "pdp-mod-product-badge-title").text
        print("Product name: ", product_name)
        print("Prices:", len(prices), "Images:", len(relevant_image_links))
        print("Iter done")

def habitt(linky):
    response = requests.get(linky)
    soup = BeautifulSoup(response.text, 'html.parser')
    base_habbit_link = "https://habitt.com"
    prices = soup.find_all("span", class_="price-item price-item--regular")
    possible_item_names = soup.find_all("a", class_="card-title link-underline card-title-ellipsis")
    item_names = []
    for item in possible_item_names:
        item_names.append(item)
        print(item['data-product-title'])
    for price in prices:
        prices[prices.index(price)] = price.get_text()
    image_links = []
    card_links = soup.find_all("a", class_ = "card-link")
    for link in card_links:
        response = requests.get(base_habbit_link + link.get("href"))
        soup = BeautifulSoup(response.text, 'html.parser')
        possible_image_links = soup.find_all("img")
        possible_image_links = list(possible_image_links)
        try:
            for link in possible_image_links:
                if(link.get("id") != None):
                    if "product-featured-image" in link.get("id"):
                        image_link = link.get("src")
                        if(image_link != None):
                            image_link = str(image_link)[2:]
                            image_links.append(image_link) 
        except Exception as e:
            print(e)
    print(image_links)
    print(prices)
    print(item_names)

if __name__ == "__main__":
    shopping_sites = open("./shopping_sites.txt", "r").read().splitlines()
    query = input("Enter query: ")
    search_results = search(query, num_results=100)
    # A list of common User-Agents to rotate
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/117.0",
    ]

    # Construct your headers
    headers = {
        "User-Agent": random.choice(user_agents), # Randomly pick a User-Agent
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.google.com/", # Or a plausible previous page on the target site
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
    }
    for result in search_results:
        print(result)
        for site in shopping_sites:
            if site in result:
                #print("If entered")
                if site == "habitt":
                    habitt(result)    
                elif site == "daraz":
                    pass
                    # try:
                    #     daraz(result)    
                    # except Exception as e:
                    #     print("Error occured while scraping Daraz: ", e)
                    #     print("Retrying")
                    #     driver = uc.Chrome()
                    #     daraz(result)        
                        #images = soup.find_all('img')#root > div > div.ant-row.FrEdP.css-1bkhbmc.app > div:nth-child(1) > div > div.ant-col.ant-col-20.ant-col-push-4.Jv5R8.css-1bkhbmc.app > div._17mcb > div:nth-child(1) > div > div > div.ICdUp > div > a
                    # print(images)
                    #sys.exit(0)
