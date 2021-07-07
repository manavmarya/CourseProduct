from rest_framework import viewsets
from .models import Course, WishList
from .serializers import courseSerializer, wishListSerializer
from courses import serializers

class courseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('-date_added')
    serializer_class = courseSerializer

class wishListViewSet(viewsets.ModelViewSet):
    queryset = WishList.objects.all().order_by('-date_added')
    serializer_class = wishListSerializer

    def perform_create(self, serializer):
        serializer.save()