from bs4 import BeautifulSoup
from requests import get


def get_news_data():
    url = "https://www.livechart.me/feeds/headlines"
    response = get(url).text
    soup = BeautifulSoup(response , features="xml")

    item = soup.find("item")
    title = item.title.text
    link = item.guid.text
    img = item.enclosure["url"]

    return {"title":title , "link" : link , "image" : img , "type" : "news"}

