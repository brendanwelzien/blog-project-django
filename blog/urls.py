from django.urls import path
from .views import HomeView, ListView, DetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('base/', BaseView.as_view(), name='base'),
]
