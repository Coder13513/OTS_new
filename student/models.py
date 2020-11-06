from django.db import models
from authentication.models import User
# from school.models import School
from classes.models import Classes


# Create your models here.



class Student(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    class_id=models.ForeignKey(Classes,on_delete=models.DO_NOTHING)
    gender=models.CharField(max_length=255)
    phone_Number=models.CharField(max_length=120,null=True,blank=True)
    address=models.CharField(max_length=120,null=True,blank=True)
    state=models.CharField(max_length=120,null=True,blank=True)
    country=models.CharField(max_length=120,null=True,blank=True) 

    def __str__(self):
        return F"{self.user}"




# class Class_nursery_student(models.Model):
#     school_name=models.ForeignKey(School,on_delete=models.CASCADE)
#     classname=models.CharField(max_length=200,default="class 1",editable=False)
#     student=models.ForeignKey(Student,on_delete=models.CASCADE)
    
#     def __str__(self):
#         return F'{self.student}'



# class Class_lkg_student(models.Model):
#     school_name=models.ForeignKey(School,on_delete=models.CASCADE)
#     classname=models.CharField(max_length=200,default="class 1",editable=False)
#     student=models.ForeignKey(Student,on_delete=models.CASCADE)
    
#     def __str__(self):
#         return F'{self.student}'



# class Class_ukg_student(models.Model):
#     school_name=models.ForeignKey(School,on_delete=models.CASCADE)
#     classname=models.CharField(max_length=200,default="class 1",editable=False)
#     student=models.ForeignKey(Student,on_delete=models.CASCADE)
    
#     def __str__(self):
#         return F'{self.student}'


# class Class_1_student(models.Model):
#     school_name=models.ForeignKey(School,on_delete=models.CASCADE)
#     classname=models.CharField(max_length=200,default="class 1",editable=False)
#     student=models.ForeignKey(Student,on_delete=models.CASCADE)

#     def __str__(self):
#         return F'{self.student}'



# class Class_2_student(models.Model):
#     school_name=models.ForeignKey(School,on_delete=models.CASCADE)
#     classname=models.CharField(max_length=200,default="class 1",editable=False)
#     student=models.ForeignKey(Student,on_delete=models.CASCADE)
    
#     def __str__(self):
#         return F'{self.student}'



# class Class_3_student(models.Model):
#     school_name=models.ForeignKey(School,on_delete=models.CASCADE)
#     classname=models.CharField(max_length=200,default="class 1",editable=False)
#     student=models.ForeignKey(Student,on_delete=models.CASCADE)
    
#     def __str__(self):
#         return F'{self.student}'


# class Class_4_student(models.Model):
#     school_name=models.ForeignKey(School,on_delete=models.CASCADE)
#     classname=models.CharField(max_length=200,default="class 1",editable=False)
#     student=models.ForeignKey(Student,on_delete=models.CASCADE)
    
#     def __str__(self):
#         return F'{self.student}'




# class Class_5_student(models.Model):
#     school_name=models.ForeignKey(School,on_delete=models.CASCADE)
#     classname=models.CharField(max_length=200,default="class 1",editable=False)
#     student=models.ForeignKey(Student,on_delete=models.CASCADE)
    
#     def __str__(self):
#         return F'{self.student}'



# class Class_6_student(models.Model):
#     school_name=models.ForeignKey(School,on_delete=models.CASCADE)
#     classname=models.CharField(max_length=200,default="class 1",editable=False)
#     student=models.ForeignKey(Student,on_delete=models.CASCADE)
    
#     def __str__(self):
#         return F'{self.student}'



# class Class_7_student(models.Model):
#     school_name=models.ForeignKey(School,on_delete=models.CASCADE)
#     classname=models.CharField(max_length=200,default="class 1",editable=False)
#     student=models.ForeignKey(Student,on_delete=models.CASCADE)
    
#     def __str__(self):
#         return F'{self.student}'



# class Class_8_student(models.Model):
#     school_name=models.ForeignKey(School,on_delete=models.CASCADE)
#     classname=models.CharField(max_length=200,default="class 1",editable=False)
#     student=models.ForeignKey(Student,on_delete=models.CASCADE)
    
#     def __str__(self):
#         return F'{self.student}'



# class Class_9_student(models.Model):
#     school_name=models.ForeignKey(School,on_delete=models.CASCADE)
#     classname=models.CharField(max_length=200,default="class 1",editable=False)
#     student=models.ForeignKey(Student,on_delete=models.CASCADE)
    
#     def __str__(self):
#         return F'{self.student}'

    

# class Class_10_student(models.Model):
#     school_name=models.ForeignKey(School,on_delete=models.CASCADE)
#     classname=models.CharField(max_length=200,default="class 1",editable=False)
#     student=models.ForeignKey(Student,on_delete=models.CASCADE)
    
#     def __str__(self):
#         return F'{self.student}'