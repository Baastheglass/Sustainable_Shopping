import requests
from googlesearch import search
from bs4 import BeautifulSoup

if __name__ == "__main__":
    shopping_sites = open("shopping_sites.txt", "r").read().splitlines()
    print(shopping_sites)
    query = input("Enter query: ")
    search_results = search(query, num_results=10)
    for result in search_results:
        for site in shopping_sites:
            if site in result:
                response = requests.get(result)
                soup = BeautifulSoup(response.text, 'html.parser')
                print(result)
