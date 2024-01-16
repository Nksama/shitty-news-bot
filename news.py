from requests import get


def get_news_data():
    url = "https://cr-news-api-service.prd.crunchyrollsvc.com/v1/en-US/stories/search?category=Announcements,News,News&page_size=16&page=1"
    try:
        response = get(url).json()
    except Exception as e:
        print(f"AN ERROR OCCURED : {e}")

    data = response['stories'][0]['content']
    title = data['headline']
    img = data['thumbnail']['filename']
    urll = response['stories'][0]['slug']
    link = f"https://crunchyroll.com/news/{urll}"
    return {"title":title , "link" : link , "image" : img , "type" : "news"}