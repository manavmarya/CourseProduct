from django.db import models
from django.db.models.base import Model
from coursePortal.settings import AUTH_USER_MODEL


class Course(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    creator = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'is_staff': True}, related_name="creator")
    users_enrolled = models.ManyToManyField(AUTH_USER_MODEL, limit_choices_to={'is_staff': False}, related_name="students")
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{0}--{1}".format(self.name, self.creator)

class WishList(models.Model):
    creator = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return  "{0} wished by {1}".format(self.course, self.creator)


    