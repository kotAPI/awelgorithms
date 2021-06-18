from django.urls import path

from . import views

urlpatterns = [
    path('', views.listQuestions, name='list'),
    path('<int:blog_id>/', views.detail, name='detail'),
]