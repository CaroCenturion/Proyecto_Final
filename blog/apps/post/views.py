from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.

class blog(CreateView):
    success_url = reverse_lazy('blog')
    template_name = 'post/blog.html'