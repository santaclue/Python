import requests
from bs4 import BeautifulSoup
import smtplib


MY_EMAIL = #your email
PASSWORD = #your password
IDEAL_PRICE = 1702
HEADERS = {
    #your header
}
URL= #your url here
response = requests.get(URL,headers=HEADERS)
soup = BeautifulSoup(response.content,"lxml")
price = soup.find(class_="a-price-whole").getText().split(".")[0]
s_price = price.split(",")[0]
e_price = price.split(",")[1]
f_price = float(s_price+e_price)

product = soup.find(id="title").getText().strip()

if f_price<IDEAL_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(password=PASSWORD,user=MY_EMAIL)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,msg=f"Subject:Price drop\n\n{product} is now Rs{price}")