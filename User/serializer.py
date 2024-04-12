from rest_framework import serializers
from .model import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class LoginStudent(serializers.ModelSerializers):
    model = Student
    fields = ['login', 'password'] 

class Teacherserializer(serializers.ModelSerializers):
    model = Teacher
    fields = ['login', 'password'] 

class LoginTeacherserializer(serializers.ModelSerializers):
    model = Teacher
    fields = ['login', 'password']   

class GroupSerializer(serializers.ModelSerializers):
    model = Group
    fields = ['login', 'password']   

                  