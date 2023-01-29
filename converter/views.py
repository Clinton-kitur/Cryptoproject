from django.http import JsonResponse
from django.views import View

from bs4 import BeautifulSoup
import requests

class ScraperView(View):
    def get(self, request):
        # Perform the web scraping here
        page = requests.get('https://www.google.com/finance/markets/cryptocurrencies?hl=en')
        soup = BeautifulSoup(page.text, 'html.parser')
        data = soup.prettify()

        # Return the data through the API endpoint
        return JsonResponse({'data': data})
import requests
from rest_framework import views
from rest_framework.response import Response


# # Create your views here.

# class ConvertView(views.APIView):
#     def get(self, request):
#         # Get the cryptocurrency from the request
#         crypto = request.query_params.get("crypto")

#         # CoinMarketCap API endpoint for fetching exchange rates
#         endpoint = "https://www.google.com/finance/markets/cryptocurrencies?hl=en"

#         # Fetch the data from the API
#         r = requests.get(endpoint + crypto)
#         data = r.json()

#         # Extract the exchange rate in USD
#         exchange_rate = data[0]['price_usd']

#         # Return the result
#         return Response({"exchange_rate": exchange_rate})
# class WebsiteScraper:
#     def __init__(self, url):
#         # self.url = url
#         self.url = https://www.google.com/finance/markets/cryptocurrencies?hl=en
#     def scrape(self):
#         # Send a GET request to the website
#         response = requests.get(self.url)

#         # Parse the HTML content of the website
#         soup = BeautifulSoup(response.text, 'html.parser')

#         # Extract the data you want to scrape
#         data = soup.find_all('div', {'class': 'some-class'})
        
#         scraper = WebsiteScraper('https://www.google.com/finance/markets/cryptocurrencies?hl=en')
#         data = scraper.scrape()

#         return data

