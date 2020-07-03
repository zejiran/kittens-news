from django.db import models
from django.conf import settings
import json

# Decoding JSON file to dictionary.
with open(settings.NEWS_JSON_PATH, 'r') as json_file:
    news = json.load(json_file)
# List of all the links in the news.
links = []
for post in news:
    links.append(str(post['link']))
