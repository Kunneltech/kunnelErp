from django.db import models


class attendanceManage(models.Model):


    date                = models.DateField()
    labourerid          = models.CharField(max_length=50)
    labourername        = models.CharField(max_length=50)
    labourerclass       = models.CharField(max_length=50)
    shiftid             = models.CharField(max_length=50)
    labouercategory     = models.CharField(max_length=50)
    labourertype        = models.CharField(max_length=50)
    intime              = models.TimeField()
    outtime             = models.TimeField()
    numberofhours       = models.IntegerField()
    overtimeallocated   = models.BooleanField()
    overtimeworked      = models.BooleanField()
    siteid              = models.CharField(max_length=50)
    projectid           = models.CharField(max_length=50)