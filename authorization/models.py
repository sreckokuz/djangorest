from django.db import models

# Create your models here.
class Author1(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    
    def __str__(self):
        return self.first_name
    
    
class Book1(models.Model):
    title = models.CharField(max_length=20)
    rating = models.IntegerField()
    author = models.ForeignKey(Author1, related_name='books', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class Test2(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
