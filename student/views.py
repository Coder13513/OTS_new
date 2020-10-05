from django.shortcuts import render
from student.models import Student
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from student.serializers import studentSerializer
from rest_framework import  generics
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib.auth.decorators import login_required

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from rest_framework.permissions import (IsAuthenticated)
from authentication.renderer import UserJSONRenderer



class studentAPIView(generics.GenericAPIView):

    serializer_class = studentSerializer
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
   
    def get(self, request):
        print("enter")
        user = self.request.user
        print(user.id)
        try:
            fav = Student.objects.get(user_id=user.id)
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


class SnippetList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = studentSerializer

    def get_queryset(self, *args, **kwargs):
     return Student.objects.all().filter(User=self.request.user)

    # def get(self,request):
    #     user 			= 		self.request.user
    #     print("studentapi:",user)
    #     stud            =		Student.objects.get(User=user)
    #     serialize  		=		studentSerializer(stud,context={'request': request})
        # return Response(serialize.data)
  

class StudentDetailAPIView(generics.GenericAPIView):
    queryset                =   Student
    permission_classes      =   []
    authentication_classes  =   [TokenAuthentication,SessionAuthentication]
    serializer_class        =   studentSerializer

    def get(self,request):
        user 			= 		self.request.user.id
        print("studentapi:",user)
        stu             =		Student.objects.get(User=user)
        serialize  		=		studentSerializer(stu,context={'request': request})
        return Response(serialize.data)

class studentList(APIView):
    """
    List all teachers, or create a new teacher.
    """
  
    def get(self, request, format=None):
        user = self.request.user.id
        print("user :",user)
        queryset=Student.objects.filter(user=user)
        serializer = studentSerializer(queryset, many=True)
        authentication_classes = [TokenAuthentication,SessionAuthentication]
        # snippets = Student.objects.all()
        # serializer = studentSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = studentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class studentDetail(APIView):
    """
    Retrieve, update or delete a teacher instance.
    """
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = studentSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = studentSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)