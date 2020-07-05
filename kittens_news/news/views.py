from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View
from .models import read_news, order_recent_news, update_json

news, links = read_news()


def redirect_home(request):
    return redirect('/news/')


class HomeView(View):
    def get(self, request):
        group_dates = order_recent_news(news)
        return render(request, 'news/index.html', context={'news': group_dates})


class NewsView(View):
    def get(self, request, link):
        # Check if link is on news links.
        if link not in links:
            raise Http404
        # Search the corresponding post to the link.
        for post in news:
            if post['link'] == int(link):
                return render(request, 'news/news.html', context={
                    'post': post
                })


class NewsCreateView(View):
    def get(self, request):
        return render(request, 'news/newscreate.html')

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        text = request.POST.get('text')
        update_json(title, text, links, news)
        return redirect('/')
