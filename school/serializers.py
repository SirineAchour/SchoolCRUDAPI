# serializers.py
from rest_framework import serializers
from .models import  Classe, Grade, Professor, Professor_Classe_Subject, Student, Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"

class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = "__all__"
    
class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = "__all__"

class Professor_Classe_SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor_Classe_Subject
        fields = "__all__"