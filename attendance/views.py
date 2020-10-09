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


class class1DetailAPIView(generics.GenericAPIView):
    # queryset                =   Lecture
    permission_classes      =   []
    # authentication_classes  =   [TokenAuthentication,SessionAuthentication]
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

# class class1DetailAPIView(generics.GenericAPIView):
#     queryset                =   Attendanceclass1
#     permission_classes      =   []
#     # authentication_classes  =   [TokenAuthentication,SessionAuthentication]
#     serializer_class        =   class1Serializer

#     def get(self,request):
#         user 			= 		self.request.user
#         print(user)
#         shopProfile     =		Attendanceclass1.objects.filter(teacher=user.id)       
#         serializer      =       self.serializer_class(shopProfile)
#         response = {
#                 'data' : serializer.data
#                   }
#         return Response(response, status=status.HTTP_200_OK)
#         # print(shopProfile)
#         # shopImage       =		ShopImage.objects.get(shop=user.shopprofile)
#         # serialize  		=		class1Serializer(shopProfile,context={'request': request})
#         # serialize  		=		class1Serializer(shopProfile,)
#         # serialize1 		=		ShopImageSerializer(shopImage,context={'request': request})
#         # serialize       =       serialize.data
#         # serialize.update(serialize1.data)
#         # return Response(serialize.data)


class class1List(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset =  Attendanceclass1.objects.all()
    serializer_class = class1Serializer



class LectrAPIView(generics.GenericAPIView):

    serializer_class = class1Serializer
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
   
    def get(self, request):
        print("enter")
        user = self.request.user
        print(user.id)
        print(user)
        try:
            print("get try")
            fav = Attendanceclass1.objects.get(teacher_id=user.id)
            print(fav)
            fav = Attendanceclass1.objects.get(teacher_id=user.id)
            print(fav)
            serializer = self.serializer_class(fav)
            response = {
                'data' : serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
           
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        except:
            response = {
                'message': 'error occurred'
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class class1Detail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Attendanceclass1.objects.all()
    serializer_class =class1Serializer

class class1APIView(generics.GenericAPIView):    
    permission_classes = (IsAuthenticated,)    
    serializer_class = class1Serializer  
    renderer_classes = (UserJSONRenderer,)
   
    def get(self, request):
        print("enter")
        user = self.request.user
        print(user.id)
        try:  
            print('filter try')           
            fav = Attendanceclass1.objects.get(teacher_id=user.id)
            print(fav)           
            serializer = self.serializer_class(fav)                  
            response = {              
                'data' : serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
           
        except ObjectDoesNotExist:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        except:
            response = {
                'message': 'error occurred'
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request, format=None):
        serializer = class1Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class class1CreateAPIView(generics.CreateAPIView):
    queryset                =   Attendanceclass1
    # permission_classes      =   []
    # authentication_classes  =   [SessionAuthentication]
    serializer_class        =   class1Serializer

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)


# class class1List(generics.CreateAPIView):
#     # permission_classes = (IsAdmin,)
#     queryset = Attendance_class_1.objects.all()
#     serializer_class = class1Serializer

    # def create(self, request, *args, **kwargs):

    #     request.POST._mutable = True
    #     payload = request.data    
    #     serializer = self.serializer_class(data=payload)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     response = {
    #         'data': {"channel": serializer.data}
    #     }
    #     return Response(response, status=status.HTTP_201_CREATED)



