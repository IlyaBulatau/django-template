from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Category

# Create your views here.
class IndexView(generic.ListView):
    template_name = "index/index.html"
    model = Category
    context_object_name = "categories"


class DetailView(generic.DetailView):
    template_name = "index/detail.html"
    model = Category
    context_object_name = "category"