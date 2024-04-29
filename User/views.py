from rest_framework.views import APIView
from rest_framework.response import Response,  render, redirect
from .serializer import *
from rest_framework import generics
from .models import *
import datetime



class RegisterView(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

class LoginView(APIView):
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
        
class CreateGroupView(APIView):
    def post(self, request):
        serializers = GroupSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)
        

    def get(self, request):
        groups = Group.objects.all()
        if groups:
            serializers = GroupSerializer(groups, many = True)
            return Response(serializers.data)
        else: 
            return Response('SORRY NOT GROUP CREATE SAW')


class EditGroupView(APIView):
    def get(self, request, id):
        group = Group.onjects.filter(id)
        if group:
            serializers = GroupSerializer(group)
            return Response(serializers.data)
        else:
            return Response('SORRY ERROR')
        

    def patch(self, request, id):
        group = Group.objects.filter(id = id).first()
        if group:
            serializers =GroupSerializer(instance = group, data = request.data, partial = True)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            else:
                return Response(serializers.errors)    
        else:
            return Response('SORRY GROUP NOT FOUND')   
        
          
    def delete(self, request, id):
        group = Group.objects.filter(id = id).first()
        if group:
            group.delete()
            return Response('GROUP DELETED')
        else:
            return Response('SORRY GROUP NOT FOUND')  

      

class HomeWorkView(APIView):
    def post (self, request):
        serializers = HomeWorkSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)
        

    def get(self, request):
        homework = HomeWork.objects.all()
        if homework:
            serializers = HomeWorkSerializer(homework, many = True)
            return Response(serializers.data)
        else:
            return Response('No Homework found')  


class HomeWorkEditView(APIView):
    def post (self, request, id):
        homework = HomeWork.objects.filter(id = id).first()
        if homework:
            homework.file = request.data.get('file')
            diedline = int(homework.time)+3
            if homework.time <= datetime.datetime.today and datetime.datetime.today <= diedline :
                homework.save()
                return Response('Yuklandi')
            else:
                return Response('Chopildiz, Vaqtida yuklash keredi')
        else:
            return Response('Bunday uyga vazifa topilmadi')
        

class PostCoinView(APIView):

    def post(self, request):
        serializers = CoinsSerializer(data=request.data)
        id = request.data.get('student')
        coins = request.data.get('coins')
        student = Student.objects.filter(id = id).first()
        if student:
            if serializers.is_valid():
                student.coin += coins
                student.save()
                serializers.save()           
                return Response(serializers.data)
            else:
                return Response(serializers.errors)
            

class HackatonView(generics.CreateAPIView):
    serializer_class = HackatonSerializer
    queryset = Hackaton.objects.all()


class HackatonGetView(generics.ListAPIView):
    serializer_class = HackatonSerializer 
    queryset = Hackaton.objects.all()  


class EditHackatontView(generics.RetrieveUpdateAPIView):
    serializer_class = HackatonSerializer 
    queryset = Hackaton.filter().first()




        



        

