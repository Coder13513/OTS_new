from django.db import models
from teacher.models import Teacher
from student.models import Student
from subjects.models import Subject

# Create your models here.

class Assignment(models.Model):
    name = models.CharField(max_length=50)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    # teacher = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.title


class Question(models.Model):
    question = models.CharField(max_length=288)
 
    def __str__(self):
        return self.question


class Choice(models.Model):
    choice = models.CharField(max_length=50)

    def __str__(self):
        return self.title



class Quiz(models.Model):
    # student=models.ForeignKey(User,on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='assignment', blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE,  blank=True, null=False)
    choices = models.ManyToManyField(Choice)
    answer = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='answer', blank=True, null=True)
   

    # def __str__(self):
    #     return self.question

    def __str__(self):
        return F"{self.assignment}'s Quiz'"



# class Score(models.Model):
#     student = models.ForeignKey(User), on_delete=models.CASCADE, related_name='taken_quizzes')
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='taken_quizzes')
#     score = models.FloatField()
#     date = models.DateTimeField(auto_now_add=True)
