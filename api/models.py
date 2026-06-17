from django.conf import settings
from django.db import models
from projects.models import Project
from rent.models import RentalProperty


class Favorite(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="favorites")

    project = models.ForeignKey(Project,on_delete=models.CASCADE,null=True,blank=True)

    rental = models.ForeignKey(RentalProperty,on_delete=models.CASCADE,null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username