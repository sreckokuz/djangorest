from django.urls import path
from .views import StudentList, StudentDetails

urlpatterns = [
    path('students/', StudentList.as_view()),
    path('students/<int:id>', StudentDetails.as_view())    
]
