from django.urls import path

from . import views

urlpatterns = [
    path('search/', views.post_search, name='post_search'),
]