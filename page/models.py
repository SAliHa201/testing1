from django.db import models

# Create your models here(name, email,message).
class Contact(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField()
    subject=models.CharField(max_length=150)
    massege=models.TextField()


    def __str__(self):
        return self.name
