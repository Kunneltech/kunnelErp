from django.db import models


class attendanceManage(models.Model):


    date                = models.DateField()
    labourerid          = models.CharField(max_length=50)
    labourername        = models.CharField(max_length=50)
    labourerclass       = models.CharField(max_length=50)
    labouercategory     = models.CharField(max_length=50)
    labourertype        = models.CharField(max_length=50)
    # intime              = models.TimeField()
    # outtime             = models.TimeField()
    # numberofhours       = models.IntegerField()
    # overtimeallocated   = models.BooleanField()
    # overtimeworked      = models.BooleanField()
    projectid           = models.CharField(max_length=50)


class labourWorkTime(models.Model):

    labourerid  = models.CharField(max_length=50)
    date        = models.DateField()
    intime      = models.TimeField(null=True)
    outtime     = models.TimeField(null=True)
    workhours   = models.TimeField(null=True)
    othours     = models.TimeField(null=True)
    otstatus    = models.BooleanField(default=False)
    #otEnd       = models.TimeField(null=True)
    shiftid     = models.CharField(max_length=50)
    siteid      = models.CharField(max_length=50)