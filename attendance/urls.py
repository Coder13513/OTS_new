from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from attendance import views

urlpatterns = [
    # path('class1/', views.class1APIView.as_view()),
    path('class1/<int:pk>/', views.class1APIView.as_view()),
    path('class1/', views.class1DetailAPIView.as_view()),
    path('class1test/', views.class1DetailAPIView.as_view()),
    # path('class1/<int:pk>/', views.class1Detail.as_view()),
]