from django.db import models

# Create your models here.
class table_user(models.Model):
    username=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    photo=models.CharField(max_length=500)
    address=models.CharField(max_length=100)
    class Meta:
        db_table="table_user"

