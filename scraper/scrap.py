# coding: utf-8
import requests
import json
from bs4 import BeautifulSoup

url ='https://www.amazon.in/Synology-DS220j-2x4TB-Disks-Warranty/dp/B085WQ9CZS/?_encoding=UTF8&pd_rd_w=bSZDb&content-id=amzn1.sym.86bd9ba7-f177-459f-9995-c8e962dd9848&pf_rd_p=86bd9ba7-f177-459f-9995-c8e962dd9848&pf_rd_r=JQH0S82JF4Q9T5EBQYB7&pd_rd_wg=NFiHG&pd_rd_r=39422c8f-ae6c-4008-b681-ccf679a53256&ref_=pd_gw_ci_mcx_mi'
def amazon_scrap(u):
    response = requests.get(u) 
    soup = BeautifulSoup(response.text, 'html.parser')
    data = {}
    data['title'] = soup.find("span", {"id": "productTitle"}).text.strip()
    data['price'] = soup.find("span", {"class": "a-price-whole"}).text.strip() + soup.find("span", {"class": "a-price-fraction"}).text.strip()
    return json.dumps(data)

print(amazon_scrap(url))