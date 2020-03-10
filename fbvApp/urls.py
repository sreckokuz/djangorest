from django.urls import path
from .views import student_list, students_details

urlpatterns = [
    path('students/', student_list),
    path('students/<int:id>', students_details)    
]
