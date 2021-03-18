from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=60)
    cin = models.CharField(max_length=10)
    birthday = models.DateField()

    class Meta:
        abstract = True

class Classe(models.Model):
    name = models.CharField(max_length=60)
    load = models.IntegerField(default=0) # number of students in class
    year = models.IntegerField()
        
    def __str__(self):
        return self.name

class Student(Person):
    student_id = models.CharField(max_length=60)
    classs = models.ManyToManyField(Classe, blank=True)
        
    def __str__(self):
        return self.student_id

class Professor(Person):
        
    def __str__(self):
        return self.person.name

class Subject(models.Model):
    name = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name

class Grade(models.Model):
    grade = models.FloatField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Professor_Classe_Subject(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    classs = models.ForeignKey(Classe, on_delete=models.CASCADE)