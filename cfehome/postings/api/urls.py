from .views import BlogPostRudView, BlogPostAPIView

from django.urls import path, include
from django.contrib import admin

app_name = 'postings'

urlpatterns = [
    path('', BlogPostAPIView.as_view(), name='post-listcreate'),
    path('<pk>/', BlogPostRudView.as_view(), name='post-rud')
]