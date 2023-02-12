from django.urls import path

from webapp.views.articles import add_view
from webapp.views.base import index_view

urlpatterns = [
    path("", index_view),
    path("article/add/", add_view)
]
