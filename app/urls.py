from django.urls import path
from . import views


urlpatterns = [
	path('', views.posts, name="posts"),
	path('post/<int:p>/', views.post, name="post"),
]