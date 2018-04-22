from django.db import models


class OrderItems (models.Model):
    dept_name=models.CharField(max_length=20);
    app_name= models.CharField(max_length=20);
    function = models.CharField(max_length=10);
    vCPU= models.IntegerField();
    RAM=models.IntegerField();
    storage = models.IntegerField();
    amount= models.IntegerField();
    order_status = models.CharField(max_length=50);