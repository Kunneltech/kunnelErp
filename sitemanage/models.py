from django.db import models

class SiteManage(models.Model):
	site_id         = models.CharField(max_length=120, null=True, blank=True) 
	name            = models.CharField(max_length=120, null=True, blank=True)
	address         = models.CharField(max_length=120, null=True, blank=True)
	client_name     = models.CharField(max_length=120, null=True, blank=True)
	project_manager = models.CharField(max_length=120, null=True, blank=True)
	project_type    = models.CharField(max_length=120,null=True, blank=True)
	site_engineer   = models.CharField(max_length=120,null=True, blank=True)
	start_date      = models.DateField(null=True, blank=True,)
	end_date        = models.DateField(null=True, blank=True)
	lunch_time      = models.TimeField(null=True, blank=True)
	start_time      = models.TimeField(null=True, blank=True)
	end_time        = models.TimeField(null=True, blank=True)
	start_buffer    = models.TimeField(null=True, blank=True)
	end_buffer      = models.TimeField(null=True, blank=True)
	salary_structure = models.CharField(max_length=120,null=True, blank=True)



	def __str__(self):
		return self.site_id


from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver





def id_creater(sender, instance, created,  *args, **kwargs):
	if created:
		instance.site_id = 'site00' + str(instance.id)
		instance.save()


post_save.connect(id_creater, sender=SiteManage)