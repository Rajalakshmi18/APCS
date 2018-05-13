from django.db import models


class OrderItems1 (models.Model):
    dept_name=models.CharField(max_length=20);
    app_name= models.CharField(max_length=20);
    function = models.CharField(max_length=10);
    vCPU= models.IntegerField();
    RAM=models.IntegerField();
    storage = models.IntegerField();
    amount= models.IntegerField();
    order_status = models.CharField(max_length=50);
    dr = models.CharField(max_length=20);
    os = models.CharField(max_length=20);
    db = models.CharField(max_length=20);


class Totaltrial(models.Model):
    totalcost=models.IntegerField();

class TotalCosts(models.Model):
    totalDC = models.IntegerField();
    totalServer= models.IntegerField();
    totalNetwork = models.IntegerField();
    LMF= models.IntegerField();
    totalvCPU= models.IntegerField();
    totalRAM = models.IntegerField();
    totalStorage= models.IntegerField();
    microsoft= models.IntegerField();
    redhat= models.IntegerField();
    suse= models.IntegerField();
    otherOS= models.IntegerField();
    oracle= models.IntegerField();
    sql= models.IntegerField();
    totalStorageCost= models.IntegerField();