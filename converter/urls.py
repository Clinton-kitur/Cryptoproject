
from django.urls import path

from . import views

urlpatterns = [

   path('scraper/', views.ScraperView.as_view(), name='scraper'),
   # path('convert/', views.ConvertView.as_view(), name='convert'),
]