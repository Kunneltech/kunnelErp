from django.db import models


class paymentInfo(models.Model):
    transationid    = models.CharField(max_length=20)
    timestamp       = models.TimeField()
    projectid       = models.CharField(max_length=20)
    siteid          = models.CharField(max_length=20)
    amount          = models.CharField(max_length=20)
    debitaccountid  = models.CharField(max_length=20)
    creditaccountid = models.CharField(max_length=20)
    issuer          = models.CharField(max_length=20)
    reciverid       = models.CharField(max_length=20)
    details         = models.CharField(max_length=20)
    resontype       = models.CharField(max_length=20)
    payflag         = models.BooleanField()
    