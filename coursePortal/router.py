from django.db import router
from courses.viewsets import courseViewSet, wishListViewSet
from users.viewsets import userViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('course', courseViewSet)
router.register('wishlist', wishListViewSet)
router.register('user', userViewSet)

