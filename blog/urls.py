from django.urls import path
from .import views

urlpatterns = [
    path('<int:pk>/', views.PostList.as_view(), name='post'),
    path('articles/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('featuredarticles', views.FeaturedList.as_view(), name='featuredarticles'),
]