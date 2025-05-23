from django.urls import path
from . import views

urlpatterns = [
    # API endpoints
    path('api/posts/', views.PostListCreateAPIView.as_view(), name='post_list_api'),
    path('api/posts/<int:pk>/', views.PostDetailAPIView.as_view(), name='post_detail_api'),
    path('api/authors/', views.AuthorListCreateAPIView.as_view(), name='author_list_api'),
    path('api/authors/<int:pk>/', views.AuthorDetailAPIView.as_view(), name='author_detail_api'),
    
    # Template views
    path('', views.PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/new/', views.PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    
    path('authors/', views.AuthorListView.as_view(), name='author_list'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('authors/new/', views.AuthorCreateView.as_view(), name='author_create'),
    path('authors/<int:pk>/edit/', views.AuthorUpdateView.as_view(), name='author_update'),
    path('authors/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='author_delete'),
]
