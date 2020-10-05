from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import *
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from .serializers import *
from rest_framework import  generics
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import (IsAuthenticated,)

from authentication.renderer import UserJSONRenderer



class LectrAPIView(generics.GenericAPIView):

    serializer_class = lectureSerializer
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
   
    def get(self, request):
        print("enter")
        user = self.request.user
        print(user.id)
        try:
            fav = Lecture.objects.get(teacher_id=user.id)
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



class lectureList(APIView):
    permission_classes = (IsAuthenticated, )
   
    def get(self, request, format=None):
        snippets = Lecture.objects.all()
        serializer = lectureSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = lectureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class lectureDetail(APIView):
  
    def get_object(self, pk):
        try:
            return Lecture.objects.get(pk=pk)
        except Lecture.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = lectureSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = lectureSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)