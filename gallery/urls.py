from django.urls import path
from . import views


urlpatterns = [
    path('media-hub', views.gallery_view, name='gallery'),
    path('media-hub/ImageDetail/<int:pk>', views.PhotoGalleryDetails.as_view(), name='PhotoGalleryDetails'),
    path('media-hub/VideoDetail/<int:pk>', views.VideoGalleryDetails.as_view(), name='VideoGalleryDetails'),
]