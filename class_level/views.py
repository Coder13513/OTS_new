from django.shortcuts import render
from django.shortcuts import render
from teacher.models import Teacher
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from teacher.serializers import teacherSerializer
from rest_framework import  generics
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from authentication.renderer import UserJSONRenderer

from rest_framework.permissions import (IsAuthenticated)

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.core.exceptions import ObjectDoesNotExist

from .models import *
from .serializers import *
from authentication.permissions import IsAdmin,IsSuper


# Create your views here.



class class1List(generics.ListCreateAPIView):
    permission_classes = [IsAdmin|IsSuper]
    queryset = Class_1_student.objects.all()
    serializer_class = class1Serializer
class class1Detail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdmin|IsSuper)
    queryset = Class_1_student.objects.all()
    serializer_class =class1Serializer


class class2List(generics.ListCreateAPIView): 
    permission_classes = (IsAdmin|IsSuper)
    queryset = Class_2_student.objects.all()
    serializer_class = class2Serializer
class class2Detail(generics.RetrieveUpdateDestroyAPIView): 
    permission_classes = (IsAdmin,)
    queryset = Class_2_student.objects.all()
    serializer_class =class2Serializer


class class3List(generics.ListCreateAPIView): 
    permission_classes = (IsAdmin,)
    queryset = Class_3_student.objects.all()
    serializer_class = class3Serializer
class class3Detail(generics.RetrieveUpdateDestroyAPIView): 
    permission_classes = (IsAdmin,)
    queryset = Class_3_student.objects.all()
    serializer_class =class3Serializer


class class4List(generics.ListCreateAPIView): 
    permission_classes = (IsAdmin,)
    queryset = Class_4_student.objects.all()
    serializer_class = class4Serializer
class class4Detail(generics.RetrieveUpdateDestroyAPIView): 
    permission_classes = (IsAdmin,)
    queryset = Class_4_student.objects.all()
    serializer_class =class4Serializer


class class5List(generics.ListCreateAPIView):  
    permission_classes = (IsAdmin,)
    queryset = Class_5_student.objects.all()
    serializer_class = class5Serializer
class class5Detail(generics.RetrieveUpdateDestroyAPIView):  
    permission_classes = (IsAdmin,)
    queryset = Class_5_student.objects.all()
    serializer_class =class5Serializer


class class6List(generics.ListCreateAPIView):  
    permission_classes = (IsAdmin,)
    queryset = Class_6_student.objects.all()
    serializer_class = class6Serializer
class class6Detail(generics.RetrieveUpdateDestroyAPIView):  
    permission_classes = (IsAdmin,)
    queryset = Class_6_student.objects.all()
    serializer_class =class6Serializer   

class class7List(generics.ListCreateAPIView):  
    permission_classes = (IsAdmin,)
    queryset = Class_7_student.objects.all()
    serializer_class = class7Serializer
class class7Detail(generics.RetrieveUpdateDestroyAPIView):  
    permission_classes = (IsAdmin,)
    queryset = Class_7_student.objects.all()
    serializer_class =class7Serializer  

class class8List(generics.ListCreateAPIView):  
    permission_classes = (IsAdmin,)
    queryset = Class_8_student.objects.all()
    serializer_class = class8Serializer
class class8Detail(generics.RetrieveUpdateDestroyAPIView):  
    permission_classes = (IsAdmin,)
    queryset = Class_8_student.objects.all()
    serializer_class =class8Serializer   

class class9List(generics.ListCreateAPIView):  
    permission_classes = (IsAdmin,)
    queryset = Class_9_student.objects.all()
    serializer_class = class9Serializer
class class9Detail(generics.RetrieveUpdateDestroyAPIView):  
    permission_classes = (IsAdmin,)
    queryset = Class_9_student.objects.all()
    serializer_class =class9Serializer



class class10List(generics.ListCreateAPIView):  
    permission_classes = (IsAdmin,)
    queryset = Class_10_student.objects.all()
    serializer_class = class10Serializer
class class10Detail(generics.RetrieveUpdateDestroyAPIView):  
    permission_classes = (IsAdmin,)
    queryset = Class_10_student.objects.all()
    serializer_class =class10Serializer  

class classnurList(generics.ListCreateAPIView):  
    permission_classes = (IsAdmin,)
    queryset = Class_nursery_student.objects.all()
    serializer_class = classNurserySerializer
class classnurDetail(generics.RetrieveUpdateDestroyAPIView):   
    permission_classes = (IsAdmin,)
    queryset = Class_nursery_student.objects.all()
    serializer_class =classNurserySerializer

class classlkgList(generics.ListCreateAPIView):  
    permission_classes = (IsAdmin,)
    queryset = Class_lkg_student.objects.all()
    serializer_class = classLKGSerializer
class classlkgDetail(generics.RetrieveUpdateDestroyAPIView):  
    permission_classes = (IsAdmin,)
    queryset = Class_lkg_student.objects.all()  
    serializer_class =classLKGSerializer


class classukgList(generics.ListCreateAPIView):  
    permission_classes = (IsAdmin,)
    queryset = Class_ukg_student.objects.all()
    serializer_class = classUKGSerializer
class classukgDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdmin,)
    queryset = Class_ukg_student.objects.all()
    serializer_class =classUKGSerializer



    

    
