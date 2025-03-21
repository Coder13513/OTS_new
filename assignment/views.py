from django.shortcuts import render
from assignment.models import *
# from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from .serializers import *
# from rest_framework import  generics
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# -------------assignment---------------


class assignmentList(APIView):
    """
    List all assignment, or create a new assignment.
    """
    def get(self, request, format=None):
        snippets = Assignment.objects.all()
        serializer = assignmentSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer =assignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class assignmentDetail(APIView):
    """
    Retrieve, update or delete a assignment instance.
    """
    def get_object(self, pk):
        try:
            return Assignment.objects.get(pk=pk)
        except Assignment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = assignmentSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = assignmentSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ------------question----------------

class questionList(APIView):
    """
    List all question, or create a new question.
    """
    def get(self, request, format=None):
        snippets = Question.objects.all()
        serializer = questionSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer =questionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class questionDetail(APIView):
    """
    Retrieve, update or delete a question instance.
    """
    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = questionSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = questionSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# -----------------choice---------------

class choiceList(APIView):
    """
    List all choice, or create a new choice.
    """
    def get(self, request, format=None):
        snippets = Choice.objects.all()
        serializer = choiceSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer =choiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class choiceDetail(APIView):
    """
    Retrieve, update or delete a choice instance.
    """
    def get_object(self, pk):
        try:
            return Choice.objects.get(pk=pk)
        except Choice.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = choiceSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = choiceSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ----------------quiz-------------


class quizList(APIView):
    """
    List all quiz, or create a new quiz.
    """
    def get(self, request, format=None):
        snippets = Quiz.objects.all()
        serializer = quizSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer =quizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class quizDetail(APIView):
    """
    Retrieve, update or delete a quiz instance.
    """
    def get_object(self, pk):
        try:
            return Quiz.objects.get(pk=pk)
        except Quiz.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = quizSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = quizSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
