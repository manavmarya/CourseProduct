from django.db import models
from rest_framework import serializers
from .models import Course, WishList

class courseSerializer(serializers.ModelSerializer):
    '''using model serializers with creator as hidden field to parse it in the end'''
    creator = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
    class Meta:
        model = Course
        fields = '__all__' # wouldn't show creator as made read_only

class wishListSerializer(serializers.ModelSerializer):
    '''using model serializers with creator as hidden field to parse it in the end'''
    courseData = serializers.SerializerMethodField()
    userData = serializers.SerializerMethodField()
    creator = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
    class Meta:
        model= WishList
        fields = '__all__' # wouldn't show creator as made read_only
    
    def get_courseData(self, obj):
        '''course attributes as list'''
        return [obj.course.price, obj.course.creator.name, obj.course.date_added]

    def get_userData(self, obj):
        '''user attributes as list'''
        return [obj.creator.email, obj.creator.is_staff]