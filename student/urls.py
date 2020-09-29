from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from student import views

urlpatterns = [
    path('student/', views.studentAPIView.as_view()),

    # path('student/new/', views.StudentDetailAPIView.as_view()),
    
    # path('student/old/', views.studentList.as_view()),
    path('student/<int:pk>/', views.studentDetail.as_view()),
]
