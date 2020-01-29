from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class customUser(AbstractUser):
    choices = (
        ('SiteAssistent',"SiteAssistent"),
        ('ProjectIncharge','Project_Incharge'),
    )
    user_type = models.CharField(max_length=100,choices=choices)
    emailid = models.EmailField(max_length=20)
    active = models.BooleanField(default=True)

    # USERNAME_FIELD= 'emailid'
    REQUIRED_FIELDS = []


class Staff(customUser):

    name        = models.CharField(max_length=100)
    address     = models.TextField()
    adaar       = models.IntegerField()
    fatherName = models.CharField(max_length=100)
    department  = models.CharField(max_length=100)
    BankAC     = models.CharField(max_length=100)
    contact     = models.CharField(max_length=100)
    bloodGroup = models.CharField(max_length=10)
    employeeCode = models.CharField(max_length=20)
    salaryStructure = models.CharField(max_length=50)
    class Meta:
        verbose_name = 'Staff'


class SubContractor(customUser):
    
    choices = (
           ('civil',"civil"),
           ('electrical','electrical'),
           ('plumbing','plumbing')
       )    
    category            = models.CharField(max_length=100,choices=choices)
    nameOfContractor    = models.CharField(max_length=50)
    nameOfEmployee      = models.CharField(max_length=50)
    GSTRegistration    = models.CharField(max_length=50)
    adhar               = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'SubContractor'



class SiteManagement(customUser):
    name            = models.CharField(max_length=100)
    address         = models.TextField()
    clientName      = models.CharField(max_length=50)
    projectManager  = models.CharField(max_length=50)
    typeOFProject   = models.CharField(max_length=50)
    siteEngineer    = models.CharField(max_length=50)
    startDate       = models.DateField()
    endDate         = models.DateField()
    lunchTime       = models.TimeField()
    startTime       = models.TimeField()
    salaryStructure = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'SiteManagement'    


class customAdmin(customUser):
    companyName = models.CharField(max_length=200)
    epmployeeId = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    is_admin    = models.BooleanField()
    
    class Meta:
        verbose_name = 'customAdmin'