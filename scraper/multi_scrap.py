import requests
import json
import csv
from bs4 import BeautifulSoup

pages =list(range(1,21))
# for page in pages:
#     response = requests.get("https://www.amazon.in/s?k=laptop&page={}".format(page))
#     soup = BeautifulSoup(response.text, 'html.parser')
#     con = soup.find_all('div',class_='s-result-item')
#     for i in range(len(con)):
#         content =[]
#         content.append(con[i].text)
#         len(content)
        # print(content)
    # print(content)
    # for i in range(len(content)):
    #     title = soup.find_all("div", {"class": "s-title-instructions-style"})
    #     print(title)
    #     print("______________________")
search ='laptop'
content =[]
for page in pages:
    response = requests.get("https://www.flipkart.com/search?q={}&page={}".format(search,page))
    con = BeautifulSoup(response.text, 'html.parser').find_all('div',class_='_2kHMtA')
    for i in range(len(con)):
        json_data = {}
        json_data["title"] = con[i].find('div',class_='_4rR01T').text.encode()
        json_data["price"] = con[i].find('div',class_='_30jeq3').text[1:].encode()
        json_data["link"] = 'www.flipkart.com' + con[i].find('a',class_='_1fQZEK').get("href").encode()
        content.append(json_data)
print(len(content))