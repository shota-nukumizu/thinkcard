from django.urls import path
from .api import views

urlpatterns = [
    path('idea/', views.ListView.as_view()),
    path('idea/<int:pk>', views.DetailView.as_view()),
]