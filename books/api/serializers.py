from rest_framework import serializers
from .models import Book
from rest_framework.validators import ValidationError


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


    def validate_name(self, attrs):
        if attrs == 'Game of Madness':
            message = 'This book is not allowed'
            raise ValidationError(message)
        return attrs

