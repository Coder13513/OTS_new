from django.db import models

# Create your models here.


from classes.models import Classes
from authentication.models import User

class Subject(models.Model):
    id=models.AutoField(primary_key=True)
    subject_name=models.CharField(max_length=255)
    class_id=models.ForeignKey(Classes,on_delete=models.CASCADE,default=1)
    teacher=models.OneToOneField(User,on_delete=models.CASCADE)
    
   

    def __str__(self):
        return self.subject_name 