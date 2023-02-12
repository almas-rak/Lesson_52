from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def add_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'article_create.html')
    print(request.POST)
    context = {
        'title': request.POST.get('title'),
        'text': request.POST.get('text'),
        'author': request.POST.get('author')
    }
    return render(request, 'article.html', context=context)


