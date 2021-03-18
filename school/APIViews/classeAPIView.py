from school.serializers import ClasseSerializer
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from ..models import Classe

""" Classe """
class ListClasseAPIView(ListAPIView):
    """This endpoint lists all classes from the database"""
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer

class CreateClasseAPIView(CreateAPIView):
    """This endpoint allows for creation of a class"""
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer

class UpdateClasseAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific class by passing in the id of the class to update"""
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer

class DeleteClasseAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific class from the database"""
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer