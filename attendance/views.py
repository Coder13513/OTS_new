from django.shortcuts import render
from .models import *
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from .serializers import *
from rest_framework import  generics
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from authentication.renderer import UserJSONRenderer

from rest_framework.permissions import (IsAuthenticated,)

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.core.exceptions import ObjectDoesNotExist



# Create your views here.


class class1List(generics.GenericAPIView):  
 
    serializer_class        =   class1Serializer

    def get(self,request):
        user 			= 		self.request.user
        print(user)
        shopProfile     =		Attendanceclass1.objects.filter(teacher=user.id)             
        serializer      =       self.serializer_class(shopProfile,many=True)
        response = {
                'data' : serializer.data
                  }
        return Response(response, status=status.HTTP_200_OK)  


    def post(self, request, format=None):
        serializer = class1Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class class1Detail(APIView):
  
    def get_object(self, pk):
        try:
            return Attendanceclass1.objects.get(pk=pk)
        except Attendanceclass1.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = class1Serializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = class1Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  

class class2List(generics.GenericAPIView):  
 
    serializer_class        =   class2Serializer

    def get(self,request):
        user 			= 		self.request.user
        print(user)
        shopProfile     =		Attendance_class_2.objects.filter(teacher=user.id)             
        serializer      =       self.serializer_class(shopProfile,many=True)
        response = {
                'data' : serializer.data
                  }
        return Response(response, status=status.HTTP_200_OK)  


    def post(self, request, format=None):
        serializer = class2Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class class2Detail(APIView):
  
    def get_object(self, pk):
        try:
            return Attendance_class_2.objects.get(pk=pk)
        except Attendance_class_2.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = class2Serializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = class2Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  


class class3List(generics.GenericAPIView):  
 
    serializer_class        =   class3Serializer

    def get(self,request):
        user 			= 		self.request.user
        print(user)
        shopProfile     =		Attendance_class_3.objects.filter(teacher=user.id)             
        serializer      =       self.serializer_class(shopProfile,many=True)
        response = {
                'data' : serializer.data
                  }
        return Response(response, status=status.HTTP_200_OK)  


    def post(self, request, format=None):
        serializer = class3Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class class3Detail(APIView):
  
    def get_object(self, pk):
        try:
            return Attendance_class_3.objects.get(pk=pk)
        except Attendance_class_3.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = class3Serializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = class3Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  

class class4List(generics.GenericAPIView):  
 
    serializer_class        =   class4Serializer

    def get(self,request):
        user 			= 		self.request.user
        print(user)
        shopProfile     =		Attendance_class_4.objects.filter(teacher=user.id)             
        serializer      =       self.serializer_class(shopProfile,many=True)
        response = {
                'data' : serializer.data
                  }
        return Response(response, status=status.HTTP_200_OK)  


    def post(self, request, format=None):
        serializer = class4Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class class4Detail(APIView):
  
    def get_object(self, pk):
        try:
            return Attendance_class_4.objects.get(pk=pk)
        except Attendance_class_4.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = class4Serializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = class4Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class class5List(generics.GenericAPIView):  
 
    serializer_class        =   class5Serializer

    def get(self,request):
        user 			= 		self.request.user
        print(user)
        shopProfile     =		Attendance_class_5.objects.filter(teacher=user.id)             
        serializer      =       self.serializer_class(shopProfile,many=True)
        response = {
                'data' : serializer.data
                  }
        return Response(response, status=status.HTTP_200_OK)  


    def post(self, request, format=None):
        serializer = class5erializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class class5Detail(APIView):
  
    def get_object(self, pk):
        try:
            return Attendance_class_5.objects.get(pk=pk)
        except Attendance_class_5.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = class5Serializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = class5Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   

class class6List(generics.GenericAPIView):  
 
    serializer_class        =   class6Serializer

    def get(self,request):
        user 			= 		self.request.user
        print(user)
        shopProfile     =		Attendance_class_6.objects.filter(teacher=user.id)             
        serializer      =       self.serializer_class(shopProfile,many=True)
        response = {
                'data' : serializer.data
                  }
        return Response(response, status=status.HTTP_200_OK)  


    def post(self, request, format=None):
        serializer = class6Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class class6Detail(APIView):
  
    def get_object(self, pk):
        try:
            return Attendance_class_6.objects.get(pk=pk)
        except Attendance_class_6.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = class6Serializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = class6Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   

