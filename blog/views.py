from django.views.generic import TemplateView, ListView, DetailView
from.models import blog, Post

class HomeView(ListView):
    template_name = 'home.html'
    model = blog

class BaseView(TemplateView):
    template_name = 'base.html'

class PostDetailView(DetailView):
    template_name = "post_detail.html"
    model = Post