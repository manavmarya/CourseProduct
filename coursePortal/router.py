from django.db import router
from courses.viewsets import courseViewSet, wishListViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('course', courseViewSet)
router.register('wishlist', wishListViewSet)

