from django.urls import path
from .views import *

urlpatterns = [
    path('programminglanguages/new', ProgrammingLanguagesCreateView.as_view()),
    path('programminglanguages/<int:pk>', ProgrammingLanguagesRetrieveView.as_view()),
    path('programminglanguages/update/<int:pk>', ProgrammingLanguagesUpdateView.as_view()),
    path('programminglanguages/all', ProgrammingLanguagesListView.as_view()),

    path('courses/new', CoursesCreateView.as_view()),
    path('courses/<int:pk>', CoursesRetrieveView.as_view()),
    path('courses/update/<int:pk>', CoursesUpdateView.as_view()),
    path('courses/all', CoursesListView.as_view()),
]
