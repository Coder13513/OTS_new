from django.db import models

# Create your models here.


class_choice=(('NURSERY','nursery'),('LKG','LKG'),('UKG','UKG'),('CLASS1','class 1'),('CLASS2','class 2'),('CLASS3','class 3'),('CLASS4','class 4'),('CLASS5','class 5'),('CLASS6','class 6'),('CLASS7','class 7'),('CLASS8','class 8'),('CLASS9','class 9'),('CLASS10','class 10'))

class  Classes(models.Model):
    id=models.AutoField(primary_key=True)   
    name=models.CharField(max_length=255,choices=class_choice)
   

    def __str__(self):
        return self.name 
