from django.db import models

class personal_info(models.Model):

    genchoices = (
        ("Male","Male"),
        ('Female','Female'),
    )

    bloodchoices = (
        ('A+','A+'),
        ('A1+','A1+'),
        ('B+','B+'),
        ('O+','O+'),
        ('O-','O-'),
        ('A-','A-'),
        ('B-','B-')
    )        

    lbourerName         = models.CharField(max_length=100)
    callByName          = models.CharField(max_length=100)
    gender              = models.CharField(max_length=10,choices=genchoices)
    dateOfBirth         = models.DateField()
    fatherName          = models.CharField(max_length=100)
    bloodGroup          = models.CharField(max_length=10,choices=bloodchoices)
    NxtOFKin            = models.CharField(max_length=12)
    contactNumOfNxtOfKin= models.CharField(max_length=12)
    motherTounge        = models.CharField(max_length=20)
    address             = models.TextField()
    city                = models.CharField(max_length=20)
    state               = models.CharField(max_length=50)
    country             = models.CharField(max_length=50)
    pinCode             = models.CharField(max_length=20)
    mobileNUmber        = models.CharField(max_length=12)
    residencePHNumber   = models.CharField(max_length=12)
    emergencyPHNumber   = models.CharField(max_length=12)

class employeement_info(models.Model):
    dateOfJoining       = models.DateField()
    migrateWoker        = models.BooleanField()
    designation         = models.CharField(max_length=20)
    projectNeme         = models.CharField(max_length=50)
    labouerGrade        = models.CharField(max_length=50,default="") 
    labouerGraderatio   = models.IntegerField()
    labourerType        = models.CharField(max_length=50)
    siteName            = models.CharField(max_length=50)
    siteID              = models.CharField(max_length=50)
    siteOfJoining       = models.CharField(max_length=50)
    labourerid          = models.ForeignKey('personal_info',on_delete=models.CASCADE,default=7)

class identity_info(models.Model):
    documentType         = models.CharField(max_length=50)
    documentNumber       = models.CharField(max_length=50)
    nameAsPerTheDocument = models.CharField(max_length=100)
    labourerid           = models.ForeignKey('personal_info',on_delete=models.CASCADE,default=7)

class bankAccount_info(models.Model):
    BankName            = models.CharField(max_length=50)
    ifscCode            = models.CharField(max_length=50)
    branchName          = models.CharField(max_length=50)
    bankAccountNumber   = models.CharField(max_length=50)
    nameinBank          = models.CharField(max_length=50)
    labourerid          = models.ForeignKey('personal_info',on_delete=models.CASCADE,default=7)