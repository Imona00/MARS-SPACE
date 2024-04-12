from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    parent = models.TextField()
    coin = models.IntegerField()
    day = models.IntegerField()


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    lev = (  ('Backend', 'Backend'),
             ('Fronted', 'Fronted'),
             ('Starter', 'Starter'),
             ('Designer', 'Designer'), )
    level = models.CharField(max_length=20, choices=lev)
    day = models.BooleanField(default=False)

    def str(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    day = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    room = models.CharField(max_length=25)

    def str(self):
        return self.name


