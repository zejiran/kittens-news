from collections import OrderedDict
from django.db import models
from django.conf import settings
import json
from datetime import datetime


# Join posts by same date.
def add_dates(group, actual_post):
    actual_date = actual_post['created'].split()[0]
    # Date is new on dictionary.
    if actual_date not in group:
        group[actual_date] = [actual_post]
    # New post on old date.
    elif actual_post not in group[actual_date]:
        group[actual_date].append(actual_post)


# Decoding JSON file to dictionary.
with open(settings.NEWS_JSON_PATH, 'r') as json_file:
    news = json.load(json_file)
# List of all the links in the news.
links = []
# Dictionary for grouping news by date.
group_dates = {}
for post in news:
    # Append individual link to links.
    links.append(str(post['link']))
    # Make groups by date.
    add_dates(group_dates, post)
    # Fresh news on top
    # Date
    group_dates = OrderedDict(
        sorted(group_dates.items(), key=lambda x: datetime.strptime(x[0], '%Y-%m-%d'), reverse=True))
    # If you want more accuracy, change keys and try this: "%Y/%m/%d %H:%M:%S"
