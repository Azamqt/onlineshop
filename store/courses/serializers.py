from rest_framework import serializers
from .models import *
from user.serializers import ProfileSerializer


class ProgrammingLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingLanguages
        fields = '__all__'


class CoursesSerializer(serializers.ModelSerializer):
    teacher = ProfileSerializer()
    programming_languages = ProgrammingLanguagesSerializer(many=True)

    class Meta:
        model = Courses
        fields = '__all__'
