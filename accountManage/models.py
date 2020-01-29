from django.db import models

# Create your models here.

class accountinfo(models.Model):

    labourerid  = models.CharField(max_length=50)
    timestamp   = models.TimeField()
    phonenumber = models.CharField(max_length=20)
    siteid      = models.CharField(max_length=50)
    recoveryperiod = models.CharField(max_length=50)
    reson          = models.CharField(max_length=150)
    approveid      = models.CharField(max_length=50)
    approvestatus  = models.BooleanField()
    paystatus      = models.BooleanField()


class account(models.Model):
    transationid    = models.CharField(max_length=50)
    timestamp       = models.TimeField()
    projectid       = models.CharField(max_length=50)
    siteid          = models.CharField(max_length=50)
    creditaccountid = models.CharField(max_length=50)
    debitaccountid  = models.CharField(max_length=50)
       
