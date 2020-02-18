from django.db import models

# Create your models here.



class shift(models.Model):
    shiftId         = models.CharField(max_length=50)
    shiftstart      = models.TimeField()
    shiftend        = models.TimeField()
    break1start     = models.TimeField()
    break1end       = models.TimeField()
    lunchbreakstart = models.TimeField()
    lunchbreakend   = models.TimeField()
    break2start     = models.TimeField()
    break2end       = models.TimeField()
    siteclosetime   = models.TimeField()
    