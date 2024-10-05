from django.urls import path
from .views import BlogList, BlogDetail, CommentList, RegisterView, LoginView

urlpatterns = [
    path('blogs/', BlogList.as_view(), name='blog-list'),
    path('blogs/<int:pk>/', BlogDetail.as_view(), name='blog-detail'),
    path('blogs/<int:blog_pk>/comments/', CommentList.as_view(), name='comment-list'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
