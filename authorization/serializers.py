from rest_framework import serializers
from .models import Author1, Book1


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book1
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(read_only=True, many=True)

    class Meta:
        model = Author1
        fields = '__all__'
