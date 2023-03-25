from django.shortcuts import render
from .models import Book
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,APIView
from .serializers import BookSerializer
from rest_framework.parsers import JSONParser
# Create your views here.

# def Book_list(request):
#     books = Book.objects.all()
#     book_value = list(books.values())
#     return JsonResponse({
#         'books':book_value
#     })


# @api_view(['GET','POST'])
# def book_list(request):
#     if request.method == 'GET':
#         book = Book.objects.all()
#         serializers = BookSerializer(book,many=True)
#         return Response(serializers.data)
#     elif request.method == 'POST':
#         serializers = BookSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data)
#         return Response(serializers.errors)

# @api_view(['GET','PUT','DELETE'])
# def book_view(request,pk):
#     try:
#         books = Book.objects.get(pk=pk)
#     except:
#         Book.DoesNotExist
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#     if request.method == 'GET':
#         serializers = BookSerializer(books)
#         return Response(serializers.data)
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializers = BookSerializer(books,data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data)
#         return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         books.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    


class BookList(APIView):
    def get(self,request,format=None):
            books = Book.objects.all()
            serializers = BookSerializer(books,many=True)
            return Response(serializers.data)

    def post(self,request,format=None):
            books = Book.objects.all()
            serializers = BookSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
        
class BookView(APIView):
    def get_object(self,pk):
        try: 
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404
    def get(self,request,pk,format=None):
        books = self.get_object(pk)
        serializers = BookSerializer(books)
        return Response(serializers.data)
    def put(self,request,pk,format=None):
        books = self.get_object(pk)
        serializers = BookSerializer(books,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format=None):
        books = self.get_object(pk)
        books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


