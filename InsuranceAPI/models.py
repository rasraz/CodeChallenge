from django.db import models

# Model for recording and storing user insurance risk data
class DataModel(models.Model):
    MARITAL_STATUS_CHOICE=(('married','married'),('Single','Single'))
    OWNERSHIP_STATUS_CHOICE=(('owned','owned'),('mortgage','mortgage'))
    age=models.CharField(max_length=3)
    dependents=models.CharField(max_length=16)
    income=models.CharField(max_length=16)
    marital_status=models.CharField(max_length=8,choices=MARITAL_STATUS_CHOICE)
    risk_questions=models.CharField(max_length=1)
    house=models.CharField(max_length=10,null=True,blank=True,choices=OWNERSHIP_STATUS_CHOICE)
    vehicle=models.DateField(null=True,blank=True)