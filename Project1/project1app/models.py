from django.db import models

# Create your models here.
class FirstApp(models.Model):
    Name = models.CharField(max_length=30,default = "NULL")
    ID=models.AutoField
    Contact = models.CharField(max_length=50,default = "NULL")
    Address = models.CharField(max_length=100,default = "NULL")