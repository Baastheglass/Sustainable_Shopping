import requests
from googlesearch import search
from bs4 import BeautifulSoup

if __name__ == "__main__":
    shopping_sites = open("./shopping_sites.txt", "r").read().splitlines()
    query = input("Enter query: ")
    search_results = search(query, num_results=10)
    for result in search_results:
        print(result)
        for site in shopping_sites:
            if site in result:
                #print("If entered")
                response = requests.get(result)
                soup = BeautifulSoup(response.text, 'html.parser')
                if site == "habitt":
                    base_habbit_link = "https://habitt.com"
                    prices = soup.find_all("span", class_="price-item price-item--regular")
                    image_links = []
                    card_links = soup.find_all("a", class_ = "card-link")
                    for link in card_links:
                        response = requests.get(base_habbit_link + link.get("href"))
                        soup = BeautifulSoup(response.text, 'html.parser')
                        possible_image_links = soup.find_all("img")
                        possible_image_links = list(possible_image_links)
                        try:
                            for link in possible_image_links:
                                #print(link.get("id"))
                                if(link.get("id") != None):
                                    if "product-featured-image" in link.get("id"):
                                        image_link = link.get("src")
                                        image_link = str(image_link)[2:]
                                        image_links.append(image_link) 
                        except Exception as e:
                            print(e)
                    print(image_links)
                
