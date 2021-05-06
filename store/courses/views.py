from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import Courses, ProgrammingLanguages
from .serializers import CoursesSerializer, ProgrammingLanguagesSerializer


class ProgrammingLanguagesCreateView(generics.CreateAPIView):
    queryset = ProgrammingLanguages.objects.all()
    serializer_class = ProgrammingLanguagesSerializer


class ProgrammingLanguagesRetrieveView(generics.RetrieveAPIView):
    queryset = ProgrammingLanguages.objects.all()
    serializer_class = ProgrammingLanguagesSerializer


class ProgrammingLanguagesUpdateView(generics.UpdateAPIView):
    queryset = ProgrammingLanguages.objects.all()
    serializer_class = ProgrammingLanguagesSerializer


class ProgrammingLanguagesListView(generics.ListAPIView):
    queryset = ProgrammingLanguages.objects.all()
    serializer_class = ProgrammingLanguagesSerializer


class CoursesCreateView(generics.CreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer


class CoursesRetrieveView(generics.RetrieveAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer


class CoursesUpdateView(generics.UpdateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer


class CoursesListView(generics.ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

