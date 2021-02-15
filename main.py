from bs4 import BeautifulSoup
import requests

URL = 'https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463'

headers = {
    "User-Agent":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    "Accept-Language": 'en-US,en;q=0.9,si;q=0.8'
}

response = requests.get(url=URL, headers=headers)
amazon_web = response.text

soup = BeautifulSoup(amazon_web, 'html.parser')
price = soup.find(name="span", id="priceblock_ourprice")
print(price.getText())