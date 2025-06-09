from django.urls import path
from . import views

app_name = 'bbs'
urlspatterns = [
    path('', views.IndexView.as_view(),name="index")
]