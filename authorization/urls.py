from django.urls import path
from .views import AuthorDetalsUpdateDelete, AuthorListCreate, BookListCreate, BookRetriveUpdateDelete

urlpatterns = [
    path('author/', AuthorListCreate.as_view()),
    path('author/<int:pk>', AuthorDetalsUpdateDelete.as_view()),
    path('book/', BookListCreate.as_view()),
    path('book/<int:pk>', BookRetriveUpdateDelete.as_view())       
]
