import requests
from bs4 import BeautifulSoup
from lxml import html


path = 'https://news.sky.com/uk'
path1 = 'https://news.sky.com'
final_news = []


def fetch_response():
    return requests.get(path)


def fetch_using_bs4(resp):
    global final_news
    response = BeautifulSoup(resp.text, 'html.parser')
    news = response.select('.sdc-site-tile__headline-link')
    image = response.select('.sdc-site-tile__image')
    for i in range(len(news)):
        link = news[i].get('href')
        headlines = news[i].getText()
        img = image[i].get('src')
        final_news.append({"image": img, "news": headlines, "link": path1 + link})
    return final_news


def fetch_using_lxml(resp):
    global final_news
    tree = html.fromstring(resp.content)
    length = tree.xpath('//*[@class=""]/div[5]/div/div/div')
    for i in range(1, (len(length) + 1)):
        url = tree.xpath(f'//*[@class=""]/div[5]/div/div/div[{i}]//a')
        news = tree.xpath(f'//*[@class=""]/div[5]/div/div/div[{i}]//span/text()')
        news = ''.join(news)
        for href in url:
            link = href.attrib['href']
            final_news.append({"news": news, "url": path1 + link})
    return final_news


# if __name__=='__main__':
#     response = fetch_response()
#     if response.status_code == 200:
#         print(fetch_using_bs4(response))
