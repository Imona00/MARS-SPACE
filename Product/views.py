from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from .models import *
# from .forms import ProductForm


class ProductView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class ProductEditView(APIView):

    def get(self, request, id):
        product = Product.objects.filter(id = id).first()
        if product:
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        else:
            return Response("Bunday mahsulot topilmaydi")
        

    def patch(self, request, id):
        product = Product.objects.filter(id = id).first()
        if product:
            serializer = ProductSerializer(instance = product, data = request.data, patrial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response("Bunday mahsulot topilmadi")
        
    def delete(self, request, id):
        product = Product.objects.filter(id = id).first()
        if product:
            product.delete()
            return Response("O'chirildi")
        else:
            return Response("Bunday mahsulot topilmaydi")
 
class Getall_View(APIView):
    def get(self, request):
        products = Product.objects.all()
        if products:
            serializer = ProductSerializer(products, many = True)
            return Response(serializer.data)
        else:
            return Response("Malumot topilmadi")

