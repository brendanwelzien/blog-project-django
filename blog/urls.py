from django.urls import path
from .views import HomePageView, ListView, DetailView, BaseView, PostDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('details/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]
