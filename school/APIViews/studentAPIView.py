from school.serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from ..models import Student

""" Student """
class ListStudentAPIView(ListAPIView):
    """This endpoint lists all students from the database"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CreateStudentAPIView(CreateAPIView):
    """This endpoint allows for creation of a student"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class UpdateStudentAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific student by passing in the id of the student to update"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class DeleteStudentAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific student from the database"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer