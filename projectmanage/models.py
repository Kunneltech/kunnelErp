from django.db import models


class project(models.Model):
    projectName = models.CharField(max_length=100)
    # projectid   = models.AutoField()

class site(models.Model):
    sitename           = models.CharField(max_length=100)
    numberOflabourer   = models.IntegerField()
    projectId          = models.ForeignKey('project',on_delete=models.CASCADE)
    compensationamount = models.IntegerField()
    compensationdays   = models.IntegerField()
    concreteamount     = models.IntegerField()
    creditaccountid    = models.CharField(max_length=20)
    debitaccountid     = models.CharField(max_length=20)
    # siteid             = models.AutoField()
    

