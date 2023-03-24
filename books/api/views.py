from django.shortcuts import render
from .models import Book
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,APIView
from .serializers import BookSerializer
from rest_framework.parsers import JSONParser
# Create your views here.

def Book_list(request):
    books = Book.objects.all()
    book_value = list(books.values())
    return JsonResponse({
        'books':book_value
    })


@api_view(['GET'])
def book_list(request):
    if request.method == 'GET':
        book = Book.objects.all()
        serializers = BookSerializer(book,many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializers = BookSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)




