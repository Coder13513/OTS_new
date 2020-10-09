from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from attendance import views

urlpatterns = [
   
    
    path('class1/', views.class1List.as_view()),
    path('class1/<int:pk>/', views.class1Detail.as_view()),
    path('class2/', views.class2List.as_view()),
    path('class2/<int:pk>/', views.class2Detail.as_view()),
    path('class3/', views.class3List.as_view()),
    path('class3/<int:pk>/', views.class3Detail.as_view()),
    path('class4/', views.class4List.as_view()),
    path('class4/<int:pk>/', views.class4Detail.as_view()),
    path('class5/', views.class5List.as_view()),
    path('class5/<int:pk>/', views.class5Detail.as_view()),
    path('class6/', views.class6List.as_view()),
    path('class6/<int:pk>/', views.class6Detail.as_view()),
    path('class7/', views.class7List.as_view()),
    path('class7/<int:pk>/', views.class7Detail.as_view()),
    path('class8/', views.class8List.as_view()),
    path('class8/<int:pk>/', views.class8Detail.as_view()),
    path('class9/', views.class9List.as_view()),
    path('class9/<int:pk>/', views.class9Detail.as_view()),
    path('class10/', views.class10List.as_view()),
    path('class10/<int:pk>/', views.class10Detail.as_view()),
    path('classNursery/', views.classnurList.as_view()),
    path('classNursery/<int:pk>/', views.classnurDetail.as_view()),
    path('classLKG/', views.classlkgList.as_view()),
    path('classLKG/<int:pk>/', views.classlkgDetail.as_view()),
    path('classUKG/', views.classukgList.as_view()),
    path('classUKG/<int:pk>/', views.classukgDetail.as_view()),
   
 ]