from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:category_id>', views.posts, name='posts'),
    path('detail/<int:post_id>', views.detail, name='detail'),
    path('about', views.about, name='about'),
]