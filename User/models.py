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

    def __str__ (self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    day = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    room = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    

class HomeWork(models.Model): 
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    file = models.FileField(upload_to='homework', null=True)
    text = models.TextField(null=True)
    time = models.DateField(auto_now=True)
    coin = models.IntegerField(null=True)

    def __str__(self):
        return self.student.name
    

class Coins(models.Model):
    son = (
        ('-2', '-2'),
        ('1', '1'),
        ('3', '3'),
        ('5', '5'),
        ('10', '10'),
    )
    coins = models.IntegerField(choises = son)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.name
    

class Hackaton(models.Model):
    title = (
        ("Back-end", "Back-end")
        ("Front-end", "Front-end")
        ("Design", "Design")
    )

    




    


