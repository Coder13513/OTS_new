from rest_framework import serializers
from attendance.models import *


class classNurserySerializer(serializers.ModelSerializer):
    class Meta:
        model       =     Attendance_class_nursery
        fields      =       '__all__'

class classLKGSerializer(serializers.ModelSerializer):
    class Meta:
        model       =     Attendance_class_LKG
        fields      =       '__all__'
       
class classUKGSerializer(serializers.ModelSerializer):
    class Meta:
        model       =     Attendance_class_UKG
        fields      =       '__all__'

class class1Serializer(serializers.ModelSerializer):
    class Meta:
        model       =     Attendanceclass1
        fields      =       '__all__'
       

class class2Serializer(serializers.ModelSerializer):
    class Meta:
        model       =     Attendance_class_2
        fields      =       '__all__'

class class3Serializer(serializers.ModelSerializer):
    class Meta:
        model       =     Attendance_class_3
        fields      =       '__all__'

class class4Serializer(serializers.ModelSerializer):
    class Meta:
        model       =     Attendance_class_4
        fields      =       '__all__'
       

class class5Serializer(serializers.ModelSerializer):
    class Meta:
        model       =     Attendance_class_5
        fields      =       '__all__'
class class6Serializer(serializers.ModelSerializer):
    class Meta:
        model       =     Attendance_class_6
        fields      =       '__all__'

class class7Serializer(serializers.ModelSerializer):
    class Meta:
        model       =     Attendance_class_7
        fields      =       '__all__'

class class8Serializer(serializers.ModelSerializer):
    class Meta:
        model       =     Attendance_class_8
        fields      =       '__all__'

class class9Serializer(serializers.ModelSerializer):
    class Meta:
        model       =     Attendance_class_9
        fields      =       '__all__'

class class10Serializer(serializers.ModelSerializer):
    class Meta:
        model       =     Attendance_class_10
        fields      =       '__all__'


       