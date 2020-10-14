from django.urls import path, re_path
from .api import MyQuizListAPI, QuizListAPI,QuizCreateAPI, QuizDetailAPI, SaveUsersAnswer, SubmitQuizAPI,TeacherQuizListAPI,quesListAPI,ansListAPI


urlpatterns = [
	path("quizzes/", QuizListAPI.as_view()),
	path("quizzes/create/", QuizCreateAPI.as_view()),

	re_path(r"quizzes/(?P<slug>[\w\-]+)/$", QuizDetailAPI.as_view()),	
	path("my-quizzes/", MyQuizListAPI.as_view()),
	path("save-answer/", SaveUsersAnswer.as_view()),
	re_path(r"quizzes/(?P<slug>[\w\-]+)/submit/$", SubmitQuizAPI.as_view()), 
	
	path("teacher-quizzes/", TeacherQuizListAPI.as_view()),
	path("question/", quesListAPI.as_view()),
	path("answer/", ansListAPI.as_view()),
]