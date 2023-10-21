from django.db import models

class HouseModel(models.Model):
    OWNERSHIP_STATUS_CHOICE=(('owned','صاحب'),('mortgage','رهن'))
    ownership_status=models.CharField(max_length=10,choices=OWNERSHIP_STATUS_CHOICE)

class VehicleModel(models.Model):
    year=models.DateField()

class DataModel(models.Model):
    MARITAL_STATUS_CHOICE=(('married','متاهل'),('Single','مجرد'))
    age=models.CharField(max_length=3)
    dependents=models.CharField(max_length=16)
    income=models.CharField(max_length=16)
    marital_status=models.CharField(max_length=8,choices=MARITAL_STATUS_CHOICE)
    risk_questions=models.CharField(max_length=1)
    house=models.ForeignKey(to=HouseModel,on_delete=models.CASCADE,null=True,blank=True,related_name='data')
    vehicle=models.ForeignKey(to=VehicleModel,on_delete=models.CASCADE,null=True,blank=True,related_name='data')