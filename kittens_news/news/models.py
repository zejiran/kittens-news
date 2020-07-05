from collections import OrderedDict
from django.db import models
from django.conf import settings
import json
from datetime import datetime
import pytz
from random import randint


def read_news():
    # Decoding JSON file to dictionary.
    with open(settings.NEWS_JSON_PATH, 'r') as json_file:
        news = json.load(json_file)
    # List of all the links in the news.
    links = []
    for post in news:
        # Append individual link to links.
        links.append(str(post['link']))
    print('Reading news')
    return news, links


# Fresh news on top.
def order_recent_news(news):
    # Dictionary for grouping news by date.
    group_dates = {}
    for post in news:
        # Make groups by date.
        add_dates(group_dates, post)
    group_dates = OrderedDict(
        sorted(group_dates.items(), key=lambda x: datetime.strptime(x[0], '%Y-%m-%d'), reverse=True))
    # If you want more accuracy, change keys and try this: "%Y/%m/%d %H:%M:%S"
    return group_dates


# Join posts by same date.
def add_dates(group, actual_post):
    actual_date = actual_post['created'].split()[0]
    # Date is new on dictionary.
    if actual_date not in group:
        group[actual_date] = [actual_post]
    # New post on old date.
    elif actual_post not in group[actual_date]:
        group[actual_date].append(actual_post)


def generate_link(old_links):
    new_link = str(randint(1000, 9999))
    while new_link in old_links:
        new_link = randint(1000, 9999)
    old_links.append(new_link)
    return int(new_link)


def actual_datetime():
    date_time = str(datetime.now(pytz.timezone('America/Bogota')).replace(microsecond=0))
    date_time = date_time[:-6]
    print(date_time)
    return date_time


def update_json(title, text, links, news):
    if title != '' and text != '':
        link = generate_link(links)
        date_time = actual_datetime()
        with open(settings.NEWS_JSON_PATH, 'w+') as json_file:
            news.append({
                'created': date_time,
                'text': text,
                'title': title,
                'link': link
            })
            json_news_str = json.dumps(news, indent=4)
            json_file.write(json_news_str)


def filter_news(group_dates, query):
    filtered_news = {}
    for date in group_dates:
        for post in group_dates[date]:
            if query.lower() in post['title'].lower():
                if date not in filtered_news:
                    filtered_news[date] = [post]
                else:
                    filtered_news[date].append(post)
    return filtered_news
