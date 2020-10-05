from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save

from subjects.models import Subject
from authentication.models import User
from classes.models import Classes
from student.models import Student
from teacher.models import Teacher
# from school.models import Class_1_student

# Create your models here.



# class Attendance_class(models.Model):
#   class_attendance=models.ForeignKey(Classes,on_delete=models.DO_NOTHING)
#   class_select=models.TextField(max_length=200,blank=True)

#   def __str__(self):
#         return f'{self.class_select}'



# class class_select(models.Model):
#   class_select=models.TextField(max_length=200)    


class Attendance_class_1(models.Model):
    id=models.AutoField(primary_key=True)
    attendance_class=models.CharField(max_length=200,default="class 1",editable=False)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.DO_NOTHING,blank=True)    
    attendance_date=models.DateTimeField() 
    # student=models.ManyToManyField(Attendance_class)  
    student=models.ManyToManyField(Student)  

    def __str__(self):
        # return (self.student_new)
        return '{0} | Attendance:{1}'.format(self.subject,self.attendance_date.strftime('%d-%b-%y'))


class Attendance_class_2(models.Model):
    id=models.AutoField(primary_key=True)
    attendance_class=models.CharField(max_length=200,default="class 2",editable=False)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.DO_NOTHING,blank=True)    
    attendance_date=models.DateTimeField() 
    # student=models.ManyToManyField(Attendance_class)  
    student=models.ManyToManyField(Student)  

    def __str__(self):
        # return (self.student_new)
        return '{0} | Attendance:{1}'.format(self.subject,self.attendance_date.strftime('%d-%b-%y'))


class Attendance_class_3(models.Model):
    id=models.AutoField(primary_key=True)
    attendance_class=models.CharField(max_length=200,default="class 3",editable=False)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.DO_NOTHING,blank=True)    
    attendance_date=models.DateTimeField() 
    # student=models.ManyToManyField(Attendance_class)  
    student=models.ManyToManyField(Student)  

    def __str__(self):
        # return (self.student_new)
        return '{0} | Attendance:{1}'.format(self.subject,self.attendance_date.strftime('%d-%b-%y'))

class Attendance_class_4(models.Model):
    id=models.AutoField(primary_key=True)
    attendance_class=models.CharField(max_length=200,default="class 4",editable=False)
    subject=models.ForeignKey(Subject,on_delete=models.DO_NOTHING,blank=True)    
    attendance_date=models.DateTimeField() 
    # student=models.ManyToManyField(Attendance_class)  
    student=models.ManyToManyField(Student)  

    def __str__(self):
        # return (self.student_new)
        return '{0} | Attendance:{1}'.format(self.subject,self.attendance_date.strftime('%d-%b-%y'))

class Attendance_class_5(models.Model):
    id=models.AutoField(primary_key=True)
    attendance_class=models.CharField(max_length=200,default="class 5",editable=False)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.DO_NOTHING,blank=True)    
    attendance_date=models.DateTimeField() 
    # student=models.ManyToManyField(Attendance_class)  
    student=models.ManyToManyField(Student)  

    def __str__(self):
        # return (self.student_new)
        return '{0} | Attendance:{1}'.format(self.subject,self.attendance_date.strftime('%d-%b-%y'))

class Attendance_class_6(models.Model):
    id=models.AutoField(primary_key=True)
    attendance_class=models.CharField(max_length=200,default="class 6",editable=False)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)  
    subject=models.ForeignKey(Subject,on_delete=models.DO_NOTHING,blank=True)    
    attendance_date=models.DateTimeField() 
    # student=models.ManyToManyField(Attendance_class)  
    student=models.ManyToManyField(Student)  

    def __str__(self):
        # return (self.student_new)
        return '{0} | Attendance:{1}'.format(self.subject,self.attendance_date.strftime('%d-%b-%y'))


