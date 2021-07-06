from django.db import models
from rest_framework import serializers
from .models import Course, WishList

class courseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class wishListSerializer(serializers.ModelSerializer):
    courseData = serializers.SerializerMethodField()
    userData = serializers.SerializerMethodField()
    class Meta:
        model= WishList
        fields= '__all__'
    
    def get_courseData(self, obj):
        return [obj.course.price, obj.course.creator.name, obj.course.date_added]

    def get_userData(self, obj):
        return [obj.creator.email, obj.creator.is_staff]