from school.serializers import Professor_Classe_SubjectSerializer
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from ..models import Professor_Classe_Subject

""" Professor_Classe_Subject """
class ListProfessor_Classe_SubjectAPIView(ListAPIView):
    """This endpoint lists all entries in Professor_Classe_Subject collection/table from the database"""
    queryset = Professor_Classe_Subject.objects.all()
    serializer_class = Professor_Classe_SubjectSerializer

class CreateProfessor_Classe_SubjectAPIView(CreateAPIView):
    """This endpoint allows for creation of a Professor_Classe_Subject collection/table entry"""
    queryset = Professor_Classe_Subject.objects.all()
    serializer_class = Professor_Classe_SubjectSerializer

class UpdateProfessor_Classe_SubjectAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific Professor_Classe_Subject collection/table entry by passing in the id of the entry to update"""
    queryset = Professor_Classe_Subject.objects.all()
    serializer_class = Professor_Classe_SubjectSerializer

class DeleteProfessor_Classe_SubjectAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Professor_Classe_Subject collection/table entry from the database"""
    queryset = Professor_Classe_Subject.objects.all()
    serializer_class = Professor_Classe_SubjectSerializer