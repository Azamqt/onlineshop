from django.urls import path, include
from .views import *

urlpatterns = [
    path('user/new', ProfileCreateView.as_view()),
    path('user/<int:pk>', ProfileRetrieveView.as_view()),
    path('user/update/<int:pk>', ProfileUpdateView.as_view()),
    path('user/all', ProfileListView.as_view()),
]
