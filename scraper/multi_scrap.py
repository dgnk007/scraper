import requests
from bs4 import BeautifulSoup
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
def flipkartPage(search,start_,end_):
    pages =list(range(start_,end_))
    content =[]
    for page in pages:
        try:
            response = requests.get("https://www.flipkart.com/search?q={}&page={}".format(search,page))
            con = BeautifulSoup(response.text, 'html.parser').find_all('div',class_='_2kHMtA')
        except:
            break
        for i in range(len(con)):
            json_data = {}
            json_data["title"] = con[i].find('div',class_='_4rR01T').text.encode('utf-8')
            try:
                json_data["price"] = con[i].find('div',class_='_30jeq3').text[1:].encode('utf-8').replace(',','')
            except:
                json_data["price"] = None
            json_data["link"] = 'www.flipkart.com' + con[i].find('a',class_='_1fQZEK').get("href").encode('utf-8')
            json_data['id'] = json_data['link'].split('/')[-1].split('?')[0]
            content.append(json_data)
    return content
# print(flipkartPage('laptop',1,2))
