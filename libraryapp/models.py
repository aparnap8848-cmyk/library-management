from django.db import models

# Create your models here.


class Books(models.Model):
    Title=models.CharField(max_length=50)
    Author=models.CharField(max_length=50)
    Category=models.CharField(max_length=50)
    Price=models.DecimalField(max_digits=10,decimal_places=10)
    Publishes_year=models.IntegerField()
    Available=models.BooleanField(max_length=50)



    



    