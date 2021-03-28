from django.db import models

# Create your models here.
class Organization(models.Model):
    org_id= models.IntegerField(primary_key=True, auto_created=True, blank=True) #blank=True means field will not be required in form
    orgname = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=30, unique=True)
    phone = models.IntegerField( unique=True)

class User(models.Model):
    user_id= models.IntegerField(primary_key=True, auto_created=True, blank=True) #blank=True means field will not be required in form
    username = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=30, unique=True)
    phone = models.IntegerField( unique=True)
    org_id = models.ForeignKey(Organization, null=True, blank=True, on_delete=models.SET_NULL) 

