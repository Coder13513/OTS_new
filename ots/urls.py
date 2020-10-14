"""ots URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('auth/', include(("authentication.urls", "auth"),namespace="auth")),
    path('teacher/', include(("teacher.urls", "teacher"),namespace="teacher")),
    path('student/', include(("student.urls", "student"),namespace="student")),
    path('classLevel/', include(("class_level.urls", "class"),namespace="class")),
    path('lecture/', include(("lecture.urls", "lecture"),namespace="lecture")),
    # path('school/', include(("school.urls", "school"),namespace="school")),
    path('classesList/', include(("classes.urls", "classesList"),namespace="classesList")),
    path('subjects/', include(("subjects.urls", "subjects"),namespace="subjects")),
    path('chapter/', include(("chapter.urls", "chapter"),namespace="chapter")),
    path('attendance/', include(("attendance.urls", "attendance"),namespace="attendance")),
    
    path('nested_admin/', include('nested_admin.urls')),
    path('quiz/', include('quiz.urls')),

    
]
