from django.urls import path,include
from .views import *
from rest_framework import routers

app_name = 'blog'  # Set the app_name to the name of your app

get_author_router = routers.SimpleRouter() 
get_author_router.register('get-author',AuthorListView,basename='authorlist') 

urlpatterns = [
    # Define your app-specific URL patterns
    path('',include(get_author_router.urls)),
    # path('author/',AuthorListView.as_view(),name='author'),
    path('author/<int:pk>',AuthorDetailView.as_view(),name='author_view'),
    path('category/',CategoryListView.as_view(),name='category'),
    path('category/<int:pk>',CategoryDetailView.as_view(),name='category_view'),
    path('tag',TagListView.as_view(),name='tag'),
    path('tag/<int:pk>',TagDetailView.as_view(),name='tag_view'),
    path('Blogpost',BlogPostListView.as_view(),name='Blogpost'),
    path('Blogpost/<int:pk>',BlogPostDetailView.as_view(),name='Blogpost_view'),
    path('comment',CommentListView.as_view(),name='comment'),
    path('comment/<int:pk>',CommentDetailView.as_view(),name='comment_view')
]