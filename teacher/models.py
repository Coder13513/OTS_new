from django.db import models
from authentication.models import User

# Create your models here.
from classes.models import Classes
from subjects.models import Subject
from school.models import School

class Teacher(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    gender=models.CharField(max_length=255)
    phone_Number=models.CharField(max_length=120,null=True,blank=True)
    address=models.CharField(max_length=120,null=True,blank=True) 
    state=models.CharField(max_length=120,null=True,blank=True)
    country=models.CharField(max_length=120,null=True,blank=True)
    class_assigned=models.ManyToManyField(Classes) 
    # school_name=models.ForeignKey(School,on_delete=models.CASCADE)
    # subject_assigned=models.ManyToManyField(Subject)   
  


    def __str__(self):
        return F"{self.user}"