class Attendance_class_7(models.Model):
    id=models.AutoField(primary_key=True)
    attendance_class=models.CharField(max_length=200,default="class 7",editable=False)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.DO_NOTHING,blank=True)    
    attendance_date=models.DateTimeField() 
    # student=models.ManyToManyField(Attendance_class)  
    student=models.ManyToManyField(Student)  

    def __str__(self):
        # return (self.student_new)
        return '{0} | Attendance:{1}'.format(self.subject,self.attendance_date.strftime('%d-%b-%y'))


class Attendance_class_8(models.Model):
    id=models.AutoField(primary_key=True)
    attendance_class=models.CharField(max_length=200,default="class 8",editable=False)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.DO_NOTHING,blank=True)    
    attendance_date=models.DateTimeField() 
    # student=models.ManyToManyField(Attendance_class)  
    student=models.ManyToManyField(Student)  

    def __str__(self):
        # return (self.student_new)
        return '{0} | Attendance:{1}'.format(self.subject,self.attendance_date.strftime('%d-%b-%y'))


class Attendance_class_9(models.Model):
    id=models.AutoField(primary_key=True)
    attendance_class=models.CharField(max_length=200,default="class 9",editable=False)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.DO_NOTHING,blank=True)    
    attendance_date=models.DateTimeField() 
    # student=models.ManyToManyField(Attendance_class)  
    student=models.ManyToManyField(Student)  

    def __str__(self):
        # return (self.student_new)
        return '{0} | Attendance:{1}'.format(self.subject,self.attendance_date.strftime('%d-%b-%y'))


class Attendance_class_10(models.Model):
    id=models.AutoField(primary_key=True)
    attendance_class=models.CharField(max_length=200,default="class 10",editable=False)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.DO_NOTHING,blank=True)    
    attendance_date=models.DateTimeField() 
    # student=models.ManyToManyField(Attendance_class)  
    student=models.ManyToManyField(Student)  

    def __str__(self):
        # return (self.student_new)
        return '{0} | Attendance:{1}'.format(self.subject,self.attendance_date.strftime('%d-%b-%y'))
        
class Attendance_class_nursery(models.Model):
    id=models.AutoField(primary_key=True)
    attendance_class=models.CharField(max_length=200,default="nursery",editable=False)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.DO_NOTHING,blank=True)    
    attendance_date=models.DateTimeField() 
    # student=models.ManyToManyField(Attendance_class)  
    student=models.ManyToManyField(Student)  

    def __str__(self):
        # return (self.student_new)
        return '{0} | Attendance:{1}'.format(self.subject,self.attendance_date.strftime('%d-%b-%y'))


class Attendance_class_LKG(models.Model):
    id=models.AutoField(primary_key=True)
    attendance_class=models.CharField(max_length=200,default="LKG",editable=False)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.DO_NOTHING,blank=True)    
    attendance_date=models.DateTimeField() 
    # student=models.ManyToManyField(Attendance_class)  
    student=models.ManyToManyField(Student)  

    def __str__(self):
        # return (self.student_new)
        return '{0} | Attendance:{1}'.format(self.subject,self.attendance_date.strftime('%d-%b-%y'))

class Attendance_class_UKG(models.Model):
    id=models.AutoField(primary_key=True)
    attendance_class=models.CharField(max_length=200,default="UKG",editable=False)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.DO_NOTHING,blank=True)    
    attendance_date=models.DateTimeField() 
    # student=models.ManyToManyField(Attendance_class)  
    student=models.ManyToManyField(Student)  

    def __str__(self):
        # return (self.student_new)
        return '{0} | Attendance:{1}'.format(self.subject,self.attendance_date.strftime('%d-%b-%y'))

# class Test(models.Model):
#     student_test=models.ManyToManyField(Take_Attendance)



# def  post_save_att_class(sender,instance,created,*args, **kwargs):
#     c=instance.class_attendance
#     print(c)
#     s=Student.objects.all()
#     print(s)
#     e=s.filter(class_id=c)
#     print(e)
#     lst=[]
#     # if not instance.class_select:
#     print("enter")
#     for var in e:
#         lst.append(var)
#         print(lst)
#     Attendance_class.objects.filter(pk=instance.pk).update(class_select=lst)
# post_save.connect(post_save_att_class,sender=Attendance_class)
