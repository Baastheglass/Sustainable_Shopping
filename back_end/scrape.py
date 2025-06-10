import requests
from googlesearch import search

if __name__ == "__main__":
    query = input("Enter query: ")
    search_results = search(query, num_results=100)
    for result in search_results:
        print(result)
