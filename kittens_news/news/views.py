from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View
from .models import news, links, group_dates


def redirect_home(request):
    return redirect('/news/')


class HomeView(View):
    def get(self, request):
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
