from school.serializers import SubjectSerializer
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from ..models import Subject

""" Subject """
class ListSubjectAPIView(ListAPIView):
    """This endpoint lists all subjects from the database"""
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class CreateSubjectAPIView(CreateAPIView):
    """This endpoint allows for creation of a subject"""
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class UpdateSubjectAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific subject by passing in the id of the subject to update"""
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class DeleteSubjectAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific subject from the database"""
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer