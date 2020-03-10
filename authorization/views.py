from django.shortcuts import render
from .models import Author1, Book1
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# Create your views here.
class AuthorListCreate(ListCreateAPIView):
    queryset = Author1.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetalsUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Author1.objects.all()
    serializer_class = AuthorSerializer


class BookListCreate(ListCreateAPIView):
    queryset = Book1.objects.all()
    serializer_class = BookSerializer

    
class BookRetriveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Book1.objects.all()
    serializer_class = BookSerializer
