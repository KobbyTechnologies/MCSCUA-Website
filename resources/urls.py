from django.urls import path
from resources import views

urlpatterns = [
    path('resource-center/category/<int:pk>', views.reports_view, name='publication'),
    path('resource-center/faq/', views.faq_view, name='faq'),
    path('resource-center/terms-of-service/', views.terms, name='terms'),
    path('resource-center/privacy-policy/', views.privacy, name='privacy'),
    path('auditServiceView', views.auditServiceView, name='auditServiceView'),
    path('customerSurvey', views.customerSurvey, name='customerSurvey'),
]
