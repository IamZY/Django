from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(primary_key=True,max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=50,null=True)
    birthday = models.DateField(null=True)

class Meta:
    ordering = ['name']
    db_table = 'Users'
