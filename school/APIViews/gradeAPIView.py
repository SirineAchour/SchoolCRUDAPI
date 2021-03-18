from school.serializers import GradeSerializer
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from ..models import Grade

""" Grade """
class ListGradeAPIView(ListAPIView):
    """This endpoint lists all grades from the database"""
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

class CreateGradeAPIView(CreateAPIView):
    """This endpoint allows for creation of a grade"""
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

class UpdateGradeAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific grade by passing in the id of the grade to update"""
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

class DeleteGradeAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific grade from the database"""
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer