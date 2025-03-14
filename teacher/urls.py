from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from teacher import views

urlpatterns = [
   
    path('teacher/', views.teacherAPIView.as_view()),
    path('teacher/<int:pk>/', views.teacherDetail.as_view()),
    path('teacher/admin/', views.teacherList.as_view()),
]
