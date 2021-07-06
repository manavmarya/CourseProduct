from django.db import models
from rest_framework import serializers
from .models import Course, WishList

class courseSerializer(serializers.ModelSerializer):
    class Meta:
        model: Course
        fields: '__all__'

class wishListSerializer(serializers.ModelSerializer):
    class Meta:
        model: WishList
        fields: '__all__'