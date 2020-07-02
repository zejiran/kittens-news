from django.shortcuts import render
from django.views import View

title = 'News'
coming_soon = 'Coming soon'


class NewsView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'news/index.html', context={
                'title': title,
                'text': coming_soon,
            }
        )
