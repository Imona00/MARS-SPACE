from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class LoginStudent(serializers.ModelSerializers):
    class Meta:
        model = Student
        fields = ['login', 'password'] 

class Teacherserializer(serializers.ModelSerializers):
    class Meta:
        model = Teacher
        fields = '__all__' 

class LoginTeacherserializer(serializers.ModelSerializers):
    class Meta:
        model = Teacher
        fields = '__all__'   

class GroupSerializer(serializers.ModelSerializers):
    class Meta:
        model = Group
        fields = '__all__'   

class HomeWorkSerializer(serializers.ModelSerializers):
    class Meta:
        model = Group
        fields = '__all__' 

class CoinsSerializer(serializers.ModelSerializers):
    class Meta:
        model = Coins
        fields = '__all__'

class  HackatonSerializer(serializers.ModelSerializers):
    class Meta:
        model = Hackaton
        fields = '__all__'


        

                                