from django.db import models


class shiftInfo(models.Model):

    shiftstart      = models.TimeField()
    shiftend        = models.TimeField()
    break1start     = models.TimeField()
    break1end       = models.TimeField()
    lunchbreakstart = models.TimeField()
    lunchbreakend   = models.TimeField()
    break2start     = models.TimeField()
    break2end       = models.TimeField()
    