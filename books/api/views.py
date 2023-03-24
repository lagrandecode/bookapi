from django.shortcuts import render
from .models import Book
from django.http import JsonResponse
# Create your views here.

def Book_list(request):
    books = Book.objects.all()
    book_value = list(books.values())
    return JsonResponse({
        'books':book_value
    })

