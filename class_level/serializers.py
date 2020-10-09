from rest_framework import serializers
from .models import *


class classNurserySerializer(serializers.ModelSerializer):
    class Meta:
        model       =     Class_nursery_student
        fields      =       '__all__'

class classLKGSerializer(serializers.ModelSerializer):
    class Meta:
        model       =     Class_lkg_student
        fields      =       '__all__'
       
class classUKGSerializer(serializers.ModelSerializer):
    class Meta:
        model       =     Class_ukg_student
        fields      =       '__all__'

class class1Serializer(serializers.ModelSerializer):
    class Meta:
        model       =     Class_1_student
        fields      =       '__all__'

class class2Serializer(serializers.ModelSerializer):
    class Meta:
        model       =     Class_2_student
        fields      =       '__all__'

class class3Serializer(serializers.ModelSerializer):
    class Meta:
        model       =     Class_3_student
        fields      =       '__all__'

class class4Serializer(serializers.ModelSerializer):
    class Meta:
        model       =     Class_4_student
        fields      =       '__all__'
       

class class5Serializer(serializers.ModelSerializer):
    class Meta:
        model       =     Class_5_student
        fields      =       '__all__'
class class6Serializer(serializers.ModelSerializer):
    class Meta:
        model       =     Class_6_student
        fields      =       '__all__'

class class7Serializer(serializers.ModelSerializer):
    class Meta:
        model       =     Class_7_student
        fields      =       '__all__'

class class8Serializer(serializers.ModelSerializer):
    class Meta:
        model       =     Class_8_student
        fields      =       '__all__'

class class9Serializer(serializers.ModelSerializer):
    class Meta:
        model       =     Class_9_student
        fields      =       '__all__'

class class10Serializer(serializers.ModelSerializer):
    class Meta:
        model       =     Class_10_student
        fields      =       '__all__'


       