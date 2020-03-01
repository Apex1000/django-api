from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from data import views

urlpatterns = [
    path('data/',views.DataList.as_view()),
    path('data/<int:pk>/',views.DataDetail.as_view()),
    path('customer/',views.CustomerList.as_view()),
    path('customer/<int:pk>/',views.CustomerDetail.as_view()),

]

urlpatterns=format_suffix_patterns(urlpatterns)