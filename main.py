import os
from bs4 import BeautifulSoup
from smtplib import SMTP
from dotenv import load_dotenv
import requests
load_dotenv()


URL = 'https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463'
TARGET_PRICE = 200.0

headers = {
    "User-Agent":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    "Accept-Language": 'en-US,en;q=0.9,si;q=0.8'
}

response = requests.get(url=URL, headers=headers)
amazon_web = response.text

soup = BeautifulSoup(amazon_web, 'html.parser')
price = soup.find(name="span", id="priceblock_ourprice")

price_in_float = float(price.getText().split('$')[1])

SENDER_EMAIL = 'nawodya135@gmail.com'
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

RECIVER_EMAIL = 'nawodyahckr@gmail.com'
MSG_CONTENT = f'Subject:Buy The Rice Cooker \n\n Now the price is below than $100 then Hurry go and buy!  {URL}'

if price_in_float < TARGET_PRICE:
    with SMTP('smtp.gmail.com', 587) as session:
        session.starttls()
        session.login(SENDER_EMAIL, EMAIL_PASSWORD)
        session.sendmail(SENDER_EMAIL, RECIVER_EMAIL, MSG_CONTENT)
        print("Mail Sent!")

else:
    print("Email not sent")
    