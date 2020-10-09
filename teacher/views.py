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

from authentication.permissions import IsAdmin,IsSuper


class teacherList(generics.ListCreateAPIView):
    permission_classes = [IsAdmin|IsSuper]
    queryset = Teacher.objects.all()
    serializer_class = teacherSerializer

class teacherAPIView(generics.GenericAPIView):

    serializer_class = teacherSerializer
    
    renderer_classes = (UserJSONRenderer,)
   
    def get(self, request):
        print("enter")
        user = self.request.user
        print(user.id)
        try:
            fav = Teacher.objects.get(user_id=user.id)
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
        serializer = teacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  




class teacherDetail(APIView):

    permission_classes = [IsAdmin|IsSuper]
    """
    Retrieve, update or delete a teacher instance.
    """
    def get_object(self, pk):
        try:
            return Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = teacherSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = teacherSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)