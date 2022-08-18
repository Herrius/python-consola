import requests
import smtplib
from bs4 import BeautifulSoup

EMAIL='youremail@gmail.com'
PASSWORD='yourpassword'



url = "https://www.amazon.com/ASTRO-Gaming-Wireless-Base-Station-PlayStation/dp/B07R4Q8FQY?ref_=ast_sto_dp"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54",
    "Accept-Language": "es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
}

response=requests.get(url,headers=header)
web=response.text

web_scrapping=BeautifulSoup(web,'html.parser')

price=float(web_scrapping.find(id='priceblock_ourprice').getText()[1:])
if price<300:
    with smtplib.SMTP('your stmp') as connection:
        connection.starttls()
        connection.login(EMAIL,PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs='enriqueubaldo97@gmail.com',
            msg=f"Subject:Demo python audifonos\n\nLos audifonos estaban baratos :v"
        )