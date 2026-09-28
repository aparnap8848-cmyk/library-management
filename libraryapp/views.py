from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from libraryapp import BookSerializer,BookModelSerializer



# Create your views here.

class BookCreateListView(APIView):
    def get(self,request,**kwargs): 
        Books=Books.objects.all()
        serializer=BookSerializer(Books,many=True)
        return Response(serializer.data)

    
    def post(self,request):
        Book_name=request.data.get("Book_name")
        author=request.data.get("author")
        catagory=request.data.get("catagory")
        price=request.data.get("price")
        publised_year=request.data.get("publised_year")
        available=request.data.get("available")
        Books.objects.create(Book_name=Book_name,author=author,catagory=catagory,price=price,publised_year=publised_year)
        return Response("Books added successfully")


class BookCreateListView(APIView):
    def get(self,request):
        Books=Books.objects.all()
        serializer=BookModelSerializer(Books,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=BookModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
        
class BookDetailView(APIView):
    def get(self,request,**kwargs):
        try:
            print(kwargs)
            id=kwargs.get("bookid")
            Books=Books.objects.get(id=id)
            serializer=BookModelSerializer(Books)
            return Response(serializer.data)
        except:
            return Response({"msg":"book is doesnt exist"},status=status.HTTP_400_BAD_REQUEST)



    def put(self,request,**kwargs):
        id=kwargs.get("studid")
        Books=Books.objects.get(id=id)
        serializer=BookModelSerializer(Books,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Book updated'})
        

    def delete(self,request,**kwargs):
        try:
             id=kwargs.get("studid")
             Books=Books.objects.get(id=id)
             Books.delete()
             return Response({'msg':'delete book'})
        except:
            return Response({'msg': "invalid book"},status=status.HTTP_400_BAD_REQUEST)












        



   
        