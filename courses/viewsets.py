from rest_framework import viewsets
from .models import Course, WishList
from .serializers import courseSerializer, wishListSerializer
from courses import serializers

class courseViewSet(viewsets.ModelViewSet):
    '''viewset for course CRUD rest api'''
    queryset = Course.objects.all().order_by('-date_added')
    serializer_class = courseSerializer

    def perform_create(self, serializer):
        '''method override to save current user as default'''
        serializer.save(creator = self.request.user)

class wishListViewSet(viewsets.ModelViewSet):
    '''viewset for wishList CRUD rest api'''
    queryset = WishList.objects.all().order_by('-date_added')
    serializer_class = wishListSerializer

    def perform_create(self, serializer):
        '''method override to save current user as default'''
        serializer.save(creator = self.request.user)