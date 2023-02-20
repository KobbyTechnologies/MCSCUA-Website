from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.contact_view, name='contact'),
    path('rate-us', views.RateUs_view, name='rate-us'),
    path('feedback', views.feedback_form, name='feedback'),
    path('subscription', views.subscription_form_view, name='subscription'),
]

