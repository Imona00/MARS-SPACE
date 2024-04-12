from rest_framework.views import APIView
from rest_framework.response import Response,  render, redirect
from .serializer import *
from .model import *
from .forms import ProductForm


class RegistertView(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

class LogintView(APIView):
    def post(self, request):
        login = request.data.get('login')
        password = request.data.get('password')
        student = Student.objects.filter(login = login, password = password).first()
        if student:
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        else:
            return Response('Bunday student yoq')  


class RegisterTeacherView(APIView):
    def post(self, request, *args, **kwards):
        serializer = Teacherserializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

class LoginTeacherView(APIView):
    def post(self, request, *args, **kwards):
        login = request.data.get('login')
        password = request.data.get('passoword')
        user = Teacher.objects.filter(login=login, password=password).first()
        if user:
            return Response('success')
        else:
            return Response('fail')
        

