from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_view, name='index'),
    path('<int:pid>/', views.blog_single, name='single'),
    path('author/<str:author_username>', views.blog_view, name='author'),
    path('search/', views.blog_search, name='search'),
    path('category/<str:cat>/', views.blog_view, name='category'),
    path('tag/<str:tag>/', views.blog_view, name='tag')
]
