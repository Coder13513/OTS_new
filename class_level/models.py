from django.db import models
from school.models import School
from student.models import Student

# Create your models here.


class Class_nursery_student(models.Model):
    school_name=models.ForeignKey(School,on_delete=models.CASCADE)
    classname=models.CharField(max_length=200,default="class 1",editable=False)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    
    def __str__(self):
        return F'{self.student}'



class Class_lkg_student(models.Model):
    school_name=models.ForeignKey(School,on_delete=models.CASCADE)
    classname=models.CharField(max_length=200,default="class 1",editable=False)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    
    def __str__(self):
        return F'{self.student}'



class Class_ukg_student(models.Model):
    school_name=models.ForeignKey(School,on_delete=models.CASCADE)
    classname=models.CharField(max_length=200,default="class 1",editable=False)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    
    def __str__(self):
        return F'{self.student}'


class Class_1_student(models.Model):
    school_name=models.ForeignKey(School,on_delete=models.CASCADE)
    classname=models.CharField(max_length=200,default="class 1",editable=False)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)

    def __str__(self):
        return F'{self.student}'



class Class_2_student(models.Model):
    school_name=models.ForeignKey(School,on_delete=models.CASCADE)
    classname=models.CharField(max_length=200,default="class 1",editable=False)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    
    def __str__(self):
        return F'{self.student}'



class Class_3_student(models.Model):
    school_name=models.ForeignKey(School,on_delete=models.CASCADE)
    classname=models.CharField(max_length=200,default="class 1",editable=False)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    
    def __str__(self):
        return F'{self.student}'


class Class_4_student(models.Model):
    school_name=models.ForeignKey(School,on_delete=models.CASCADE)
    classname=models.CharField(max_length=200,default="class 1",editable=False)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    
    def __str__(self):
        return F'{self.student}'




class Class_5_student(models.Model):
    school_name=models.ForeignKey(School,on_delete=models.CASCADE)
    classname=models.CharField(max_length=200,default="class 1",editable=False)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    
    def __str__(self):
        return F'{self.student}'



class Class_6_student(models.Model):
    school_name=models.ForeignKey(School,on_delete=models.CASCADE)
    classname=models.CharField(max_length=200,default="class 1",editable=False)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    
    def __str__(self):
        return F'{self.student}'



class Class_7_student(models.Model):
    school_name=models.ForeignKey(School,on_delete=models.CASCADE)
    classname=models.CharField(max_length=200,default="class 1",editable=False)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    
    def __str__(self):
        return F'{self.student}'



class Class_8_student(models.Model):
    school_name=models.ForeignKey(School,on_delete=models.CASCADE)
    classname=models.CharField(max_length=200,default="class 1",editable=False)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    
    def __str__(self):
        return F'{self.student}'



class Class_9_student(models.Model):
    school_name=models.ForeignKey(School,on_delete=models.CASCADE)
    classname=models.CharField(max_length=200,default="class 1",editable=False)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    
    def __str__(self):
        return F'{self.student}'

    

class Class_10_student(models.Model):
    school_name=models.ForeignKey(School,on_delete=models.CASCADE)
    classname=models.CharField(max_length=200,default="class 1",editable=False)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    
    def __str__(self):
        return F'{self.student}'