class class7List(generics.GenericAPIView):  
 
    serializer_class        =   class7Serializer

    def get(self,request):
        user 			= 		self.request.user
        print(user)
        shopProfile     =		Attendance_class_7.objects.filter(teacher=user.id)             
        serializer      =       self.serializer_class(shopProfile,many=True)
        response = {
                'data' : serializer.data
                  }
        return Response(response, status=status.HTTP_200_OK)  


    def post(self, request, format=None):
        serializer = class7Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class class7Detail(APIView):
  
    def get_object(self, pk):
        try:
            return Attendance_class_7.objects.get(pk=pk)
        except Attendance_class_7.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = class7Serializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = class7Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   

class class8List(generics.GenericAPIView):  
 
    serializer_class        =   class8Serializer

    def get(self,request):
        user 			= 		self.request.user
        print(user)
        shopProfile     =		Attendance_class_8.objects.filter(teacher=user.id)             
        serializer      =       self.serializer_class(shopProfile,many=True)
        response = {
                'data' : serializer.data
                  }
        return Response(response, status=status.HTTP_200_OK)  


    def post(self, request, format=None):
        serializer = class8Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class class8Detail(APIView):
  
    def get_object(self, pk):
        try:
            return Attendance_class_8.objects.get(pk=pk)
        except Attendance_class_8.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = class8Serializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = class8Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   

class class9List(generics.GenericAPIView):  
 
    serializer_class        =   class9Serializer

    def get(self,request):
        user 			= 		self.request.user
        print(user)
        shopProfile     =		Attendance_class_9.objects.filter(teacher=user.id)             
        serializer      =       self.serializer_class(shopProfile,many=True)
        response = {
                'data' : serializer.data
                  }
        return Response(response, status=status.HTTP_200_OK)  


    def post(self, request, format=None):
        serializer = class9Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class class9Detail(APIView):
  
    def get_object(self, pk):
        try:
            return Attendance_class_9.objects.get(pk=pk)
        except Attendance_class_9.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = class9Serializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = class9Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   

class class10List(generics.GenericAPIView):  
 
    serializer_class        =   class10Serializer

    def get(self,request):
        user 			= 		self.request.user
        print(user)
        shopProfile     =		Attendance_class_10.objects.filter(teacher=user.id)             
        serializer      =       self.serializer_class(shopProfile,many=True)
        response = {
                'data' : serializer.data
                  }
        return Response(response, status=status.HTTP_200_OK)  


    def post(self, request, format=None):
        serializer = class10Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class class10Detail(APIView):
  
    def get_object(self, pk):
        try:
            return Attendance_class_10.objects.get(pk=pk)
        except Attendance_class_10.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = class10Serializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = class10Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class classnurList(generics.GenericAPIView):  
 
    serializer_class        =   classNurserySerializer

    def get(self,request):
        user 			= 		self.request.user
        print(user)
        shopProfile     =		Attendance_class_nursery.objects.filter(teacher=user.id)             
        serializer      =       self.serializer_class(shopProfile,many=True)
        response = {
                'data' : serializer.data
                  }
        return Response(response, status=status.HTTP_200_OK)  


    def post(self, request, format=None):
        serializer = classNurserySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class classnurDetail(APIView):
  
    def get_object(self, pk):
        try:
            return Attendance_class_nursery.objects.get(pk=pk)
        except Attendance_class_nursery.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = classNurserySerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = classNurserySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   

class classlkgList(generics.GenericAPIView):  
 
    serializer_class        =   classLKGSerializer

    def get(self,request):
        user 			= 		self.request.user
        print(user)
        shopProfile     =		Attendance_class_LKG.objects.filter(teacher=user.id)             
        serializer      =       self.serializer_class(shopProfile,many=True)
        response = {
                'data' : serializer.data
                  }
        return Response(response, status=status.HTTP_200_OK)  


    def post(self, request, format=None):
        serializer = classLKGSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class classlkgDetail(APIView):
  
    def get_object(self, pk):
        try:
            return Attendance_class_LKG.objects.get(pk=pk)
        except Attendance_class_LKG.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = classLKGSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = classLKGSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class classukgList(generics.GenericAPIView):  
 
    serializer_class        =   classUKGSerializer

    def get(self,request):
        user 			= 		self.request.user
        print(user)
        shopProfile     =		Attendance_class_UKG.objects.filter(teacher=user.id)             
        serializer      =       self.serializer_class(shopProfile,many=True)
        response = {
                'data' : serializer.data
                  }
        return Response(response, status=status.HTTP_200_OK)  


    def post(self, request, format=None):
        serializer = classUKGSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class classukgDetail(APIView):
  
    def get_object(self, pk):
        try:
            return Attendance_class_UKG.objects.get(pk=pk)
        except Attendance_class_UKG.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = classUKGSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = classUKGSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)












