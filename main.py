from pyrogram import Client , filters
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton
from news import get_news_data
from db import NewsDb
import os

db = NewsDb()
bot = Client(
    "newsbot" ,
    api_id=6,
    api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e",
    bot_token=os.environ['BOT_TOKEN']
    )

#idk

def main():

    news = get_news_data()
    existing = db.findnews({"type" : "news"})


    if existing is not None:
        if news['title'] == existing['title']:
            print("same shit")
        else:
            db.replace_news(existing , news)
            with bot:
                text = f"**{news['title']}**\n"
                btn = [[InlineKeyboardButton("More info" , url=news['link'])]] 
                bot.send_photo(-1001228391071 , news['image'], text , reply_markup=InlineKeyboardMarkup(btn))
    else:
        db.add_news(news)
        with bot:
            text = f"**{news['title']}**\n"
            btn = [[InlineKeyboardButton("More info" , url=news['link'])]]
            bot.send_photo(-1001228391071 , news['image'], text , reply_markup=InlineKeyboardMarkup(btn))


main()

