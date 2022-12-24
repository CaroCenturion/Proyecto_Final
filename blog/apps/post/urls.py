from django.urls import path

from . import views

app_name = 'post'

urlpatterns = [
    
    path('blog/', views.blog.as_view(), name = 'blog'),
]
