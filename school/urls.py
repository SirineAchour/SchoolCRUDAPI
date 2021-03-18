# myapi/urls.py
"""
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'subjects', views.SubjectViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
"""
from django.urls import path
from school import views

urlpatterns = [
    # subjects
    path("subjects",views.ListSubjectAPIView.as_view(),name="list_subjects"),
    path("subjects/create", views.CreateSubjectAPIView.as_view(),name="create_subject"),
    path("subjects/update/<int:pk>",views.UpdateSubjectAPIView.as_view(),name="update_subject"),
    path("subjects/delete/<int:pk>",views.DeleteSubjectAPIView.as_view(),name="delete_subject"),

    # classes
    path("classes",views.ListClasseAPIView.as_view(),name="list_classes"),
    path("classes/create", views.CreateClasseAPIView.as_view(),name="create_class"),
    path("classes/update/<int:pk>",views.UpdateClasseAPIView.as_view(),name="update_class"),
    path("classes/delete/<int:pk>",views.DeleteClasseAPIView.as_view(),name="delete_class"),

    # students
    path("students",views.ListStudentAPIView.as_view(),name="list_students"),
    path("students/create", views.CreateStudentAPIView.as_view(),name="create_student"),
    path("students/update/<int:pk>",views.UpdateStudentAPIView.as_view(),name="update_student"),
    path("students/delete/<int:pk>",views.DeleteStudentAPIView.as_view(),name="delete_student"),

    # professors
    path("professors",views.ListProfessorAPIView.as_view(),name="list_professors"),
    path("professors/create", views.CreateProfessorAPIView.as_view(),name="create_professor"),
    path("professors/update/<int:pk>",views.UpdateProfessorAPIView.as_view(),name="update_professor"),
    path("professors/delete/<int:pk>",views.DeleteProfessorAPIView.as_view(),name="delete_professor"),

    # grades
    path("grades",views.ListGradeAPIView.as_view(),name="list_grades"),
    path("grades/create", views.CreateGradeAPIView.as_view(),name="create_grade"),
    path("grades/update/<int:pk>",views.UpdateGradeAPIView.as_view(),name="update_grade"),
    path("grades/delete/<int:pk>",views.DeleteGradeAPIView.as_view(),name="delete_grade"),

    # pcs
    path("pcs",views.ListProfessor_Classe_SubjectAPIView.as_view(),name="list_pcs"),
    path("pcs/create", views.CreateProfessor_Classe_SubjectAPIView.as_view(),name="create_pcs"),
    path("pcs/update/<int:pk>",views.UpdateProfessor_Classe_SubjectAPIView.as_view(),name="update_pcs"),
    path("pcs/delete/<int:pk>",views.DeleteProfessor_Classe_SubjectAPIView.as_view(),name="delete_pcs"),
]