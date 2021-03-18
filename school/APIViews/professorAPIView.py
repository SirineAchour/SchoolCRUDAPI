from school.serializers import ProfessorSerializer
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from ..models import Professor

""" Professor """
class ListProfessorAPIView(ListAPIView):
    """This endpoint lists all professors from the database"""
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class CreateProfessorAPIView(CreateAPIView):
    """This endpoint allows for creation of a professor"""
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class UpdateProfessorAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific professor by passing in the id of the professor to update"""
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class DeleteProfessorAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific professor from the database"""
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer