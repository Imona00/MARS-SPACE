from django.urls import path 
from .views import * 
urlpatterns = [
    path('post/', ProductView.as_view()),
    path('edit/<int:id>', ProductView.as_view()),
    path('get/', Getall_View.as_view()),
]
