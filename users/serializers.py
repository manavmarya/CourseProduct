from django.db import models
from rest_framework import serializers
from .models import User

class userSerializer(serializers.ModelSerializer):
    '''Model serializer is used'''
    class Meta:
        model = User
        fields = ('password','name','email','is_staff')