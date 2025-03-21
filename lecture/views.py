
from .models import *
# from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from .serializers import *
from rest_framework import  generics
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated 
from rest_framework.permissions import IsAuthenticated

from authentication.renderer import UserJSONRenderer
from django.core.exceptions import ObjectDoesNotExist

from authentication.permissions import IsAdmin,IsSuper




class lectureList(generics.ListCreateAPIView):
    permission_classes = [IsAdmin|IsSuper]
    queryset = Lecture.objects.all()
    serializer_class = lectureSerializer


class LectrAPIView(generics.GenericAPIView):
   
       
    serializer_class        =   lectureSerializer

    def get(self,request):
        user 			= 		self.request.user
        print(user)
        shopProfile     =		Lecture.objects.filter(teacher=user.id)       
        serializer      =       self.serializer_class(shopProfile,many=True)
        response = {
                'data' : serializer.data
                  }
        return Response(response, status=status.HTTP_200_OK)


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