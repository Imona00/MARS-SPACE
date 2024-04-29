from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from .serializers import *
from User.models import *



class RegisterAdminView(APIView):
    def post(self, request):
        serializers = AdminSerializers(data=request.data)
        if serializers.is_valid(): 
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)
        

class LoginAdminView(APIView):       
    def post(self,request):
        username = request.data.get('username')
        parol = request.data.get('password')
        admin = Admin.objects.filter(username=username      ,password=parol).first()
        if admin:
            return Response("login togri")
        else:
            return Response("Admin topilmadi")
        

class CreateAdminView(APIView):
    def patch(self, request, id):
        admin = Admin.objects.filter(id=id).first()
        if admin:
            serializers = AdminSerializers(instance= admin,data= request.data, partial=True)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            else:
                return Response(serializers.errors)
        else:
            return Response('SORRY Admin NOT FOUND!')
        

    def get(self,request):
        admin = Admin.objects.all()
        if admin:
            serializers = AdminSerializers(admin, many=True)
            return Response(serializers.data)
        else:
            return Response('SORY NOT Admin CRATE')

    def delete(self, request, id):
        Admin = Admin.objects.filter(id = id).first()
        if Admin:
            Admin.delete()
            return Response("O'chirildi")
        else:
            return Response("Bunday admin topilmaydi")
        

class TeacherStudentView(APIView):
    def get(self, request, id):
        user = Student.objects.all()
        if user:
            serializers = AdminSerializers(user, many = True)
            return Response(serializers.data)
        else:
            return Response('SORRY error')
   

    def get(self, request, id):
        teacher = Teacher.objects.all()
        if teacher:
            serializers = AdminSerializers(teacher, many = True)
            return Response(serializers.data)
        else:
            return Response('SORRY error')
 