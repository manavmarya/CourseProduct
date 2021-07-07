from rest_framework import viewsets
from .models import Course, WishList
from .serializers import courseSerializer, wishListSerializer
from courses import serializers

class courseViewSet(viewsets.ModelViewSet):
    '''viewset for course CRUD rest api'''
    queryset = Course.objects.all().order_by('-date_added')
    serializer_class = courseSerializer

class wishListViewSet(viewsets.ModelViewSet):
    '''viewset for wishList CRUD rest api'''
    queryset = WishList.objects.all().order_by('-date_added')
    serializer_class = wishListSerializer

    def get_serializer_context(self):
        context = super(wishListViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context

    def perform_create(self, serializer):
        request = self.context['request']
        serializer.save(creator = request.user)