from django.urls import path

from .views import TodaysPrice


urlpatterns = [
    path('todaysprice/', TodaysPrice.as_view(), name='todays-price'),
]
