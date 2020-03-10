from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework import status
from django.http import Http404


# Create your views here.
class StudentList(APIView):
    
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetails(APIView):
    
    def get_student(self, id):
        try:
            return Student.objects.get(pk=id)
        except Student.DoesNotExist:
            raise Http404
    
    def get(self, request, id):
        student = self.get_student(id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    def put(self, request, id):
        student = self.get_student(id)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        student = self.get_student(id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
