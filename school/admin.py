from school.models import Classe, Grade, Person, Professor, Professor_Classe_Subject, Student, Subject
from django.contrib import admin

# Register your models here.
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Professor)
admin.site.register(Classe)
admin.site.register(Grade)
admin.site.register(Professor_Classe_Subject)