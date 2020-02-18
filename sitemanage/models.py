from django.db import models

class SiteManage(models.Model):
    siteid          = models.CharField(max_length=50,null=True,blank=True)
    name            = models.CharField(max_length=50,null=True,blank=True)
    clientName      = models.CharField(max_length=50,null=True,blank=True)
    projectIncharge = models.CharField(max_length=50,null=True,blank=True)
    typeOfProject   = models.CharField(max_length=50,null=True,blank=True)
    siteEngineer    = models.CharField(max_length=50,null=True,blank=True)
    startDate       = models.DateField(blank=True,null=True)
    endDate         = models.DateField(blank=True,null=True)
    lunchTime       = models.TimeField(blank=True,null=True)
    startTime       = models.TimeField(blank=True,null=True)
    endTime         = models.TimeField(blank=True,null=True)
    strtBuffer      = models.TimeField(blank=True,null=True)
    endBuffer       = models.TimeField(blank=True,null=True)
    salaryStructure = models.CharField(max_length=50,null=True,blank=True)


from django.db.models.signals import post_save

def id_create(sender,instance,created,*args,**kwargs):
    if created:
        instance.siteid = "site00"+str(instance.id)
        instance.save()


post_save.connect(id_create,sender=SiteManage)