from django.db import models
class Article(models.Model):
    vorname=models.CharField(max_length=150)
    nachname=models.CharField(max_length=150)
    date_of_Birth=models.CharField(max_length=150)
    date_of_creation=models.DateTimeField(auto_now_add=True)
    slug=models.CharField(max_length=150)
    
    def __str__(self):
        return self.vorname
    